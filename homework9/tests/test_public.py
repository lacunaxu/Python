import os

import pytest
from lab9 import analyze_quotes, longest_word_in_text

valid_url1 = "https://www.gutenberg.org/files/1661/1661-0.txt"
valid_url2 = "http://data.pr4e.org/romeo-full.txt"
valid_url3 = "https://www.gutenberg.org/files/1662/1662-8.txt"
invalid_url = "https://www.invalidurl.com/files/404.txt"

expected_result1 = ("disproportionately", 18)
expected_result2 = ("satisfaction", 12)
expected_result3 = ("Bundesverfassungsgericht", 24)


@pytest.mark.parametrize(
    "url, expected",
    [
        (valid_url1, expected_result1),
        (valid_url2, expected_result2),
        (valid_url3, expected_result3),
    ],
)
def test_longest_word_in_text_valid(url, expected):
    result = longest_word_in_text(url)
    assert result == expected, f"For {url}, expected {expected}, but got {result}"


@pytest.mark.timeout(5)
def test_longest_word_in_text_invalid_url():
    with pytest.raises(Exception) as excinfo:
        longest_word_in_text(invalid_url)
    assert str(excinfo.value) == "Invalid URL", f"Expected 'Invalid URL', but got {str(excinfo.value)}"


analyze_quotes_link1 = "http://quotes.toscrape.com/page/1/"
analyze_quotes_link2 = "http://quotes.toscrape.com/page/2/"
invalid_url = "http://quotes.toscrape.com/abc/"
empty_page_url = "http://quotes.toscrape.com/page/100/"


def assert_dicts_equal_unordered(dict1, dict2):
    assert dict1.keys() == dict2.keys()

    for key in dict1:
        assert sorted(dict1[key]) == sorted(dict2[key])


@pytest.mark.parametrize(
    "url, expected",
    [
        (
            analyze_quotes_link1,
            {
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
                "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.": [
                    "inspirational",
                    "life",
                    "live",
                    "miracle",
                    "miracles",
                ],
                "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.": [
                    "aliteracy",
                    "books",
                    "classic",
                    "humor",
                ],
                "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.": [
                    "be-yourself",
                    "inspirational",
                ],
                "Try not to become a man of success. Rather become a man of value.": [
                    "adulthood",
                    "success",
                    "value",
                ],
                "It is better to be hated for what you are than to be loved for what you are not.": [
                    "life",
                    "love",
                ],
                "I have not failed. I've just found 10,000 ways that won't work.": [
                    "edison",
                    "failure",
                    "inspirational",
                    "paraphrased",
                ],
                "A woman is like a tea bag; you never know how strong it is until it's in hot water.": [
                    "misattributed-eleanor-roosevelt"
                ],
                "A day without sunshine is like, you know, night.": [
                    "humor",
                    "obvious",
                    "simile",
                ],
            },
        ),
        (
            analyze_quotes_link2,
            {
                "This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.": [
                    "friends",
                    "heartbreak",
                    "inspirational",
                    "life",
                    "love",
                    "sisters",
                ],
                "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.": [
                    "courage",
                    "friends",
                ],
                "If you can't explain it to a six year old, you don't understand it yourself.": [
                    "simplicity",
                    "understand",
                ],
                "You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.": [
                    "love"
                ],
                "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.": [
                    "fantasy"
                ],
                "I may not have gone where I intended to go, but I think I have ended up where I needed to be.": [
                    "life",
                    "navigation",
                ],
                "The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.": [
                    "activism",
                    "apathy",
                    "hate",
                    "indifference",
                    "inspirational",
                    "love",
                    "opposite",
                    "philosophy",
                ],
                "It is not a lack of love, but a lack of friendship that makes unhappy marriages.": [
                    "friendship",
                    "lack-of-friendship",
                    "lack-of-love",
                    "love",
                    "marriage",
                    "unhappy-marriage",
                ],
                "Good friends, good books, and a sleepy conscience: this is the ideal life.": [
                    "books",
                    "contentment",
                    "friends",
                    "friendship",
                    "life",
                ],
                "Life is what happens to us while we are making other plans.": [
                    "fate",
                    "life",
                    "misattributed-john-lennon",
                    "planning",
                    "plans",
                ],
            },
        ),
    ],
)
@pytest.mark.timeout(7)
def test_analyze_quotes_valid(url, expected):
    result = analyze_quotes(url)
    assert_dicts_equal_unordered(result, expected)


@pytest.mark.timeout(5)
def test_analyze_quotes_invalid_url():
    with pytest.raises(Exception):
        analyze_quotes(invalid_url)


@pytest.mark.timeout(5)
def test_analyze_quotes_empty_page():
    with pytest.raises(Exception):
        analyze_quotes(empty_page_url)
