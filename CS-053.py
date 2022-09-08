class RaikenLibrary:

    def sort_Func(self):
        with open("booksrec.txt", "a+") as f:
            f.seek(0)
            file_data = f.readlines()
            books = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                books.append(data)
        LENGTH_OF_BOOK_LIST = len(books)
        for i in range(LENGTH_OF_BOOK_LIST - 1):
            for j in range(LENGTH_OF_BOOK_LIST - i - 1):
                if books[j] > books[j + 1]:
                    books[j], books[j + 1] = books[j + 1], books[j]
        return books


    def add_Func(self):
        with open("booksrec.txt", "a+") as f:
            f.seek(0)
            file_data = f.readlines()
            books = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                books.append(data)
            f.close()

        print("""The Raiken Library has the following books: """)
        for data in books:
            print("Name Of The Book: ")
            print(f" " * 20 + f"{data[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{data[1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{data[2]}")
            print("_"*50)
        print()
        print("Enter The Following Details To Add A Book To The Raiken Library")
        BOOKNAME = input("The Book's Name: ")
        AUTHOR = input("The Author Of The Book: ")
        TOTALBOOKS = int(input("The Number Of Books: "))

        with open("booksrec.txt.txt", "a") as f:
            string = BOOKNAME + "-" + AUTHOR + "-" + str(TOTALBOOKS)
            f.write("\n")
            f.write(string)

        print("The book has been added to the raiken library successfully")


    def edit_Func(self):
        with open("booksrec.txt", "a+") as f:
            f.seek(0)
            file_data = f.readlines()
            books = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                books.append(data)
        print("""The Raiken Library has the following books: """)
        for data in range(len(books)):
            print("Book Number: ", data + 1)
            print(f" " * 20 + f"{books[data][0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{books[data][1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{books[data][2]}")
            print("_" * 50)
        print()
        print("Enter the following details To Edit Your Books")
        BOOKNUMBER = int(input("Enter The Number Of The Book: "))
        BOOKNUMBER = BOOKNUMBER - 1
        EDIT = books[BOOKNUMBER]
        books.remove(EDIT)
        while True:
            print("""Please Choose The Options Below From Which You'd Like To Change Details:
                     1.) Name Of The Book
                     2.) Author Of The Book
                     3.) Quantity Of The Books
                     4.) Exit""")
            opt = int(input("What is your choice? : "))
            if opt == 1:
                print("Please Enter")
                book_name = input("The New Name: ")
                EDIT[0] = book_name
            if opt == 2:
                print("Please Enter")
                author_name = input("The New Author: ")
                EDIT[1] = author_name
            if opt == 3:
                print("Please Enter")
                quantity = input("The New Quantity: ")
                EDIT[2] = quantity
            if opt == 4:
                break
        books.append(EDIT)
        with open("booksrec.txt", "w+") as f:
            for data in books:
                if data != books[-1]:
                    string = data[0] + "-" + data[1] + "-" + data[2]
                    f.write(string + "\n")
                else:
                    string = data[0] + "-" + data[1] + "-" + data[2]
                    f.write(string)


    def remove_Func(self):
        with open("booksrec.txt", "a+") as f:
            f.seek(0)
            file_data = f.readlines()
            books = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                books.append(data)
            f.close()
        print("""The Raiken Library has the following books: """)
        for data in books:
            print("Name Of The Book: ")
            print(f" " * 20 + f"{data[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{data[1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{data[2]}")
            print("_" * 50)
        print()
        print('To remove a book enter the following details')
        BOOKNAME = input("The name of the book: ")
        TOTALBOOKS = int(input("The number of books to be removed: "))   # quantity must be less than total no.of existing books
        REMOVEBOOK = ""
        for data in books:
            if data[0] == BOOKNAME:
                REMOVEBOOK = data
                break
        books.remove(REMOVEBOOK)
        if int(REMOVEBOOK[2]) - TOTALBOOKS == 0:
            pass
        else:
            NEW_QTY = int(REMOVEBOOK[2]) - TOTALBOOKS
            UPDATED = [REMOVEBOOK[0], REMOVEBOOK[1], str(NEW_QTY)]
            books.append(UPDATED)
        with open("booksrec.txt", "w+") as f:
            for data in books:
                if data != books[-1]:
                    string = data[0] + "-" + data[1] + "-" + data[2]
                    f.write(string + "\n")
                else:
                    string = data[0] + "-" + data[1] + "-" + data[2]
                    f.write(string)


    def sign_upFunc(self):
        print("Sign Up Here By Entering Your Details You Want To Use: ")
        print("These details will stay safe with the Raiken Program")
        EMAIL = input("Enter Your Email Please: ")
        PASS = input("Enter Your Password Please: ")

        with open("accdata.txt", "r+") as f:
            f.seek(0)
            file_data = f.readlines()
            users = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                users.append(data)
            f.close()

        for data in users:
            if EMAIL == data[0]:
                print("This email is already in use, please use your own or try to login")
                return False
            else:
                with open("accdata.txt", "a+") as f:
                    string = EMAIL + "-" + PASS
                    f.write("\n")
                    f.write(string)
                return True


    def cancel_memberFunc(self):
        print("This is the place where you cancel your membership in the Raiken Library: ")
        print("Enter Your Details Again To Remove Yourself From The Raiken Program: ")
        EMAIL = input("Enter your email: ")
        PASS = input("Enter your password: ")

        with open("accdata.txt", "r+") as f:
            f.seek(0)
            file_data = f.readlines()
            users = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                users.append(data)
        data_to_remove = [EMAIL, PASS]

        if data_to_remove in users:
            users.remove(data_to_remove)

        with open("accdata.txt", "w+") as f:
            for data in users:
                if data != users[-1]:
                    string = data[0] + "-" + data[1]
                    f.write(string + "\n")
                else:
                    string = data[0] + "-" + data[1]
                    f.write(string)
            return


    def log_inFunc(self):
        print("Hello, Please Enter Your Details: ")
        EMAIL = input("Enter Your Email Please: ")
        PASS = input("Enter Your Password Please: ")

        with open("accdata.txt", "r+") as f:
            f.seek(0)
            file_data = f.readlines()
            users = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                users.append(data)
            f.close()

        if [EMAIL, PASS] in users:
            return [True, EMAIL, PASS]
        else:
            return [False, EMAIL, PASS]


    def show_all_booksFunc(self):
        SORTED_RESULTS = self.sort_Func()
        print()
        for item in SORTED_RESULTS:
            print(f"BOOK NAME: {item[0]}")
            print(f"AUTHOR: {item[1]}")
            print(f"TOTAL AVAILABLE: {item[2]}")
            print("*"*90)
            print()


    def search_Fun(self):
        BOOKNAME = ""
        AUTHOR = ""
        while True:
            print("""Please Choose The Field You'd Like To Search:
                     1.) Name Of The Book
                     2.) Author Of The Book
                     3.) Exit""")
            opt = int(input("What is your opt? : "))
            if opt == 1:
                print("Please Enter")
                BOOKNAME = input("The Name Of The Book You Want To Search: ")
            if opt == 2:
                print("Please Enter")
                AUTHOR = input("The Name Of The Author You Want To Search: ")
            if opt == 3:
                break

        with open("booksrec.txt", "a+") as f:
            f.seek(0)
            file_data = f.readlines()
            books = []
            for data in file_data:
                data = data.split("-")
                item = data.pop()
                Last_item = ""
                for character in item:
                    if character == "\n":
                        continue
                    else:
                        Last_item = Last_item + character
                data.append(Last_item)
                books.append(data)

            SEARCH_RESULTS = []
            for data in books:
                if data[0] == BOOKNAME:
                    SEARCH_RESULTS.append(data)
                if data[1] == AUTHOR:
                    SEARCH_RESULTS.append(data)
            return SEARCH_RESULTS


    def check_outFunc(self):
        print("This Is The Checkout Page")
        print("Please Login Before You Continue")
        temp = self.log_inFunc()

        if temp[0] == False:
            print("This User Does Not Exist.")
            return False
        else:
            with open("booksrec.txt", "a+") as f:
                f.seek(0)
                file_data = f.readlines()
                books = []
                for data in file_data:
                    data = data.split("-")
                    item = data.pop()
                    Last_item = ""
                    for character in item:
                        if character == "\n":
                            continue
                        else:
                            Last_item = Last_item + character
                    data.append(Last_item)
                    books.append(data)
                f.close()

            print("""We Currently Have The Following Books: """)
            for data in range(len(books)):
                print("Book Number: ", data + 1)
                print(f" " * 20 + f"{books[data][0]}")
                print("Author Of The Book: ")
                print(f" " * 20 + f"{books[data][1]}")
                print("Quantity Of The Book: ")
                print(f" " * 20 + f"{books[data][2]}")
                print("_" * 50)
            print()

            print("Please Enter The Following Details")
            BOOKNUMBER = int(input("The Number Of The Book You Want To Borrow: "))
            BOOKNUMBER = BOOKNUMBER - 1
            BORROW = books[BOOKNUMBER]
            books.remove(BORROW)
            NEW_QTY = int(BORROW[2]) - 1
            UPDATED = [BORROW[0], BORROW[1], str(NEW_QTY)]
            books.append(UPDATED)

            with open("booksrec.txt", "w+") as f:
                for data in books:
                    if data != books[-1]:
                        string = data[0] + "-" + data[1] + "-" + data[2]
                        f.write(string + "\n")
                    else:
                        string = data[0] + "-" + data[1] + "-" + data[2]
                        f.write(string)
            with open("info.txt", "a+") as f:
                f.write("\n")
                f.write(temp[1] + "-check_out" + "-" + UPDATED[0])


    def renew_Func(self):
        print("This Is The Renew Page.")
        print("Please Login Before You Continue")
        temp = self.log_inFunc()

        if temp[0] == False:
            print("This User Does Not Exist.")
            return False
        else:
            with open("info.txt", "a+") as f:
                f.seek(0)
                file_data = f.readlines()
                information = []
                for data in file_data:
                    data = data.split("-")
                    item = data.pop()
                    Last_item = ""
                    for character in item:
                        if character == "\n":
                            continue
                        else:
                            Last_item = Last_item + character
                    data.append(Last_item)
                    information.append(data)

            print("Please Enter")
            BOOKNAME = input("The Name Of The Book You Want To Renew: ")

            for data in information:
                if (temp[1] == data[0]) and (data[1] == "check_out") and (data[2] == BOOKNAME):
                    information.remove(data)
                    print("Your Book Has Been Returned")

                    with open("booksrec.txt", "a+") as f:
                        f.seek(0)
                        file_data = f.readlines()
                        book_lists = []
                        for data in file_data:
                            data = data.split("-")
                            item = data.pop()
                            Last_item = ""
                            for character in item:
                                if character == "\n":
                                    continue
                                else:
                                    Last_item = Last_item + character
                            data.append(Last_item)
                            book_lists.append(data)


                    with open("info.txt", "w+") as f:
                        f.write(temp[1] + "-" + "renew" + "-" + BOOKNAME)
                        f.write("\n")

                        for data in information:
                            if data != information[-1]:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string + "\n")
                            else:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string)
                                return


    def reserve_Func(self):
        print("This Is The Reserve Page.")
        print("Please Login Before You Continue")
        temp = self.log_inFunc()

        if temp[0] == False:
            print("This User Does Not Exist.")
            return False
        else:
            print("Please Enter")
            BOOKNAME = input("The Name Of The Book You Want To Reserve: ")
            with open("info.txt","a+") as f:
                f.write("\n")
                f.write(temp[1] + "-reserve" + "-" + BOOKNAME)


    def return_Func(self):
        print("This Is The Return Page.")
        print("Please Login Before You Continue")
        temp = self.log_inFunc()

        if temp[0] == False:
            print("This User Does Not Exist.")
            return False
        else:
            with open("info.txt", "a+") as f:
                f.seek(0)
                file_data = f.readlines()
                information = []
                for data in file_data:
                    data = data.split("-")
                    item = data.pop()
                    Last_item = ""
                    for character in item:
                        if character == "\n":
                            continue
                        else:
                            Last_item = Last_item + character
                    data.append(Last_item)
                    information.append(data)

            print("Please Enter")
            BOOKNAME = input("The Name Of The Book You Want To Return: ")
            for data in information:
                if (temp[1] == data[0]) and ((data[1] == "check_out") or (data[1] == "renew")) and (data[2] == BOOKNAME):
                    information.remove(data)
                    print("Your Book Has Been Returned")

                    with open("booksrec.txt", "a+") as f:
                        f.seek(0)
                        file_data = f.readlines()
                        books = []
                        for data in file_data:
                            data = data.split("-")
                            item = data.pop()
                            Last_item = ""
                            for character in item:
                                if character == "\n":
                                    continue
                                else:
                                    Last_item = Last_item + character
                            data.append(Last_item)
                            books.append(data)
                        f.close()

                    RETURN = None
                    for data in books:
                        if data[0] == BOOKNAME:
                            RETURN = data

                    NEW_QTY = int(RETURN[2]) + 1
                    UPDATED = [RETURN[0], RETURN[1], str(NEW_QTY)]
                    books.append(UPDATED)

                    with open("booksrec.txt", "w+") as f:
                        for data in books:
                            if data != books[-1]:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string + "\n")
                            else:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string)

                    with open("booksrec.txt", "w+") as f:
                        for data in information:
                            if data != information[-1]:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string + "\n")
                            else:
                                string = data[0] + "-" + data[1] + "-" + data[2]
                                f.write(string)
                                return


