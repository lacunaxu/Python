class Library:
    """
    A class representing a library system for managing books.

    Attributes:
        book_dict (dict): A dictionary storing book information with book IDs as keys.
    """

    def __init__(self):
        """
        Initialize the Library with an empty book dictionary.
        """
        self.book_dict = {}

    def add_book(self, book_id: int, title: str, author: str, isbn: str) -> None:
        """
        Add a new book to the library.

        Args:
            book_id (int): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN of the book.

        Raises:
            ValueError: If the book ID already exists.
        """
        if book_id in self.book_dict:
            raise ValueError("Book ID already exists")

        self.book_dict[book_id] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }

    def borrow_book(self, book_id: int) -> dict:
        """
        Borrow a book from the library if it is available.

        Args:
            book_id (int): ID of the book to borrow.

        Returns:
            dict: Information about the borrowed book.

        Raises:
            ValueError: If the book ID is invalid or the book is already borrowed.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        if not self.book_dict[book_id]["available"]:
            raise ValueError("Book is already borrowed")

        self.book_dict[book_id]["available"] = False
        book_info = self.book_dict[book_id]
        book_info['book_id'] = book_id
        return book_info

    def return_book(self, book_id: int) -> dict:
        """
        Return a borrowed book to the library.

        Args:
            book_id (int): ID of the book to return.

        Returns:
            dict: Updated information about the returned book.

        Raises:
            ValueError: If the book ID is invalid.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        self.book_dict[book_id]["available"] = True
        return self.book_dict[book_id]

    def get_book_info(self, book_id: int) -> dict:
        """
        Retrieve information about a specific book.

        Args:
            book_id (int): ID of the book to retrieve.

        Returns:
            dict: Information about the specified book.

        Raises:
            ValueError: If the book ID is invalid.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        book_info = self.book_dict[book_id]
        book_info['book_id'] = book_id
        return book_info

    def filter_books_by_availability(self, available: bool) -> list:
        """
        Filter books by their availability status.

        Args:
            available (bool): True for available books, False for borrowed books.

        Returns:
            list: A list of books matching the specified availability status.
        """
        book_info_list = []
        for book_id, book_info in self.book_dict.items():
            if book_info["available"] == available:
                book_info_with_id = book_info.copy()
                book_info_with_id["book_id"] = book_id
                book_info_list.append(book_info_with_id)
        return book_info_list

    def update_book_info(self, book_id: int, title: str = None, author: str = None, isbn: str = None) -> dict:
        """
        Update information about a specific book.

        Args:
            book_id (int): ID of the book to update.
            title (str, optional): New title for the book.
            author (str, optional): New author for the book.
            isbn (str, optional): New ISBN for the book.

        Returns:
            dict: Updated information about the book.

        Raises:
            ValueError: If the book ID is invalid.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        if title is not None:
            self.book_dict[book_id]["title"] = title
        if author is not None:
            self.book_dict[book_id]["author"] = author
        if isbn is not None:
            self.book_dict[book_id]["isbn"] = isbn

        book_info = self.book_dict[book_id]
        book_info['book_id'] = book_id
        return book_info

    def remove_book(self, book_id: int) -> None:
        """
        Remove a book from the library.

        Args:
            book_id (int): ID of the book to remove.

        Raises:
            ValueError: If the book ID is invalid or the book is currently borrowed.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        if not self.book_dict[book_id]["available"]:
            raise ValueError("Book is already borrowed")

        del self.book_dict[book_id]


class CarLine:
    """
    A class representing a queue of cars waiting for service.

    Attributes:
        car (list): A list storing car registration numbers.
    """

    def __init__(self):
        """
        Initialize the CarLine with an empty queue.
        """
        self.car = []

    def add_car(self, reg_num: str) -> None:
        """
        Add a car to the end of the queue.

        Args:
            reg_num (str): The registration number of the car.

        Raises:
            ValueError: If the registration number is not a string.
        """
        if type(reg_num) is not str:
            raise ValueError("Invalid car registration number")

        self.car.append(reg_num)

    def service(self) -> str:
        """
        Service the car at the front of the queue.

        Returns:
            str: The registration number of the car being serviced.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("The CarLine is empty. No cars available for service")
        return self.car.pop(0)

    def count_cars(self) -> int:
        """
        Count the total number of cars in the queue.

        Returns:
            int: The number of cars in the queue.
        """
        return len(self.car)

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.car) == 0

    def __str__(self) -> str:
        """
        Get a string representation of the cars in the queue.

        Returns:
            str: A string of car registration numbers separated by arrows.
        """
        if self.is_empty():
            return ""

        result = ""
        for car in self.car:
            result += f"{car} -> "

        return result[:-4]


class RecentHistory:
    """
    A class representing a history of recently accessed items.

    Attributes:
        items (list): A list storing the history of items.
    """

    def __init__(self):
        """
        Initialize the RecentHistory with an empty list of items.
        """
        self.items = []

    def add(self, item: str) -> None:
        """
        Add a new item to the history.

        Args:
            item (str): The item to add.

        Raises:
            ValueError: If the item is not a string.
        """
        if type(item) is not str:
            raise ValueError("Invalid item type")
        self.items.append(item)

    def remove(self) -> str:
        """
        Remove the most recent item from the history.

        Returns:
            str: The removed item.

        Raises:
            ValueError: If the history is empty.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No more remove operations can be performed")
        return self.items.pop()

    def oldest(self) -> str:
        """
        Get the oldest item in the history.

        Returns:
            str: The oldest item.

        Raises:
            ValueError: If the history is empty.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No oldest item available")
        return self.items[0]

    def newest(self) -> str:
        """
        Get the most recent item in the history.

        Returns:
            str: The most recent item.

        Raises:
            ValueError: If the history is empty.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No newest item available")
        return self.items[-1]

    def count_items(self) -> int:
        """
        Count the total number of items in the history.

        Returns:
            int: The number of items in the history.
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """
        Check if the history is empty.

        Returns:
            bool: True if the history is empty, False otherwise.
        """
        return len(self.items) == 0

    def __str__(self) -> str:
        """
        Get a string representation of the items in the history.

        Returns:
            str: A string of items separated by arrows.
        """
        if self.is_empty():
            return ""

        result = ""
        for item in reversed(self.items):
            result += f"{item} -> "

        return result[:-4]
