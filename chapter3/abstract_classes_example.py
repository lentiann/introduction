# Abstract classes and methods.

from abc import ABC, abstractmethod


class Publication(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class Book(Publication):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")


class EBook(Publication):
    def __init__(self, title, author, isbn, format_):
        super().__init__(title, author)
        self.format_ = format_
        self.isbn = isbn

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Format: {self.format_}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN: {isbn} removed successfully")
                return
        print(f"Book with ISBN: {isbn} was not found")

    def display_books(self):
        for book in self.books:
            print(book.display())

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"The book was found: {book}")
                return
        print(f"Book with title: {title} was not found")


if __name__ == "__main__":
    # WE create books, then we create a library and add the books to the library.
    python_book = Book("Python Programming", "John Doe", "123456")
    java_book = Book("Java Programming", "Jane Doe", "654321")

    c_ebook = EBook("C Programming", "Alice", "12345", "PDF")
    csharp_ebook = EBook("C# Programming", "John Doe", "54321", "PDF")

    library = Library("My Library")

    library.add_book(python_book)
    library.add_book(java_book)
    library.add_book(c_ebook)
    library.add_book(csharp_ebook)

    library.display_books()

    library.remove_book("123456")

    print("--------------------------------------")

    library.display_books()
