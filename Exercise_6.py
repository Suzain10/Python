class Library:
  def __init__(self):
    self.TotalBooks = 0
    self.books = []
  def addBook(self,book):
    self.books.append(book)
    self.BooksLen = len(self.books)
  def ShowInfo(self):
    print(f"The library has {self.BooksLen} books which are as follows: ")
    for book in self.books:
      print(book)

L =Library()
L.addBook("The Kite Runner")
L.addBook("The Fault in Our Stars ")
L.addBook("Sparks of Phoenix")
L.addBook("The Mountain is You")
L.ShowInfo()

