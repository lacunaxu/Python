# Optional module
from typing import Tuple
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def longest_word_in_text(url: str) -> Tuple[str, int]:
    """
    Find the longest word in the text file hosted on the web, along with its length.
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


def analyze_quotes(url: str) -> dict:
    """
    Fetches the quotes and their associated tags from the given URL and returns a dictionary
    where quotes are keys and associated tags are values.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            raise Exception("No quotes found to Scrape")

        quote_tags = {}
        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True).strip("“”")
            tags = []
            for tag in quote.find_all("a", class_="tag"):
                tags.append(tag.get_text())

            quote_tags[text] = tags

        return quote_tags
    except RequestException:
        raise Exception("Invalid URL")
