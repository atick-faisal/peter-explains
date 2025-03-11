import os
import time
from typing import TYPE_CHECKING

import pytest
from click.testing import CliRunner

from peter_explains import __version__
from peter_explains.main import peter

if TYPE_CHECKING:
    from click import BaseCommand

    peter: BaseCommand

runner = CliRunner()


@pytest.fixture
def api_key():
    """Fixture to fetch the API key from the environment or set a default."""
    return os.getenv("GOOGLE_API_KEY", "default_key")


@pytest.fixture
def set_api_key(api_key):
    """Fixture to set the API key before tests."""
    runner.invoke(peter, ["--api", api_key])


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


def test_api_key_option(api_key):
    """Test setting the API key."""
    ret = runner.invoke(peter, ["--api", api_key])
    assert ret.exit_code == 0
    assert "there ya go" in ret.output.lower()


def test_delete_api_key_option():
    """Test deleting the API key."""
    ret = runner.invoke(peter, ["--delete-api"])
    assert ret.exit_code == 0
    assert "deleted" in ret.output.lower()


def test_peter_command(set_api_key):
    """Test running 'peter' with a simple command."""
    ret = runner.invoke(peter, ["ls"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower()
        for keyword in ["command", "purpose", "syntax", "options", "examples"]
    )


def test_peter_command_with_option(set_api_key):
    """Test running 'peter' with an argument that includes options."""
    ret = runner.invoke(peter, ["ls -la"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower() for keyword in ["command", "purpose", "breakdown"]
    )


def test_result_caching(set_api_key):
    """Test caching functionality."""
    # Clear the cache
    ret = runner.invoke(peter, ["--delete-cache"])
    assert ret.exit_code == 0
    assert "a fresh new start" in ret.output.lower()

    # Measure execution time for first command
    start = time.time()
    ret = runner.invoke(peter, ["grep"])
    end = time.time()
    assert ret.exit_code == 0
    assert end - start > 0.7  # First call should take time

    # Measure execution time for cached command
    start = time.time()
    ret = runner.invoke(peter, ["grep"])
    end = time.time()
    assert ret.exit_code == 0
    assert end - start < 1.5  # Cached call should be faster
