from dataclasses import dataclass

import click

import requests

API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Page:
    """Return a random page

    Args:
        language: The Wikipedia language edition. By default, the English
            Wikipedia page is used.

    Returns:
        A page resource

    Raise:
        ClickException: the Http request failed or the HTTP response
            contained an invalid body

    Example:
        >>> from modern_python import wikipedia
        >>> page = wikipedia.random_page(language='en')
        >>> bool(page.Title)
        True
    """
    url = API_URL.format(language=language)
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)


@dataclass
class Page:
    """
    Page resource.

    Attributes:
        title: The tile of the Wikipedia page
        extract: A plain text summary
    """
    title: str
    extract: str