print("A Book A Day Keeps The Bad Thoughts Away, Not Us")
print()
print("Welcome To The Raiken Library")
obj = RaikenLibrary()
while True:
    print('''You have the following options:
             1.) Login to your Raiken Account
             2.) Create a new Raiken account
             3.) Delete your existing Raiken account
             4.) Add book in the Raiken library
             5.) Remove book from the Raiken library
             6.) Edit a book in the Raiken library
             7.) Display all the books in the Raiken library
             8.) Search a particular book in the Raiken Library
             9.) Borrow a book from the Raiken library
             10.) Renew a borrowed book from the Raiken library
             11.) Return a borrowed book to the Raiken library
             12.) Reserve a book from the Raiken library
             13.) Exit the Raiken application''')
    CHOICE_NUMBER = int(input("Select one please: "))
    if CHOICE_NUMBER == 13:
        print("Exiting the application")
        print("Thankyou for coming to Raiken Library")
        break
    if CHOICE_NUMBER == 1:
        obj.log_inFunc()
    if CHOICE_NUMBER == 2:
        obj.sign_upFunc()
    if CHOICE_NUMBER == 3:
        obj.cancel_memberFunc()
    if CHOICE_NUMBER == 4:
        obj.add_Func()
    if CHOICE_NUMBER == 5:
        obj.remove_Func()
    if CHOICE_NUMBER == 6:
        obj.edit_Func()
    if CHOICE_NUMBER == 7:
        obj.show_all_booksFunc()
    if CHOICE_NUMBER == 8:
        results = obj.search_Fun()
        for item in results:
            print(f"BOOK NAME: {item[0]}")
            print(f"AUTHOR: {item[1]}")
            print(f"TOTAL BOOKS: {item[2]}")
            print()
    if CHOICE_NUMBER == 9:
        obj.check_outFunc()
    if CHOICE_NUMBER == 10:
        obj.renew_Func()
    if CHOICE_NUMBER == 11:
        obj.return_Func()
    if CHOICE_NUMBER == 12:
        obj.reserve_Func()

