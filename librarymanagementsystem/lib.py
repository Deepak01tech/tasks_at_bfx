class Book:
    def __init__(self ):
        # self.bookid = bookid
        # self.title=title
        # self.author=author
        # self.quantity=quantity
        self.issue_books=[]
        self.person_info=[]
        self.books=[]

    def add_book(self, book):
        self.books.append(book)
    
    def addnewbook(self):
        book_id=int(input("enter book id : "))
        
        for book in self.books:
            if book[0]==book_id:
                print("Book with the same id already exists")
                return
        bookname =input("enter the book name : ")
        author= input("enter the author name: ")
        quantity=int(input("enter the quantity of books: "))

        new_book=[book_id,bookname,author,quantity]
        self.add_book(new_book)
        print("book added successfully ")
        

        # with open("book_record","a") as file:
            # file.write(new_book)
        with open("book_record.txt","a") as file:
            file.write(f"{book_id},{bookname},{author},{quantity}\n")

        return new_book
    
    def issue_book(self):
        name=input("enter the name of issuer : ")
        id = input ("enter the id : ")
        book_name=input("enter the book name to be issued : ")
        

        for book in self.books:
            if book[1]==book_name:
                if book[3]>0:
                    book[3]-=1
                    self.issue_books.append(book_name)
                    self.person_info.append([name,id])
                    print(f"'{book_name}' has been issued to {name}")
                    return
                else:
                    print(f"'{book_name}' is not available for issuing")
                    return

    def view_all_books(self):
        if self.books:
            print("books in the library : ")

            for book in self.books:
               
                print(f"Id :{book[0]},Title :{book[1]},Author :{book[2]},quantity :{book[3]}")

        else:
            print("no books available in the library")

    
    def returnbook(self,book):
        if book in self.issue_books:
            self.issue_books.remove(book)
            print(f"'{book}' has been returned successfully")
        else:
            print(f"'{book}' was not issued from this library")
     
    
def main():
    books=Book()
    
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
            books.addnewbook()
        elif option=='2':

            books.issue_book()
            
        elif option=='3':
            
            book_name=input("enter the book name to be returned : ")
            
            for book in books.books:
                if book[1]==book_name:
                    book[3]+=1
                    print(f"'{book_name}' has been returned successfully")
                    break

            
        elif option == '4':
            
            book_name=input("enter the book name to check availability : ")
            for book in books.books:
                if book[1]==book_name:
                    if book[3]>0:
                        print(f"'{book_name}' is available")
                    else:
                        print(f"'{book_name}' is not available")
                    break
            else:
                print(f"'{book_name}' does not exist in the library")
            
            
        elif option == '5':
            
            books.view_all_books()

        elif option == '6':
            print("goodbye")
            break
        else:
            print('invalid choice,please try again')

if __name__=="__main__":
    main()








    
