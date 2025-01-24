class Library:
    def __init__(self):
        """
        Initialize Library.
        """
        self.book_dict = {}

    def add_book(self, book_id: int, title: str, author: str, isbn: str) -> None:
        """
        Adds a book to the library.
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
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")
        
        if self.book_dict[book_id]["available"] == False:
            raise ValueError("Book is already borrowed")
        
        self.book_dict[book_id]["available"] = False
        book_info = self.book_dict[book_id]
        book_info['book_id'] = book_id
        return book_info   

    def return_book(self, book_id: int) -> dict:
        """
        Marks a book as returned (available).
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")
            
        self.book_dict[book_id]["available"] = True
        return self.book_dict[book_id]    

    def get_book_info(self, book_id: int) -> dict:
        """
        Returns the book info for a given book_id.
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")

        book_info = self.book_dict[book_id]
        book_info['book_id'] = book_id
        return book_info   

    def filter_books_by_availability(self, available: bool) -> list:
        """
        Filters and returns a list of books by their availability.
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
        Updates the book's information (title, author, or isbn).
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
        """
        if book_id not in self.book_dict:
            raise ValueError("Invalid book ID")
            
        if self.book_dict[book_id]["available"] == False:
            raise ValueError("Book is already borrowed")
            
        del self.book_dict[book_id]


class CarLine:
    def __init__(self):
        """
        Initialize the CarLine.
        """
        self.car = [] 

    def add_car(self, reg_num: str) -> None:
        """
        Adds a new car to the end of the car line.
        """
        if type(reg_num) is not str:  
            raise ValueError("Invalid car registration number")
            
        self.car.append(reg_num)

    def service(self) -> str:
        """
        Services (removes) the car at the front of the car line.
        """
        if self.is_empty():
            raise ValueError("The CarLine is empty. No cars available for service")
        return self.car.pop(0)  

    def count_cars(self) -> int:
        """
        Returns the total number of cars currently in the car line.
        """
        return len(self.car) 

    def is_empty(self) -> bool:
        """
        Checks if the car line is empty.
        """
        return len(self.car) == 0  

    def __str__(self) -> str:
        """
        Returns a string representation of the cars in the line.
        """
        if self.is_empty():
            return ""
        
        result = ""
        for car in self.car:
            result += f"{car} -> "
            
        return result[:-4] 
    


class RecentHistory:
    def __init__(self):
        """
        Initialize the RecentHistory with an empty list of items.
        """
        self.items = []  

    def add(self, item: str) -> None:
        """
        Add a new item (file path) to the top of the history.
        """
        if type(item) is not str:
            raise ValueError("Invalid item type")
        self.items.append(item)  

    def remove(self) -> str:
        """
        Remove the most recent item from the history and return it.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No more remove operations can be performed")
        return self.items.pop()  

    def oldest(self) -> str:
        """
        Return the oldest item in the history without removing it.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No oldest item available")
        return self.items[0]  

    def newest(self) -> str:
        """
        Return the most recent item in the history without removing it.
        """
        if self.is_empty():
            raise ValueError("The RecentHistory is empty. No newest item available")
        return self.items[-1]  

    def count_items(self) -> int:
        """
        Return the total number of items in the history.
        """
        return len(self.items) 

    def is_empty(self) -> bool:
        """
        Check if the history is empty.
        """
        return len(self.items) == 0 

    def __str__(self) -> str:
        """
        Return a string representation of the items in the history, separated by arrows.
        """
        if self.is_empty():
            return ""
        
        result = ""
        for item in reversed(self.items):
            result += f"{item} -> "

        return result[:-4]
