class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a human-readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation of the Book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor called when a Book instance is deleted."""
        print(f"Deleting {self.title}")
