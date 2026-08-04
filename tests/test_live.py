"""
Smoke tests against the real Gemini API.

Deselected by default (see `addopts` in pyproject.toml). Run with:

    GOOGLE_API_KEY=<key> uv run pytest -m live

These exist to catch google-genai contract drift and model response-shape
changes, which the mocked suite cannot see. They consume API quota, so CI runs
them only on a schedule or manual dispatch — never on pull requests.
"""

import os

import pytest
from click.testing import CliRunner

from peter_explains.main import peter

pytestmark = pytest.mark.live

runner = CliRunner()


@pytest.fixture
def live_api_key():
    """
    Store the real API key in the isolated config dir.

    The `live` marker keeps conftest's autouse stub out of the way, so these
    calls reach Gemini for real; `isolated_app_dir` still redirects the key
    file and cache into tmp_path.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY is not set")

    runner.invoke(peter, ["--api", api_key])
    return api_key


def test_live_simple_command(live_api_key):
    ret = runner.invoke(peter, ["ls"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower()
        for keyword in ["command", "purpose", "syntax", "options", "examples"]
    )


def test_live_command_with_arguments(live_api_key):
    ret = runner.invoke(peter, ["ls -la"])
    assert ret.exit_code == 0
    assert all(
        keyword in ret.output.lower() for keyword in ["command", "purpose", "breakdown"]
    )
