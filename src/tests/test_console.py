"""
execution code: poetry run pytest
execution with cover: poetry run pytest --cov

You should generally have a single assertion per test case,
because more fine-grained test cases make it easier to figure out why the test suite failed when it does.
"""
import requests
import click.testing
import pytest

from modern_python import console


# Text fixtures are simple functions declared with pytest
@pytest.fixture
def runner():
    """Invokes the command line interface within a test case
    """
    return click.testing.CliRunner()


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0  # Checks if the function exits with a status code of 0


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output  # test for specific word in the output=


def test_main_invokes_requests_get(runner, mock_requests_get):
    """mocks can be inspected to see if they were called
    """
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    """Mock objects also allow you to inspect the arguments they were called with, using the call_args attribute.
    """
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    """You can configure a mock to raise an exception instead of returning a value
    by assigning the exception instance or class to the side_effect attribute of the mock.
    """
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


# Handling exceptions
def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


#@TODO not sure why this is not working
# @pytest.fixture
# def mock_wikipedia_random_page(mocker):
#     return mocker.patch("modern_python.wikipedia.random_page")
#
#
# def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
#     """As the second step, we make the new functionality accessible from the command line, adding a --language option.
#     The test case mocks the wikipedia.random_page function,
#     and uses the assert_called_with method on the mock
#     to check that the language specified by the user is passed on to the function:
#     """
#     runner.invoke(console.main, ['--language = pl'])
#     mock_wikipedia_random_page.assert_called_with(language="pl")


