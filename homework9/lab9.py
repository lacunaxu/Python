# Optional module
from typing import Tuple, Dict
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def longest_word_in_text(url: str) -> Tuple[str, int]:
    """
    Find the longest word in a text file hosted on the web and its length.

    Args:
        url (str): The URL of the text file to fetch and analyze.

    Returns:
        Tuple[str, int]: A tuple containing the longest word and its length.

    Raises:
        Exception: If the URL is invalid or the request fails.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()

        words = []
        word = ""
        for char in resp.text:
            if char.isalpha():
                word += char
            else:
                if word:
                    words.append(word)
                word = ""
        if word:
            words.append(word)

        longest_word = max(words, key=len)
        return longest_word, len(longest_word)

    except RequestException:
        raise Exception("Invalid URL")


def analyze_quotes(url: str) -> Dict[str, list]:
    """
    Fetch and analyze quotes and their tags from a given webpage.

    Args:
        url (str): The URL of the webpage containing quotes to scrape.

    Returns:
        Dict[str, list]: A dictionary where the keys are quotes (str) and the values
        are lists of associated tags (list[str]).

    Raises:
        Exception: If the URL is invalid, the request fails, or no quotes are found on the page.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            raise Exception("No quotes found to scrape")

        quote_tags = {}
        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True).strip("“”")
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

            quote_tags[text] = tags

        return quote_tags
    except RequestException:
        raise Exception("Invalid URL")
