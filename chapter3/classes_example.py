# Management system for Library with boooks.


class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn: str) -> None:
        """Remove a book from the library by ISBN

        Args:
            isbn (str): isbn is a unique identifier for a book
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN: {isbn} removed successfully")
                return
        print(f"Book with ISBN: {isbn} was not found")

    def display_books(self) -> None:
        for book in self.books:
            print(book)

    def search_book(self, title: str) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"The book was found: {book}")
                return
        print(f"Book with title: {title} was not found")


if __name__ == "__main__":
    # WE create books, then we create a library and add the books to the library.
    python_book = Book("Python Programming", "John Doe", "123456")
    java_book = Book("Java Programming", "Jane Doe", "654321")
    c_book = Book("C Programming", "Alice", "987654")

    library = Library("My Library")

    library.add_book(python_book)
    library.add_book(java_book)
    library.add_book(c_book)

    library.display_books()

    library.remove_book("987654")

    print("--------------------------------------")

    library.display_books()

    library.search_book("java programming")
