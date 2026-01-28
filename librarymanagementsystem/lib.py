class Book:
    def __init__(self,bookid,title, author, quantity ):
        self.bookid = bookid
        self.title=title
        self.author=author
        self.quantity=quantity
        self.issue_books=[]
        self.person_info=[]
        self.books=[]


    def display_books_info(self):
        print(f"Id :{self.bookid},Title :{self.title},Author :{self.author},quantity :{self.quantity}") 

    def check_book_availability(self):
        return self.quantity > 0
    
        
    
    def addnewbook(self):
        book_id=int(input("enter book id : "))
        if any(book.book_id == book_id for book in self.books):
            print("Book with the same id already exists")
            return
        bookname =input("enter the book name : ")
        author= input("enter the author name: ")
        quantity=int(input("enter the quantity of books: "))

        new_book=Book(book_id,bookname,author,quantity)
        self.add_book(new_book)
        print("book added successfully ")
        new_book.display_books_info()

        with open("book_record","a") as file:
            file.write(new_book)
        return new_book
    
    def issue_book(self):
        name=input("enter the name : ")
        id = input ("enter the id : ")
        book_name=input("enter the book name to be issued : ")
        if book_name.check_book_availability():
            self.issue_books.append(book_name)
            self.person_info.append([name,id])

    def view_all_books(self):
        if self.books:
            print("books in the library : ")
            for book in self.books:
                book.self.display_book_info()

        else:
            print("no books available in the library")

    
    
    def returnbook(self,book):
        if book in self.issue_books:
            self.issue_books.remove(book)
            print(f"{self.person_info} has returned '{self.title}")
        # self.pname=pname
        # self.pid=pid
        # self.bookname=bookname
        # self.bookid=bookid

    
    
    
def main():
    books=Book()
    book1 = books(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 5)
    book2 = books(2, "The Hobbit", "J.R.R. Tolkien", 3)
    book3 = books(3, "1984", "George Orwell", 2)

    books.addnewbook(book1)
    books.addnewbook(book2)
    books.addnewbook(book3)

    while True:
        print("\nWelcome to the Library Management System")
        print("1. add new books")
        print("2. issue books")
        print("3. return book")
        print("4. check book availability")
        print("5. view all books")

        print("6. Exit")

        option= input("enter the choice from above options: ")

        if option == '1':
            Book.addnewbook()
        elif option=='2':
            Book.issue_book()


            
        elif option=='3':
            Book.returnbook()

            
        elif option == '4':
            Book.check_book_availability()
            
        elif option == '5':
            Book.view_all_books()
        elif option == '6':
            print("goodbye")
            break
        else:
            print('invalid choice,please try again')

if __name__=="__main__":
    main()








    
