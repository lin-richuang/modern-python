from modern_python import wikipedia


# no need to import mock_requests_get becasue it is in conftest.py file
# and will be automatically picked up by pytest
def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
