from lab6 import CarLine, Library, RecentHistory

def test_library_operations():
    library = Library()

    # Add books
    library.add_book(101, "To Kill a Mockingbird", "Harper Lee", "9780061120084")
    print(library.get_book_info(101))

    library.add_book(102, "1984", "George Orwell", "9780451524935")
    print(library.borrow_book(102))

    library.add_book(103, "Brave New World", "Aldous Huxley", "9780060850524")
    print(library.filter_books_by_availability(True))

    library.update_book_info(101, title="To Kill a Mockingbird - Revised")
    print(library.get_book_info(101))

    library.remove_book(103)
    try:
        print(library.get_book_info(103))
    except ValueError as e:
        print(f"Error: {e}")


def test_car_line_operations():
    car_line = CarLine()

    # Add cars
    car_line.add_car("ABC123")
    car_line.add_car("DEF456")
    car_line.add_car("GHI789")
    print(car_line)

    # Service cars
    print(car_line.service())
    print(car_line)

    print(car_line.service())
    print(car_line)

    print(car_line.service())
    print(car_line)

    # Try servicing when no cars are in line
    try:
        car_line.service()
    except ValueError as e:
        print(f"Error: {e}")


def test_recent_history_operations():
    history = RecentHistory()

    # Add items
    history.add("file1.txt")
    history.add("file2.txt")
    history.add("file3.txt")
    print(history)

    # Access oldest and newest
    print(f"Newest: {history.newest()}")
    print(f"Oldest: {history.oldest()}")

    # Remove items
    print(f"Removed: {history.remove()}")
    print(history)

    print(f"Removed: {history.remove()}")
    print(history)

    print(f"Removed: {history.remove()}")
    print(history)

    # Try removing when empty
    try:
        history.remove()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Testing Library Operations:")
    test_library_operations()

    print("\nTesting Car Line Operations:")
    test_car_line_operations()

    print("\nTesting Recent History Operations:")
    test_recent_history_operations()
