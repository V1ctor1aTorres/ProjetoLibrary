class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f'{self.name}, We have the following books in our library.')
        sno = 1
        for book in self.bookList:
            print(f"{sno} {book}")
            sno += 1

    def lendBook(self, book, name):
        if book in self.bookList:
            if book not in self.lenDict:
                self.lenDict.update({book: name})
                print("Lender-Book database has been update.\nYou can take the book now")
            else:
                print(f'Book is already being used by {self.lenDict[book]}')
        else:
            print("This book is not relate to our database")

    def addBook(self, book):
        self.bookList.append(book)
        print(f'Book has been added to the book list.')
    
    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lenDict.keys():
                self.lenDict.pop(book)
            else:
                print("This book {book} is not in use.")
        else:
            print("This book is not relate to our database")
