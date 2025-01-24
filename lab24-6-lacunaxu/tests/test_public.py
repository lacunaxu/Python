import pytest
from lab6 import CarLine, Library, RecentHistory


def test_library_operations():
    library = Library()

    library.add_book(101, "To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book_info = library.get_book_info(101)
    assert book_info == {
        "book_id": 101,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084",
        "available": True,
    }

    library.add_book(102, "1984", "George Orwell", "9780451524935")

    borrowed_info = library.borrow_book(101)
    assert borrowed_info == {
        "book_id": 101,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084",
        "available": False,
    }

    returned_info = library.return_book(101)
    assert returned_info == {
        "book_id": 101,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084",
        "available": True,
    }

    borrowed_info = library.borrow_book(102)
    assert borrowed_info == {
        "book_id": 102,
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "available": False,
    }

    book_info = library.get_book_info(101)
    assert book_info == {
        "book_id": 101,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780061120084",
        "available": True,
    }

    library.add_book(103, "Brave New World", "Aldous Huxley", "9780060850524")
    library.add_book(104, "The Catcher in the Rye", "J.D. Salinger", "9780316769488")

    available_books = library.filter_books_by_availability(True)
    assert available_books == [
        {
            "book_id": 101,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "9780061120084",
            "available": True,
        },
        {
            "book_id": 103,
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "isbn": "9780060850524",
            "available": True,
        },
        {
            "book_id": 104,
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "isbn": "9780316769488",
            "available": True,
        },
    ]

    unavailable_books = library.filter_books_by_availability(False)
    assert unavailable_books == [
        {
            "book_id": 102,
            "title": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "available": False,
        }
    ]

    updated_book = library.update_book_info(101, title="To Kill a Mockingbird - Updated", author="Harper Lee - Updated")
    assert updated_book == {
        "book_id": 101,
        "title": "To Kill a Mockingbird - Updated",
        "author": "Harper Lee - Updated",
        "isbn": "9780061120084",
        "available": True,
    }

    updated_book = library.update_book_info(104, isbn="9780316769601")
    assert updated_book == {
        "book_id": 104,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "isbn": "9780316769601",
        "available": True,
    }

    library.add_book(105, "Moby Dick", "Herman Melville", "9781503280786")
    assert library.get_book_info(105) == {
        "book_id": 105,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "isbn": "9781503280786",
        "available": True,
    }

    library.remove_book(105)

    with pytest.raises(ValueError):
        library.get_book_info(105)


def test_car_line_operations():
    car_line = CarLine()

    car_line.add_car("ABC123")
    car_line.add_car("DEF456")
    car_line.add_car("GHI789")

    assert str(car_line) == "ABC123 -> DEF456 -> GHI789"
    assert car_line.count_cars() == 3
    assert not car_line.is_empty()

    assert car_line.service() == "ABC123"
    assert str(car_line) == "DEF456 -> GHI789"
    assert car_line.count_cars() == 2

    assert car_line.service() == "DEF456"
    assert str(car_line) == "GHI789"
    assert car_line.count_cars() == 1

    assert car_line.service() == "GHI789"
    assert car_line.count_cars() == 0
    assert car_line.is_empty()

    with pytest.raises(ValueError):
        car_line.service()


def test_invalid_car_registration():
    car_line = CarLine()

    with pytest.raises(ValueError):
        car_line.add_car(12345)


def test_recent_history_operations():
    history = RecentHistory()

    history.add("file1.txt")
    history.add("file2.txt")
    history.add("file3.txt")

    assert str(history) == "file3.txt -> file2.txt -> file1.txt"
    assert history.count_items() == 3
    assert not history.is_empty()

    assert history.newest() == "file3.txt"
    assert str(history) == "file3.txt -> file2.txt -> file1.txt"

    assert history.oldest() == "file1.txt"
    assert str(history) == "file3.txt -> file2.txt -> file1.txt"

    assert history.remove() == "file3.txt"
    assert str(history) == "file2.txt -> file1.txt"
    assert history.count_items() == 2

    assert history.remove() == "file2.txt"
    assert history.count_items() == 1
    assert not history.is_empty()

    assert history.remove() == "file1.txt"
    assert history.count_items() == 0
    assert history.is_empty()

    with pytest.raises(ValueError):
        history.remove()


def test_invalid_item_type():
    history = RecentHistory()

    with pytest.raises(ValueError):
        history.add(12345)


def test_empty_oldest_and_newest():
    history = RecentHistory()

    with pytest.raises(ValueError):
        history.oldest()

    with pytest.raises(ValueError):
        history.newest()
