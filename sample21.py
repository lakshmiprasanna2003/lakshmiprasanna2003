class Book:
    def _init_(self, title, author, publisher, price, author_royalty):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = author_royalty
    def title(self):
        return self._title
    def title(self, title):
        self._title = title
    def author(self):
        return self._author
    def author(self, author):
        self._author = author
    def publisher(self):
        return self._publisher
    def publisher(self, publisher):
        self._publisher = publisher
    def price(self):
        return self._price
    def price(self, price):
        self._price = price
    def author_royalty(self):
        return self._author_royalty
    def author_royalty(self, author_royalty):
        self._author_royalty = author_royalty
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            return (0.10 * self._price * 500) + (0.125 * self._price * (copies_sold - 500))
        else:
            return (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (copies_sold - 1500))
class Ebook(Book):
    def _init_(self, title, author, publisher, price, author_royalty, ebook_format):
        super()._init_(title, author, publisher, price, author_royalty)
        self._ebook_format = ebook_format
    def ebook_format(self):
        return self._ebook_format
    def ebook_format(self, ebook_format):
        self._ebook_format = ebook_format
    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst_deduction = base_royalty * 0.12
        return base_royalty - gst_deduction
book = Book("Sample Book", "John Doe", "Sample Publisher", 20.0, 0.10)
ebook = Ebook("Sample Ebook", "John Doe", "Sample Publisher", 15.0, 0.10, "EPUB")
print("Book Royalty for 2000 copies:", book.royalty(2000))
print("Ebook Royalty for 2000 copies:", ebook.royalty(2000))
