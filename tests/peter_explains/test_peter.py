import os
import time
from peter_explains._version import __version__


def test_version_option(script_runner):
    """
    Test the --version option of the 'peter' command-line tool.

    This function runs the 'peter' command with the '--version' option using the provided
    script_runner fixture. It then asserts that the command executed successfully and that
    the output contains the value of the '__version__' variable.
    """
    ret = script_runner.run(["peter", "--version"])
    assert ret.success
    assert __version__ in ret.stdout


def test_peter_help_option(script_runner):
    """
    Test case to verify the behavior of the `peter` command with the `--help` option.

    Args:
        script_runner: An instance of the `ScriptRunner` class for running the command-line script.

    Returns:
        None

    Raises:
        AssertionError: If the command execution fails or the expected output is not found.
    """
    ret = script_runner.run(["peter", "--help"])
    assert ret.success
    assert "how to use" in ret.stdout.lower()


def test_api_key_option(script_runner):
    """
    Test the API key option of the 'peter' script.

    This function runs the 'peter' script with the '--api' option and the value of the 'GOOGLE_API_KEY' environment variable.
    It asserts that the script execution is successful and that the phrase "there ya go" is present in the output.

    Args:
        script_runner: A fixture provided by the testing framework for running scripts.

    Returns:
        None
    """
    ret = script_runner.run(["peter", "--api", os.environ.get("GOOGLE_API_KEY")])
    assert ret.success
    assert "there ya go" in ret.stdout.lower()


def test_delete_api_key_option(script_runner):
    """
    Test case to verify the behavior of the '--delete-api' option in the 'peter' command.

    Args:
        script_runner: A fixture provided by the testing framework.

    Returns:
        None

    Raises:
        AssertionError: If the test fails.

    """
    ret = script_runner.run(["peter", "--delete-api"])
    assert ret.success
    assert "deleted" in ret.stdout.lower()


def test_peter_command(script_runner):
    """
    Test case for the 'peter' command.

    This test case verifies the behavior of the 'peter' command by running it with different arguments and checking the output.

    Args:
        script_runner: A fixture provided by the testing framework for running command-line scripts.

    Returns:
        None

    Raises:
        AssertionError: If any of the assertions fail.

    """
    script_runner.run(["peter", "--api", os.environ.get("GOOGLE_API_KEY")])
    ret = script_runner.run(["peter", "ls"])
    assert ret.success
    assert "command" in ret.stdout.lower()
    assert "purpose" in ret.stdout.lower()
    assert "syntax" in ret.stdout.lower()
    assert "options" in ret.stdout.lower()
    assert "examples" in ret.stdout.lower()


def test_peter_command_with_option(script_runner):
    """
    Test case for the 'peter' command with an option.

    This test case verifies the behavior of the 'peter' command when it is
    executed with an option. It checks if the command runs successfully,
    and if the expected output is present in the command's stdout.

    Args:
        script_runner: A fixture provided by the testing framework.

    Returns:
        None
    """
    script_runner.run(["peter", "--api", os.environ.get("GOOGLE_API_KEY")])
    ret = script_runner.run(["peter", '"ls -la"'])
    assert ret.success
    assert "command" in ret.stdout.lower()
    assert "purpose" in ret.stdout.lower()
    assert "breakdown" in ret.stdout.lower()


def test_result_caching(script_runner):
    """
    Test the result caching functionality of the 'peter' command-line tool.

    This test case verifies that the 'peter' command caches the results of previous commands
    and retrieves them from the cache instead of making a new API call.

    Args:
        script_runner: An instance of the ScriptRunner class for running command-line scripts.

    Returns:
        None
    """
    script_runner.run(["peter", "--api", os.environ.get("GOOGLE_API_KEY")])

    # delete cache
    ret = script_runner.run(["peter", "--delete-cache"])
    assert ret.success
    assert "a fresh new start" in ret.stdout.lower()

    # measure the time taken to run the command
    start = time.time()
    ret = script_runner.run(["peter", "grep"])
    end = time.time()
    assert ret.success
    # assert it is more than 1 second
    assert end - start > 1

    # measure the time taken to run the command again
    start = time.time()
    ret = script_runner.run(["peter", "grep"])
    end = time.time()
    # assert it it is less than 1 second
    assert end - start < 1.5
