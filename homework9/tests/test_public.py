from lab9 import analyze_quotes, longest_word_in_text

def test_longest_word_in_text():
    """Tests for the longest_word_in_text function."""
    valid_url1 = "https://www.gutenberg.org/files/1661/1661-0.txt"
    valid_url2 = "http://data.pr4e.org/romeo-full.txt"
    valid_url3 = "https://www.gutenberg.org/files/1662/1662-8.txt"
    invalid_url = "https://www.invalidurl.com/files/404.txt"

    expected_result1 = ("disproportionately", 18)
    expected_result2 = ("satisfaction", 12)
    expected_result3 = ("Bundesverfassungsgericht", 24)

    # Test valid URLs
    for url, expected in [(valid_url1, expected_result1), (valid_url2, expected_result2), (valid_url3, expected_result3)]:
        try:
            result = longest_word_in_text(url)
            assert result == expected, f"Failed: {url}, expected {expected}, got {result}"
            print(f"Passed: {url}")
        except Exception as e:
            print(f"Error while testing {url}: {e}")

    # Test invalid URL
    try:
        longest_word_in_text(invalid_url)
        print("Failed: Expected an exception for invalid URL")
    except Exception as e:
        print(f"Passed: Invalid URL test with exception: {e}")

def test_analyze_quotes():
    """Tests for the analyze_quotes function."""
    analyze_quotes_link1 = "http://quotes.toscrape.com/page/1/"
    analyze_quotes_link2 = "http://quotes.toscrape.com/page/2/"
    invalid_url = "http://quotes.toscrape.com/abc/"
    empty_page_url = "http://quotes.toscrape.com/page/100/"

    expected_result1 = {
        "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.": [
            "change",
            "deep-thoughts",
            "thinking",
            "world",
        ],
        "It is our choices, Harry, that show what we truly are, far more than our abilities.": [
            "abilities",
            "choices",
        ],
    }

    expected_result2 = {
        "This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.": [
            "friends",
            "heartbreak",
            "inspirational",
            "life",
            "love",
            "sisters",
        ]
    }

    # Test valid URLs
    for url, expected in [(analyze_quotes_link1, expected_result1), (analyze_quotes_link2, expected_result2)]:
        try:
            result = analyze_quotes(url)
            assert result == expected, f"Failed: {url}, expected {expected}, got {result}"
            print(f"Passed: {url}")
        except Exception as e:
            print(f"Error while testing {url}: {e}")

    # Test invalid URL
    try:
        analyze_quotes(invalid_url)
        print("Failed: Expected an exception for invalid URL")
    except Exception as e:
        print(f"Passed: Invalid URL test with exception: {e}")

    # Test empty page URL
    try:
        analyze_quotes(empty_page_url)
        print("Failed: Expected an exception for empty page URL")
    except Exception as e:
        print(f"Passed: Empty page URL test with exception: {e}")

if __name__ == "__main__":
    print("Testing longest_word_in_text...")
    test_longest_word_in_text()
    print("\nTesting analyze_quotes...")
    test_analyze_quotes()
