import os
import stat
from typing import TYPE_CHECKING

import pytest
from click.testing import CliRunner

from peter_explains import __version__
from peter_explains.api_key import GoogleApiKey
from peter_explains.main import peter

from .conftest import FAKE_API_KEY

if TYPE_CHECKING:
    from click import BaseCommand

    peter: BaseCommand

runner = CliRunner()


@pytest.fixture
def set_api_key():
    """Store an API key so the explanation path can run."""
    runner.invoke(peter, ["--api", FAKE_API_KEY])


def test_version_option():
    """Test the --version option."""
    ret = runner.invoke(peter, ["--version"])
    assert ret.exit_code == 0
    assert __version__ in ret.output


def test_peter_help_option():
    """Test the --help option."""
    ret = runner.invoke(peter, ["--help"])
    assert ret.exit_code == 0
    assert "how to use" in ret.output.lower()


def test_api_key_option():
    """Test setting the API key."""
    ret = runner.invoke(peter, ["--api", FAKE_API_KEY])
    assert ret.exit_code == 0
    assert "there ya go" in ret.output.lower()
    assert GoogleApiKey().get() == FAKE_API_KEY


@pytest.mark.skipif(os.name != "posix", reason="POSIX permission bits only")
def test_api_key_file_is_not_world_readable(set_api_key):
    """The stored key must not be readable by group or other."""
    mode = os.stat(GoogleApiKey.get_api_key_file_path()).st_mode
    assert stat.S_IMODE(mode) & 0o077 == 0


def test_api_key_rejects_implausible_key():
    """Keys outside the accepted length range are refused."""
    ret = runner.invoke(peter, ["--api", "too-short"])
    assert ret.exit_code == 1
    assert "valid key" in ret.output.lower()


def test_delete_api_key_option(set_api_key):
    """Test deleting the API key."""
    ret = runner.invoke(peter, ["--delete-api"])
    assert ret.exit_code == 0
    assert "deleted" in ret.output.lower()
    assert not os.path.exists(GoogleApiKey.get_api_key_file_path())


def test_delete_api_key_without_stored_key():
    """Deleting a key that was never set must not blow up."""
    ret = runner.invoke(peter, ["--delete-api"])
    assert ret.exit_code == 0


def test_peter_command(set_api_key, fake_genai):
    """Test running 'peter' with a simple command."""
    ret = runner.invoke(peter, ["ls"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower()
        for keyword in ["command", "purpose", "syntax", "options", "examples"]
    )
    assert len(fake_genai.calls) == 1


def test_peter_command_with_option(set_api_key, fake_genai):
    """Test running 'peter' with an argument that includes options."""
    ret = runner.invoke(peter, ["ls -la"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower() for keyword in ["command", "purpose", "breakdown"]
    )
    assert len(fake_genai.calls) == 1


def test_command_without_api_key_is_rejected(fake_genai):
    """Explaining a command with no stored key must not reach the API."""
    ret = runner.invoke(peter, ["ls"])
    assert ret.exit_code == 1
    assert "api key" in ret.output.lower()
    assert fake_genai.calls == []


def test_result_caching(set_api_key, fake_genai):
    """A repeated command is served from cache instead of the API."""
    ret = runner.invoke(peter, ["--delete-cache"])
    assert ret.exit_code == 0
    assert "a fresh new start" in ret.output.lower()

    first = runner.invoke(peter, ["grep"])
    assert first.exit_code == 0
    assert len(fake_genai.calls) == 1

    second = runner.invoke(peter, ["grep"])
    assert second.exit_code == 0
    assert len(fake_genai.calls) == 1  # served from cache, no second API call
    assert second.output == first.output
