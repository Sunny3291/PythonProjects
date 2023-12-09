# Without Function: 

print("***************Welcome To Book Mangement System****************")
book={}

while True:
        print("1. Add Book""\n")
        print("2. Search Book""\n")
        print("3. Display All Books""\n")
        print("4. Delete Book""\n")
        print("5. Update Book""\n")
        print("6. Exit""\n")
    
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            title=str(input("Enter Book Title: "))
            author=str(input("Enter Author: "))
            publication=str(input("Enter Publication Year: "))
            gen=str(input("Enter Book Generation: "))
            book[title]={"Title":title,"Author":author,"Publication Year":publication,"Generation":gen}
        
            print("Book Added Successfully..!!""\n")
            
        elif choice==2:
            title=str(input("Enter Book Title: "))
            author=str(input("Enter Author: "))
            publication=str(input("Enter Publication Year: "))
            gen=str(input("Enter Book Generation: "))
            if book["Title"]==title and book["Author"]==author and book["Publication Year"]==publication and book["Generation"]==gen:
                print("Book Found..!""\n")
                break
            else:
                print("Book Not Found...🙁""\n")
        elif choice==3:
            print(book)
        
        elif choice==4:
            title=str(input("Enter Book Title: "))
            author=str(input("Enter Author: "))
            publication=str(input("Enter Publication Year: "))
            gen=str(input("Enter Book Generation: "))
            for title in book:
                del book[title]
                print("Book Deleted..!""\n")
                break
            else:
                print("Please enter correct info..🙁")
        
        elif choice==5:
            title=str(input("Enter Book Title: "))
            author=str(input("Enter Author: "))
            publication=str(input("Enter Publication Year: "))
            gen=str(input("Enter Book Generation: "))
            book["Title"]=title
            book["Author"]=author
            book["Publication Year"]=publication
            book["Generation"]=gen
            print("Book Updated Successfully..!")
            
        elif choice==6:
            print("Exiting program. Goodbye..!")
            exit()