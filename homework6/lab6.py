class Library:
    """
    A class representing a library system for managing books.

    Attributes:
        book_dict (dict): A dictionary holding book information with book IDs as keys.
    """

    def __init__(self):
        """
        Initialize the Library with an empty book dictionary.
        """
        self.book_dict = {}

    def add_book(self, book_id: int, title: str, author: str, isbn: str) -> None:
        """
        Adds a new book to the library.

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
        Marks a book as borrowed if it is available.

        Args:
            book_id (int): ID of the book to be borrowed.

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
        Marks a book as returned (available).

        Args:
            book_id (int): ID of the book to be returned.

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
        Retrieves the information for a specific book.

        Args:
            book_id (int): ID of the book to retrieve.

        Returns:
            dict: Information about the requested book.

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
        Filters books by their availability.

        Args:
            available (bool): True for available books, False for borrowed books.

        Returns:
            list: List of books matching the availability status.
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
        Updates the information of a book.

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
        Removes a book from the library.

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
