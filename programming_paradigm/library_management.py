class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        """
        Initialize a new book.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library.
        Args:
            book (Book): An instance of the Book class to add to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' is not available in the library.")

    def return_book(self, title):
        """
        Return a book by its title.
        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
