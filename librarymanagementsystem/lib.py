class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
class Book(LibraryItem):
    def __init__(self, title, author, publication_year, bookid):
        super().__init__(title, author, publication_year)
        self.bookid = bookid

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, bookid: {self.bookid}"
    
    def addnewbook(self,):
        bookname =input("enter the book name : ")
        author= input("enter the author name: ")
        publicationyear=input("enter the publication year: ")

        new_book={
            "name":bookname,
            "author":author,
            "publication_year":publicationyear
            }
        return new_book
    




        


        

        # self.bookname = bookname
        # self.author= author
        # self.publicationyear=  publicationyear
    
    def issuebook(self,pname,pid,bookid):
        
        


    
    def returnbook(self,pname ,pid,bookname,bookid):
        self.pname=pname
        self.pid=pid
        self.bookname=bookname
        self.bookid=bookid

    def checkbookavailability(self,bookname):
        self.bookname=bookname






    
