import json

import pytest

from peter_explains import peter_ai

FAKE_API_KEY = "AIza" + "x" * 35

WITHOUT_ARGUMENTS_RESPONSE = json.dumps(
    {
        "command_name": "ls",
        "purpose": "Shows ya what's in the freakin' folder.",
        "syntax": "ls [options] <directory>",
        "options": ["-l: the long boring one", "-a: shows the sneaky hidden stuff"],
        "examples": ["ls -l", "ls /home"],
    }
)

WITH_ARGUMENTS_RESPONSE = json.dumps(
    {
        "command_name": "ls -la",
        "purpose": "Lists everything, even the stuff tryin' to hide.",
        "breakdown": ["ls: the listin' thing", "-la: long format plus hidden files"],
    }
)


class FakeResponse:
    def __init__(self, text: str):
        self.text = text


class FakeModels:
    def __init__(self, recorder: "FakeGenaiClient"):
        self._recorder = recorder

    async def generate_content(self, *, model, contents, config):
        FakeGenaiClient.calls.append({"model": model, "contents": contents})
        # "breakdown" appears only in the WITH_ARGUMENTS template, so the
        # canned response matches whichever prompt explain_command picked.
        if "breakdown" in contents:
            return FakeResponse(WITH_ARGUMENTS_RESPONSE)
        return FakeResponse(WITHOUT_ARGUMENTS_RESPONSE)


class FakeAio:
    def __init__(self, recorder: "FakeGenaiClient"):
        self.models = FakeModels(recorder)
        self._recorder = recorder

    async def aclose(self):
        FakeGenaiClient.closed += 1


class FakeGenaiClient:
    """Stand-in for genai.Client that records calls instead of hitting the network."""

    calls: list[dict] = []
    closed = 0

    def __init__(self, *, api_key: str):
        self.api_key = api_key
        self.aio = FakeAio(self)

    @classmethod
    def reset(cls):
        cls.calls = []
        cls.closed = 0


@pytest.fixture(autouse=True)
def isolated_app_dir(tmp_path, monkeypatch):
    """
    Redirect the API key file and cache into tmp_path.

    get_app_data_dir resolves from HOME on POSIX and LOCALAPPDATA on Windows,
    so patching both keeps the developer's real key and cache untouched.
    """
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))


@pytest.fixture(autouse=True)
def fake_genai(request, monkeypatch):
    """
    Replace the Gemini client so the suite needs no API key and no network.

    Tests marked `live` deliberately talk to the real API and are left alone.
    """
    FakeGenaiClient.reset()
    if request.node.get_closest_marker("live") is None:
        monkeypatch.setattr(peter_ai.genai, "Client", FakeGenaiClient)
    return FakeGenaiClient
