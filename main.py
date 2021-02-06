# For connection with MySQL server
import mysql.connector

# For typing animation
import time
import sys

print()
say = " Login "
print("=" * len(say.center(100, ".")))
print(say.center(100, "."))
print("=" * len(say.center(100, ".")))
print()

# Get user credentials.
user_name = input("Enter your mysql user name: ")
mysql_passwd = input("Enter your mysql password: ")
host_name = input("Enter host: ")

# Check if user credentials is correct or not.
try:

    # Establishing connection with MySQL Database.
    my_connection = mysql.connector.connect(
        host=host_name, user=user_name, passwd=mysql_passwd
    )
    mycursor_connection = my_connection.cursor()

    # Creating initial Database
    mycursor_connection.execute(
        "CREATE DATABASE IF NOT EXISTS School_Management_System_by_KunwarYuvraj"
    )
    print()
    print('Database "School_Management_System_by_KunwarYuvraj" Created!')

    # Choosing initial Database to work.
    mydb = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=mysql_passwd,
        database="School_Management_System_by_KunwarYuvraj",
    )

    mycursor = mydb.cursor()

    def type_animation(string, sec=0.06):
        """
        Typing animation.
        -------------------
        Takes two arguments.
            1: string
            2: sec # Decrease to increase animation speed and vice-versa.
        """
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(sec)
        return ""

    ###############################
    # Creating Initial Tables     #
    ###############################
    #           START             #
    ###############################

    def create_student_table():
        """
        Creates table named 'student'.
        And inserting some initial values to work with.
        """

        mycursor.execute(
            """
            create table IF NOT EXISTS student
            (
                UID int auto_increment, 
                Roll_No int(15), 
                Name varchar(30), 
                Class varchar(10), 
                Section varchar(10), 
                Phone_No varchar(255), 
                Email varchar(300),
                Primary Key (UID)
            );
            """
        )
        mycursor.execute("alter table student auto_increment = 1000;")
        sql = """
        insert into student
        (roll_no, name, class, Section, Phone_No, Email) 
        values(%s, %s, %s, %s, %s, %s)
        """
        val = [
            (
                000,
                "Zero",
                "12",
                "A",
                "+91 1234567891",
                "zero@mail.cm",
            ),
            (1, "One", "5", "C", "+11 7878912496", "one@mail.cm"),
            (2, "Two", "3", "F", "+2 4211234567", "two@mail.cm"),
            (3, "Three", "9", "B", "+3 87450987", "three@mail.cm"),
            (4, "Four", "2", "D", "+4 1212121212", "four@mail.cm"),
            (5, "Five", "10", "E", "+5 8723412706", "five@mail.cm"),
            (6, "Six", "7", "F", "+6 8798124508", "sie@mail.cm"),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

    def create_library_table():

        """
        Creates table named 'Library'.
        And inserting some initial values to work with.
        """

        mycursor.execute(
            """
            create table IF NOT EXISTS Library
            (
                BID int auto_increment, 
                Book_Code varchar(55), 
                Book_Name varchar(230), 
                Author_Name varchar(100), 
                Subject varchar(100), 
                Issued varchar(25), 
                UID int(22),
                Return_Date Date, 
                Return_Status varchar(20),
                Primary Key (BID)
            );
            """
        )
        mycursor.execute("alter table Library auto_increment = 3000;")
        sql = """
        insert into Library
        (
            Book_Code, 
            book_name, 
            author_name, 
            Subject, 
            Issued, 
            UID, 
            Return_Date, 
            Return_Status
        ) 
        values(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = [
            (
                "B84T",
                "Python with Django",
                "Author 1",
                "Computer Science",
                "Yes",
                1000,
                "2020-10-21",
                "Yes",
            ),
            (
                "Z432",
                "Integrations III",
                "Author 2",
                "Maths",
                "No",
                None,
                None,
                None,
            ),
            (
                "234D",
                "Algebra Basics II",
                "Author 3",
                "Maths",
                "No",
                None,
                None,
                None,
            ),
            (
                "89A4",
                "SQL",
                "Author 4",
                "Computer Science",
                "Yes",
                1003,
                "2020-10-25",
                "No",
            ),
            (
                "BG89",
                "Letters",
                "Author 5",
                "English",
                "Yes",
                1005,
                "2020-10-19",
                "Yes",
            ),
            (
                "Z5T8",
                "Example Book 6",
                "Author 6",
                "Subject 6",
                "No",
                None,
                None,
                None,
            ),
            (
                "993A",
                "Example Book 7",
                "Author 7",
                "Subject 7",
                "Yes",
                1001,
                "2020-11-05",
                "No",
            ),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

    def create_cca_table():

        """
        Creates table named 'CCA'.
        And inserting some initial values to work with.
        """

        mycursor.execute(
            """
        create table IF NOT EXISTS CCA
        (
            CCA_ID int auto_increment, 
            Activity_Code varchar(215), 
            Activity_Name varchar(230), 
            Date Date, 
            Winner_UID int(55), 
            Prize varchar(300),
            Primary Key (CCA_ID)
        );
        """
        )
        mycursor.execute("alter table CCA auto_increment = 2000;")
        sql = """
        insert into CCA
        (
            Activity_Code, 
            Activity_Name,  
            Date, 
            Winner_UID, 
            Prize
        ) 
        values(%s, %s, %s, %s, %s)"""
        val = [
            ("AC23", "Example Name 1", "2020-10-12", 1000, "Rs. 2000"),
            ("AC34", "Example Name 2", "2020-11-02", None, None),
            ("4DRS", "Example Name 3", "2020-10-29", 1004, "Rs. 1000"),
            ("RD43", "Example Name 4", "2020-12-23", None, None),
            ("EM22", "Example Name 5", "2020-09-27", None, None),
            ("DD23", "Example Name 6", "2020-11-21", 1003, "Rs. 2000"),
            ("Z23R", "Example Name 7", "2020-08-05", None, None),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

    def create_fees_table():

        """
        Creates table named 'Fees'.
        And inserting some initial values to work with.
        """
        mycursor.execute(
            """
            create table IF NOT EXISTS Fees
            (
            FID int auto_increment, 
            Student_UID int(50),
            Due_Date Date, 
            Fee_Status varchar(30), 
            Submitted_Date Date, 
            Primary Key (FID)
            );
            """
        )
        mycursor.execute("alter table Fees auto_increment = 4000;")
        sql = """
        insert into Fees
        (
            Student_UID, 
            Due_Date, 
            Fee_Status,  
            Submitted_Date
        ) 
        values(%s, %s, %s, %s)"""
        val = [
            (1000, "2020-10-12", "Yes", "2020-11-01"),
            (1001, "2020-11-02", "No", None),
            (1002, "2020-10-29", "No", None),
            (1003, "2020-12-23", "Yes", "2020-12-18"),
            (1004, "2020-09-27", "Yes", "2020-10-01"),
            (1005, "2020-11-21", "No", None),
            (1006, "2020-08-05", "No", None),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

    def create_attendence_table():
        """
        Creates table named 'Attendence'.
        And inserting some initial values to work with.
        """

        mycursor.execute(
            """
            create table IF NOT EXISTS Attendence
            (
                AID int auto_increment, 
                Student_UID int(25), 
                Date date, 
                Subject varchar(200),
                Status varchar(30), 
                Time_of_Join time, 
                Time_of_Leave time, 
                Primary Key (AID)
            );
            """
        )
        mycursor.execute("alter table Attendence auto_increment = 6000;")
        sql = """
        insert into Attendence
        (
            Student_UID, 
            Date, 
            Subject,Status, 
            Time_of_Join, 
            Time_of_Leave
        ) 
        values(%s, %s, %s,%s, %s, %s)
        """
        val = [
            (1000, "2020-10-02", "Computer Science", "P", "12:30:00", "14:00:00"),
            (1001, "2020-10-02", "Maths", "A", None, None),
            (1002, "2020-10-02", "English", "P", "12:00:12", "13:00:00"),
            (1003, "2020-11-01", "Chemistry", "P", "14:00:12", "15:30:00"),
            (1004, "2020-10-02", "Maths", "A", None, None),
            (1005, "2020-10-04", "Computer Science", "A", None, None),
            (1006, "2020-11-01", "Physics", "P", "13:00:12", "15:30:00"),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()

    ###############################
    # Creating Initial Tables     #
    ###############################
    #           ENDS              #
    ###############################

    # ====================================================================#

    ###############################
    #       main Function         #
    ###############################
    #          STARTS             #
    ###############################

    def main():

        """
        Main Menu function of script.
        Calls all create table functions.
        No parameters.
        """

        create_attendence_table()
        create_student_table()
        create_library_table()
        create_cca_table()
        create_fees_table()
        print("Initial tables created !")
        print()

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            print("=" * len(heading.center(100, "-")))
            print("+ " * len(heading.center(50, "-")))
            print(heading.center(100, "-"))
            print("+ " * len(heading.center(50, "-")))
            print("=" * len(heading.center(100, "-")))
            print()

            credit = "<< Made by Kunwar Yuvraj >>"
            credit_wrapper = credit.center(100, "*")
            type_animation(credit_wrapper, 0.02)
            print("\n")

            print()
            print("1: Students")
            print("2: Attendence")
            print("3: Fees")
            print("4: Library")
            print("5: CCA")
            type_animation("6: About (Animation Based!)\n")
            print("7: Exit")

            print()
            choice = input(type_animation("Enter your choice: "))
            print()

            if choice == "1":
                student_menu()

            elif choice == "2":
                attendence_menu()

            elif choice == "3":
                fees_menu()

            elif choice == "4":
                library_menu()

            elif choice == "5":
                cca_menu()

            elif choice == "6":
                about()

            elif choice == "7":
                confirm = input("Do you really want to exit? (Y/N): ")

                if (
                    confirm in "Yy"
                    or confirm == "YES"
                    or confirm == "yes"
                    or confirm == "Yes"
                ):

                    print("Closing database..")
                    print("Bye !")
                    mydb.close()
                    break

                elif (
                    confirm in "Nn"
                    or confirm == "NO"
                    or confirm == "No"
                    or confirm == "no"
                ):

                    print("You can continue")

                else:
                    print("Invalid Choice")

    ###############################
    #       main Function         #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       Menu Functions        #
    ###############################
    #          STARTS             #
    ###############################

    def student_menu():

        """
        Student menu function.
        Calls student sub functions accordingly.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "<Student>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Add student")
            print("2: Search Student")
            print("3: Update Student")
            print("4: Show Students")
            print("5: Remove Student")
            print("6: Return")
            print()
            choice = input(type_animation("Enter your choice: "))
            print()

            if choice == "1":
                student_menu_add()
            elif choice == "2":
                student_menu_search()
            elif choice == "3":
                student_menu_update()
            elif choice == "4":
                student_menu_show()
            elif choice == "5":
                student_menu_remove()
            elif choice == "6":
                break
            else:
                print("Invalid Choice")

    def attendence_menu():

        """
        Attendence menu function.
        Calls Attendence sub functions accordingly.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "<Attendence>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Add attendence")
            print("2: Search student's attendence")
            print("3: Update attendence information")
            print("4: Show all attendence")
            print("5: Delete an attendence")
            print("6: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                attendence_menu_add()
            elif choice == 2:
                attendence_menu_search()
            elif choice == 3:
                attendence_menu_update()
            elif choice == 4:
                attendence_menu_show()
            elif choice == 5:
                attendence_menu_delete()
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

    def fees_menu():

        """
        Fees menu function.
        Calls Fees sub functions accordingly.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "<Fees>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Add fees details")
            print("2: Search student fees")
            print("3: Update student fees")
            print("4: Show all fees status")
            print("5: Remove Fees Details")
            print("6: Return")

            print()
            choice = int(input(type_animation("Enter your choice: \n")))
            print()

            if choice == 1:
                fees_menu_add()
            elif choice == 2:
                fees_menu_search()
            elif choice == 3:
                fees_menu_update()
            elif choice == 4:
                fees_menu_show()
            elif choice == 5:
                fees_menu_delete()
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

    def library_menu():

        """
        Library menu function.
        Calls Library sub functions accordingly.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "<Library>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Add Book")
            print("2: Search Book")
            print("3: Update Book Details")
            print("4: Show all Books")
            print("5: Remove Book")
            print("6: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                library_menu_add()
            elif choice == 2:
                library_menu_search()
            elif choice == 3:
                library_menu_update()
            elif choice == 4:
                library_menu_show()
            elif choice == 5:
                library_menu_delete()
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

    def cca_menu():

        """
        CCA menu function.
        Calls CCA sub functions accordingly.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "<CCA>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Add Record")
            print("2: Search Record")
            print("3: Update Record")
            print("4: Show CCA Records")
            print("5: Remove student Record")
            print("6: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                cca_menu_add()
            elif choice == 2:
                cca_menu_search()
            elif choice == 3:
                cca_menu_update()
            elif choice == 4:
                cca_menu_show()
            elif choice == 5:
                cca_menu_delete()
            elif choice == 6:
                break
            else:
                print("Invalid Choice")

    def about():
        """
        About Section.
        It is animation based.
        You can choose typing animation speed.
        No parameters.
        """
        print()
        print("Choose animation speed")
        type_animation("1: Fast\n", 0.02)
        type_animation("2: Medium\n", 0.1)
        type_animation("3: Slow (Not Recommended)\n", 0.12)
        print()
        ask_speed = int(input("Enter your choice: "))
        if ask_speed == 1:
            animation_speed = 0.015
        elif ask_speed == 2:
            animation_speed = 0.05
        elif ask_speed == 3:
            animation_speed = 0.1
        else:
            animation_speed = 0.1

        message = """
Hi, I am Kunwar Yuvraj.
School: Kendriya Vidyalaya No. 2, Dehli Cantt, Dehli 110010
Shift: 2nd Shift
Class: XII-A

This project is for class 12.
I am NOT using any extra library for this animation.
See source code for more information.
Only "Non-Standard" library used is "mysql-connector".
This project is also available 
on github at "https://github.com/KUNWAR-YUVRAJ/python_mysql_project".

"""
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(animation_speed)

    ###############################
    #       Menu Functions        #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       SUB Functions         #
    ###############################
    #          STARTS             #
    ###############################

    ###############################
    #       Student Sub Functions #
    ###############################
    #          STARTS             #
    ###############################

    def student_menu_add():
        """
        Inserts students in student table.
        No parameters.
        """
        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Student"
        sub2 = "<Add>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        cls = input("Enter Class: ")
        section = input("Enter section: ")
        phone_no = input("Enter phone number: ")
        email = input("Enter Email: ")

        query = f"""
        insert into student
        (roll_no, name, class, section, phone_no, email) 
        values({roll_no},'{name}', '{cls}', '{section}', '{phone_no}', '{email}')
        """

        mycursor.execute(query)
        mydb.commit()
        sql = f"""
        select * from student 
        WHERE 
        name='{name}' and class='{cls}' and 
        section='{section}' and phone_no='{phone_no}' and roll_no={roll_no}
        """
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            print()
            print("Student Added with Details!")
            print()
            print("UID:", row[0])
            print("Roll Number:", row[1])
            print("Name:", row[2])
            print("Class:", row[3])
            print("Section:", row[4])
            print("Phone Number:", row[5])
            print("Email:", row[6])
            print()

    def student_menu_search():
        """
        Search students by their column names.
        And return appropriate row(s).
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Student"
            sub2 = "<Search>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Search with UID")
            print("2: Search with Roll Number")
            print("3: Search with Name")
            print("4: Search with Class")
            print("5: Search with Section")
            print("6: Search with Phone Number")
            print("7: Search with Email")
            print("8: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                ask_uid = input("Enter UID: ")
                sql = """SELECT * FROM student WHERE UID=(%s)"""
                val = (ask_uid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID", row[0])
                        print("Roll Number", row[1])
                        print("Name", row[2])
                        print("Class", row[3])
                        print("Section", row[4])
                        print("Phone Number", row[5])
                        print("Email", row[6])
                        print()
                else:
                    print("Any student with uid", ask_uid, "not found!")

            elif choice == 2:
                ask_rno = input("Enter Roll Number: ")
                sql = """SELECT * FROM student WHERE Roll_No=(%s)"""
                val = (ask_rno,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID", row[0])
                        print("Roll Number", row[1])
                        print("Name", row[2])
                        print("Class", row[3])
                        print("Section", row[4])
                        print("Phone Number", row[5])
                        print("Email", row[6])
                        print()
                else:
                    print("Any student with roll number", ask_rno, "not found!")

            elif choice == 3:
                ask_name = input("Enter Name: ")
                sql = """SELECT * FROM student WHERE Name=(%s)"""
                val = (ask_name,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID", row[0])
                        print("Roll Number", row[1])
                        print("Name", row[2])
                        print("Class", row[3])
                        print("Section", row[4])
                        print("Phone Number", row[5])
                        print("Email", row[6])
                        print()
                else:
                    print("Any student with name", ask_name, "not found!")

            elif choice == 4:
                ask_class = input("Enter Class: ")
                sql = """SELECT * FROM student WHERE Class=(%s)"""
                val = (ask_class,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID", row[0])
                        print("Roll Number", row[1])
                        print("Name", row[2])
                        print("Class", row[3])
                        print("Section", row[4])
                        print("Phone Number", row[5])
                        print("Email", row[6])
                        print()
                else:
                    print("Any student with class", ask_class, "not found!")

            elif choice == 5:
                ask_section = input("Enter Section: ")
                sql = """SELECT * FROM student WHERE Section=(%s)"""
                val = (ask_section,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID", row[0])
                        print("Roll Number", row[1])
                        print("Name", row[2])
                        print("Class", row[3])
                        print("Section", row[4])
                        print("Phone Number", row[5])
                        print("Email", row[6])
                        print()
                else:
                    print("Any student with section", ask_section, "not found!")

            elif choice == 6:
                ask_pno = input("Enter Phone Number: ")
                sql = """SELECT * FROM student WHERE Phone_No=(%s)"""
                val = (ask_pno,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID:", row[0])
                        print("Roll Number:", row[1])
                        print("Name:", row[2])
                        print("Class:", row[3])
                        print("Section:", row[4])
                        print("Phone Number:", row[5])
                        print("Email:", row[6])
                        print()
                else:
                    print("Any student with phone number", ask_pno, "not found!")

            elif choice == 7:
                ask_email = input("Enter Email: ")
                sql = """SELECT * FROM student WHERE Email=(%s)"""
                val = (ask_email,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("UID:", row[0])
                        print("Roll Number:", row[1])
                        print("Name:", row[2])
                        print("Class:", row[3])
                        print("Section:", row[4])
                        print("Phone Number:", row[5])
                        print("Email:", row[6])
                        print()
                else:
                    print("Any student with email", ask_email, "not found!")

            elif choice == 8:
                break

            else:
                print("Invalid Choice")

    def student_menu_show():
        """
        Show all students.
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Student"
            sub2 = "<Show>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Show all in Tabular Form")
            print("2: Show all in Simple Form")
            print("3: Count Student from Class")
            print("4: Count Student from Section")
            print("5: Return")
            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                mycursor.execute("SELECT * FROM student")
                rec = mycursor.fetchall()
                print("-" * 100)
                print(
                    f'{"UID":<5} | {"Roll_No":<8} | {"Name":<15} | {"Class":<8} | {"Section":<9} | {"Phone_No":<18} | {"Email"}'
                )
                print("=" * 100)
                for row in rec:
                    print(
                        f"{row[0]:<5} | {row[1]:<8} | {row[2]:<15} | {row[3]:<8} | {row[4]:<9} | {row[5]:<18} | {row[6]}"
                    )
                print("-" * 100)
                print()

            elif choice == 2:
                mycursor.execute("SELECT * FROM student")
                rec = mycursor.fetchall()
                print("Total rows are: ", len(rec))
                print("Printing each row")
                print()
                for row in rec:
                    print("UID:", row[0])
                    print("Roll Number:", row[1])
                    print("Name:", row[2])
                    print("Class:", row[3])
                    print("Section:", row[4])
                    print("Phone Number:", row[5])
                    print("Email:", row[6])
                    print()

            elif choice == 3:
                mycursor.execute("select Class, Count(*) from student group by class")
                rec = mycursor.fetchall()
                print("Class", "\tNumber_of_students")
                for row in rec:
                    print(row[0], "\t", row[1])

                print()

            elif choice == 4:
                mycursor.execute(
                    "select Section, Count(*) from student group by section"
                )
                rec = mycursor.fetchall()
                print("Section", "Number_of_students")
                for row in rec:
                    print(row[0], "\t", row[1])

            elif choice == 5:
                print()
                break

            else:
                print()
                print("Invalid Choice")

    def student_menu_update():
        """
        Update students information.
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Student"
            sub2 = "<Update>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Update Roll Number")
            print("2: Update Name")
            print("3: Update Class")
            print("4: Update Section")
            print("5: Update Phone Number")
            print("6: Update Email")
            print("7: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()
            exists = False
            if choice >= 1 and choice <= 6:
                uid = int(input("Enter UID of Student: "))

            if choice == 1:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_rno = input("Enter new Roll Number: ")
                        query = "update student set roll_no= (%s) where uid= (%s)"
                        value = (new_rno, uid)
                        mycursor.execute(query, value)
                        print("Roll Number Updated!")
                        mydb.commit()

            elif choice == 2:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_name = input("Enter new Name: ")
                        query = "update student set name = (%s) where uid= (%s)"
                        value = (new_name, uid)
                        mycursor.execute(query, value)
                        print("Name Updated!")
                        mydb.commit()

            elif choice == 3:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_class = input("Enter new Class: ")
                        query = "update student set class= (%s) where uid= (%s)"
                        value = (new_class, uid)
                        mycursor.execute(query, value)
                        print("Class Updated!")
                        mydb.commit()

            elif choice == 4:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_section = input("Enter new Section: ")
                        query = "update student set section= (%s) where uid= (%s)"
                        value = (new_section, uid)
                        mycursor.execute(query, value)
                        print("Section Updated!")
                        mydb.commit()

            elif choice == 5:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_pno = input("Enter new Phone Number: ")
                        query = "update student set phone_no= (%s) where uid= (%s)"
                        value = (new_pno, uid)
                        mycursor.execute(query, value)
                        print("Section Updated!")
                        mydb.commit()

            elif choice == 6:
                mycursor.execute("select * from student")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == uid:
                        exists = True
                        new_pno = input("Enter new Email: ")
                        query = "update student set email= (%s) where uid= (%s)"
                        value = (new_pno, uid)
                        mycursor.execute(query, value)
                        print("Email Updated!")
                        mydb.commit()

            elif choice == 7:
                break

            else:
                print("Invalid Choice")

            if not exists and choice >= 1 and choice <= 6:
                print("Invalid Details")

    def student_menu_remove():
        """
        Remove student.
        NOTE: This process is irreversible.
        No parameters.
        """
        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Student"
        sub2 = "<Remove>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        ask_uid = int(
            input(type_animation("Enter UID of Student you want to remove: "))
        )
        sql = "select * from student where uid = (%s)"
        val = (ask_uid,)
        mycursor.execute(sql, val)
        rec = mycursor.fetchall()

        if len(rec) <= 0:
            print("Wrong UID")

        else:
            confirm_name = input("Confirm by entering Student's name: ")
            for row in rec:
                if confirm_name == row[2]:
                    query = "Delete  from student where uid = (%s)"
                    value = (ask_uid,)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print(row[2], "was removed !")

                else:
                    print("Incorrect name!")
                    print("(May be Case Sesitive)")

    ###############################
    #       Student Sub Functions #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       Library Sub Functions #
    ###############################
    #          STARTS             #
    ###############################

    def library_menu_add():

        """
        Add Books.
        No parameters.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Library"
        sub2 = "<Add>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()
        book_code = input("Enter Book Code: ")
        book_name = input("Enter Book Name: ")
        author_name = input("Enter Author Name: ")
        subject = input("Enter Subject: ")
        issued = input("Is this book Issued to some Student? (Yes/No): ")

        if issued == "Yes" or issued == "YES" or issued == "yes":
            stu_uid = int(input("Enter Student's UID: "))
            mycursor.execute("select * from student")
            rec = mycursor.fetchall()
            exists = False
            for row in rec:
                if row[0] == stu_uid:
                    return_date = input("Enter Assigned Return Date (YYYY-MM-DD): ")
                    return_status = input("Is this book returned? (Yes/No)")
                    sql = """
                    insert into Library
                    (
                    book_code, book_name, 
                    author_name, subject, 
                    issued, uid, return_date, 
                    return_status
                    ) 
                    values(%s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    val = (
                        book_code,
                        book_name,
                        author_name,
                        subject,
                        issued,
                        stu_uid,
                        return_date,
                        return_status,
                    )

                    try:
                        mycursor.execute(sql, val)
                        mydb.commit()
                        exists = True
                        sql1 = "select * from Library where book_code=(%s) and book_name=(%s) and author_name=(%s) and subject=(%s)"
                        val1 = (book_code, book_name, author_name, subject)
                        mycursor.execute(sql1, val1)
                        result = mycursor.fetchall()
                        print()
                        for row in result:
                            print("Book Added with Details!")
                            print()
                            print("BID:", row[0])
                            print("Book_Code:", row[1])
                            print("Book_Name:", row[2])
                            print("Author_Name:", row[3])
                            print("Subject:", row[4])
                            print("Issued:", row[5])
                            print("UID:", row[6])
                            print("Return_Date:", row[7])
                            print("Return_Status:", row[8])
                            print()
                        break

                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error", e)
                        print()

            if not exists:
                print("Student's UID is incorrect.")
                print("Go to Student section to see Student's UID")
                print()

        elif issued == "no" or issued == "No" or issued == "NO":
            sql = "insert into Library(book_code, book_name, author_name, subject, issued) values(%s, %s, %s, %s, 'No')"
            val = (book_code, book_name, author_name, subject)
            mycursor.execute(sql, val)
            mydb.commit()
            sql1 = "select * from Library where book_code=(%s) and book_name=(%s) and author_name=(%s) and subject=(%s)"
            val1 = (book_code, book_name, author_name, subject)
            mycursor.execute(sql1, val1)
            result = mycursor.fetchall()
            print()
            for row in result:
                print("Book Added with Details!")
                print()
                print("BID:", row[0])
                print("Book_Code:", row[1])
                print("Book_Name:", row[2])
                print("Author_Name:", row[3])
                print("Subject:", row[4])
                print("Issued:", row[5])
                print("UID:", row[6])
                print("Return_Date:", row[7])
                print("Return_Status:", row[8])
                print()

        else:
            print("Invalid option choose (Yes/No)")
            print()

    def library_menu_show():
        """
        Show all Books.
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Library"
            sub2 = "<Show>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Show all in Tabular Form")
            print("2: Show all in Simple Form")
            print("3: Count Book from Author Name")
            print("4: Count Book from Subject")
            print("5: Return")
            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                mycursor.execute("SELECT * FROM Library")
                rec = mycursor.fetchall()
                print("-" * 120)
                print(
                    f'{"BID":<5} | {"Book_Code":<8} | {"Book_Name":<15} | {"Author_Name":<8} | {"Subject":<9} | {"Issued":<18} | {"UID":<8} {"Return_Date":<8} {"Return_Status"}'
                )
                print("=" * 120)
                for row in rec:
                    print(
                        f"{row[0]:<8} | {row[1]:<8} | {row[2]:<8} | {row[3]:<8} | {row[4]:<8} | {row[5]:<8} | {row[6]} | {row[7]} | {row[8]}"
                    )
                print("-" * 120)

                print()
                print(
                    'Note this table may look ugly because "None" type Cannot be formatted.'
                )
                print("Look this table in your mysql database for better view!")
                print()

            elif choice == 2:
                mycursor.execute("SELECT * FROM Library")
                rec = mycursor.fetchall()
                print("Total rows are: ", len(rec))
                print("Printing each row")
                print()
                for row in rec:
                    print("BID:", row[0])
                    print("Book_Code:", row[1])
                    print("Book_Name:", row[2])
                    print("Author_Name:", row[3])
                    print("Subject:", row[4])
                    print("Issued:", row[5])
                    print("UID:", row[6])
                    print("Return_Date:", row[7])
                    print("Return_Status:", row[8])
                    print()
                print()

            elif choice == 3:
                mycursor.execute(
                    "select Author_Name, Count(*) from Library group by Author_Name"
                )
                rec = mycursor.fetchall()
                print()
                print(f"{'Author_Name':<30} | {'Number_of_Books'}")
                print("=" * 50)
                for row in rec:
                    print(f"{row[0]:<30} | {row[1]}")
                print("-" * 50)
                print()

            elif choice == 4:
                mycursor.execute(
                    "select Subject, Count(*) from Library group by Subject"
                )
                rec = mycursor.fetchall()
                print()
                print(f"{'Subject':<30} | {'Number_of_Books'}")
                print("=" * 50)
                for row in rec:
                    print(f"{row[0]:<30} | {row[1]}")
                print("-" * 50)

            elif choice == 5:
                break

            else:
                print()
                print("Invalid Choice")
                print()

    def library_menu_search():
        """
        Search for book(s) by entering details.
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Library"
            sub2 = "<Search>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Search with BID")
            print("2: Search with Book Code")
            print("3: Search with Book Name")
            print("4: Search with Author Name")
            print("5: Search with Subject")
            print("6: Search with Issued")
            print("7: Search with UID")
            print("8: Search with Return Date")
            print("9: Search with Return Status")
            print("10: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                ask_bid = input("Enter BID: ")
                sql = """SELECT * FROM Library WHERE BID=(%s)"""
                val = (ask_bid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with bid", ask_bid, "not found!")

            elif choice == 2:
                ask_bcode = input("Enter Book Code: ")
                sql = """SELECT * FROM Library WHERE book_code=(%s)"""
                val = (ask_bcode,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Book Code", ask_bcode, "not found!")

            elif choice == 3:
                ask_bname = input("Enter Book Name: ")
                sql = """SELECT * FROM Library WHERE book_name=(%s)"""
                val = (ask_bname,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Book Name", ask_bname, "not found!")
                    print()

            elif choice == 4:
                ask_aname = input("Enter Author Name: ")
                sql = """SELECT * FROM Library WHERE author_name=(%s)"""
                val = (ask_aname,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Author Name", ask_aname, "not found!")
                    print()

            elif choice == 5:
                ask_sub = input("Enter Subject: ")
                sql = """SELECT * FROM Library WHERE subject=(%s)"""
                val = (ask_sub,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Subject", ask_sub, "not found!")
                    print()

            elif choice == 6:
                ask_istatus = input("Enter Issued Status: ")
                sql = """SELECT * FROM Library WHERE issued=(%s)"""
                val = (ask_istatus,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Issued Status", ask_istatus, "not found!")
                    print()

            elif choice == 7:
                ask_suid = input("Enter Student UID: ")
                sql = """SELECT * FROM Library WHERE uid=(%s)"""
                val = (ask_suid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print(
                        "Any book with Issued to Student with UID",
                        ask_suid,
                        "not found!",
                    )
                    print()

            elif choice == 8:
                ask_rd = input("Enter Return_Date: ")
                sql = """SELECT * FROM Library WHERE return_date=(%s)"""
                val = (ask_rd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Return Date", ask_rd, "not found!")
                    print()

            elif choice == 9:
                ask_rs = input("Enter Return Status (Yes/No): ")
                sql = """SELECT * FROM Library WHERE return_status=(%s)"""
                val = (ask_rs,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                print()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("BID:", row[0])
                        print("Book_Code:", row[1])
                        print("Book_Name:", row[2])
                        print("Author_Name:", row[3])
                        print("Subject:", row[4])
                        print("Issued:", row[5])
                        print("UID:", row[6])
                        print("Return_Date:", row[7])
                        print("Return_Status:", row[8])
                        print()
                else:
                    print("Any book with Return Status", ask_rs, "not found!")
                    print()

            elif choice == 10:
                break

            else:
                print("Invalid Choice")

    def library_menu_update():
        """
        Update Book
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Library"
            sub2 = "<Update>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Update Book Code")
            print("2: Update Book Name")
            print("3: Update Author Name")
            print("4: Update Subject")
            print("5: Update Issued Status")
            print("6: Return")
            print()

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()
            exists = False
            if choice >= 1 and choice <= 5:
                bid = int(input("Enter BID of Book: "))

            if choice == 1:
                mycursor.execute("select * from Library")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == bid:
                        exists = True
                        new_bc = input("Enter new Book Code: ")
                        query = "update Library set book_code= (%s) where bid= (%s)"
                        value = (new_bc, bid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Book Code Updated!")

            elif choice == 2:
                mycursor.execute("select * from Library")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == bid:
                        exists = True
                        new_bn = input("Enter new Book Name: ")
                        query = "update Library set book_name= (%s) where bid= (%s)"
                        value = (new_bn, bid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Book Name Updated!")

            elif choice == 3:
                mycursor.execute("select * from Library")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == bid:
                        exists = True
                        new_an = input("Enter new Author Name: ")
                        query = "update Library set author_name= (%s) where bid= (%s)"
                        value = (new_an, bid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Author Name Updated!")

            elif choice == 4:
                mycursor.execute("select * from Library")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == bid:
                        exists = True
                        new_sub = input("Enter new Subject: ")
                        query = "update Library set subject= (%s) where bid= (%s)"
                        value = (new_sub, bid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Subject Updated!")

            elif choice == 5:
                mycursor.execute("select * from Library")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == bid:
                        exists = True
                        new_istatus = input("Enter New Issued Status (Yes/No): ")
                        if (
                            new_istatus in "YyEeSs"
                            or new_istatus == "Yes"
                            or new_istatus == "yes"
                        ):
                            stu_uid = int(input("Enter Student's UID: "))
                            mycursor.execute("select * from student")
                            rec = mycursor.fetchall()
                            exists = False
                            for row in rec:
                                if row[0] == stu_uid:
                                    return_date = input(
                                        "Enter Assigned Return Date (YYYY-MM-DD): "
                                    )
                                    return_status = input(
                                        "Is this book returned? (Yes/No): "
                                    )
                                    sql = """
                                    update Library 
                                    set 
                                    Issued='Yes', uid=(%s), Return_Date=(%s), Return_Status=(%s)
                                    where bid=(%s)
                                    """

                                    val = (stu_uid, return_date, return_status, bid)

                                    try:
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        exists = True
                                        print("Book Updated!")
                                        break

                                    except mysql.connector.errors.DataError as e:
                                        print()
                                        print("Error", e)
                                        print()

                            if not exists:
                                print("Student's UID is incorrect.")
                                print("Go to Student section to see Student's UID")
                                print()

                        else:
                            sql = """
                            update Library 
                            set 
                            Issued='No', uid=(%s), Return_Date=(%s), Return_Status=(%s)
                            where bid=(%s)
                            """

                            val = (None, None, None, bid)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            exists = True
                            print("Book Updated!")

            elif choice == 6:
                break

            else:
                print("Invalid Choice")

            if not exists and choice >= 1 and choice <= 5:
                print("Invalid Details")

    def library_menu_delete():
        """
        Delete book.
        NOTE: This process is irreversible.
        No parameters.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Library"
        sub2 = "<Delete>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        ask_bid = int(input("Enter BID of Book you want to remove: "))
        sql = "select * from Library where bid = (%s)"
        val = (ask_bid,)
        mycursor.execute(sql, val)
        rec = mycursor.fetchall()

        if len(rec) <= 0:
            print("Wrong BID")

        else:
            confirm_name = input("Confirm by entering Book's name: ")
            for row in rec:
                if confirm_name == row[2]:
                    query = "Delete from Library where bid = (%s)"
                    value = (ask_bid,)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print("Activity with Details")
                    print()
                    print("BID:", row[0])
                    print("Book_Code:", row[1])
                    print("Book_Name:", row[2])
                    print("Author_Name:", row[3])
                    print("Subject:", row[4])
                    print("Issued:", row[5])
                    print("UID:", row[6])
                    print("Return_Date:", row[7])
                    print("Return_Status:", row[8])
                    print()
                    print("Was removed !")
                    print()

                else:
                    print("Incorrect name!")
                    print("(May be Case Sesitive)")

    ###############################
    #       Library Sub Functions #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       CCA Sub Functions     #
    ###############################
    #          STARTS             #
    ###############################

    def cca_menu_add():
        """
        Add CCA Record.
        No parameters.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "CCA"
        sub2 = "<Add>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()
        activity_code = input("Enter Activity Code: ")
        activity_name = input("Enter Activity Name: ")
        date = input("Enter Activity's Date (YYYY-MM-DD): ")

        winner = input("Any Winner Decided yet? (Yes/No) ")

        if winner == "Yes" or winner == "yes" or winner == "YES":
            winner_uid = int(input("Enter Student's UID: "))
            mycursor.execute("select * from student")
            rec = mycursor.fetchall()
            exists = False
            for row in rec:
                if row[0] == winner_uid:
                    exists = True
                    prize = input("Enter Prize Given: ")
                    sql = """
                    insert into CCA
                    (
                    activity_code, activity_name, 
                    date, winner_uid, prize
                    ) 
                    values(%s, %s, %s, %s, %s)"""
                    val = (activity_code, activity_name, date, winner_uid, prize)
                    try:
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql1 = "select * from CCA where activity_code=(%s) and activity_name=(%s) and date=(%s)"
                        val1 = (activity_code, activity_name, date)
                        mycursor.execute(sql1, val1)
                        result = mycursor.fetchall()
                        print()
                        for row in result:
                            print("Activity Added with Details!")
                            print()
                            print("CCA_ID:", row[0])
                            print("Activity_Code:", row[1])
                            print("Activity_Name:", row[2])
                            print("Date:", row[3])
                            print("Winner_UID:", row[4])
                            print("Prize:", row[5])
                            print()
                        break
                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error", e)
                        print()

            if not exists:
                print("Student's UID is incorrect.")
                print("Go to Student section to see Students UID")
                print()

        elif winner == "no" or winner == "No" or winner == "NO":
            sql = """
            insert into CCA
            (Activity_Code, Activity_Name, Date, Winner_UID, Prize) 
            values(%s, %s, %s, %s, %s)"""
            val = (activity_code, activity_name, date, None, None)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                sql1 = "select * from CCA where activity_code=(%s) and activity_name=(%s) and date=(%s)"
                val1 = (activity_code, activity_name, date)
                mycursor.execute(sql1, val1)
                result = mycursor.fetchall()
                print()
                for row in result:
                    print("Activity Added with Details!")
                    print()
                    print("CCA_ID:", row[0])
                    print("Activity_Code:", row[1])
                    print("Activity_Name:", row[2])
                    print("Date:", row[3])
                    print("Winner_UID:", row[4])
                    print("Prize:", row[5])
                    print()

            except mysql.connector.errors.DataError as e:
                print()
                print("Error", e)
                print()

        else:
            print("Invalid option choose (Yes/No)")
            print()

    def cca_menu_show():
        """
        Show all CCA Records.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "CCA"
            sub2 = "<Show>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Show all in Tabular Form")
            print("2: Show all in Simple Form")
            print("3: Count Book from Activity Date")
            print("4: Return")
            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                mycursor.execute("SELECT * FROM CCA")
                rec = mycursor.fetchall()
                print("-" * 120)
                print(
                    f'{"CCA_ID":<5} | {"Activity_Code":<8} | {"Activity_Name":<15} | {"Date":<8} | {"Winner_UID":<9} | {"Prize":<18}'
                )
                print("=" * 120)
                for row in rec:
                    print(
                        f"{row[0]:<8} | {row[1]:<8} | {row[2]:<8} | {row[3]} | {row[4]} | {row[5]}"
                    )
                print("-" * 120)

                print()
                print(
                    'Note this table may look ugly because "None" type Cannot be formatted.'
                )
                print("Look this table in your mysql database for better view!")
                print()

            elif choice == 2:
                mycursor.execute("SELECT * FROM CCA")
                rec = mycursor.fetchall()
                print("Total rows are: ", len(rec))
                print("Printing each row")
                print()
                for row in rec:
                    print("CCA_ID:", row[0])
                    print("Activity_Code:", row[1])
                    print("Activity_Name:", row[2])
                    print("Date:", row[3])
                    print("Winner_UID:", row[4])
                    print("Prize:", row[5])
                    print()
                print()

            elif choice == 3:
                mycursor.execute("select Date, Count(*) from CCA group by Date")
                rec = mycursor.fetchall()
                print()
                print(f"{'Date':<} | {'Number_of_Activities'}")
                print("=" * 50)
                for row in rec:
                    print(f"{row[0]} | {row[1]}")
                print("-" * 50)
                print()

            elif choice == 4:
                break

            else:
                print()
                print("Invalid Choice")
                print()

    def cca_menu_search():
        """
        Search for CCA record(s) by entering details.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "CCA"
            sub2 = "<Search>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Search with CCA_ID")
            print("2: Search with Activity Code")
            print("3: Search with Activity Name")
            print("4: Search with Date")
            print("5: Search with Winner_UID")
            print("6: Search with Prize")
            print("7: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                ask_cid = input("Enter BID: ")
                sql = """SELECT * FROM CCA WHERE CCA_ID=(%s)"""
                val = (ask_cid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with CCA_ID", ask_cid, "not found!")

            elif choice == 2:
                ask_ac = input("Enter Activity Code: ")
                sql = """SELECT * FROM CCA WHERE Activity_Code=(%s)"""
                val = (ask_ac,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with Activity Code", ask_ac, "not found!")

            elif choice == 3:
                ask_an = input("Enter Activity Name: ")
                sql = """SELECT * FROM CCA WHERE Activity_Name=(%s)"""
                val = (ask_an,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with Activity Name", ask_an, "not found!")

            elif choice == 4:
                ask_ad = input("Enter Activity Date: ")
                sql = """SELECT * FROM CCA WHERE Date=(%s)"""
                val = (ask_ad,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with Activity Date", ask_ad, "not found!")

            elif choice == 5:
                ask_wid = input("Enter Winner UID: ")
                sql = """SELECT * FROM CCA WHERE Winner_UID=(%s)"""
                val = (ask_wid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with Winner UID", ask_wid, "not found!")

            elif choice == 6:
                ask_prize = input("Enter Prize: ")
                sql = """SELECT * FROM CCA WHERE Prize=(%s)"""
                val = (ask_prize,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("CCA_ID:", row[0])
                        print("Activity_Code:", row[1])
                        print("Activity_Name:", row[2])
                        print("Date:", row[3])
                        print("Winner_UID:", row[4])
                        print("Prize:", row[5])
                        print()
                else:
                    print("Any Activity with Prize", ask_prize, "not found!")

            elif choice == 7:
                break

            else:
                print("Invalid Choice")

    def cca_menu_update():
        """
        Update CCA Records.
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "CCA"
            sub2 = "<Update>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Update Activity Code")
            print("2: Update Activity Name")
            print("3: Update Date")
            print("4: Update Winner Status")
            print("5: Return")
            print()

            choice = int(input(type_animation("Enter your choice: ")))
            print()
            exists = False
            if choice >= 1 and choice <= 4:
                cid = int(input("Enter CCA_ID of Activity: "))

            if choice == 1:
                mycursor.execute("select * from CCA")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == cid:
                        exists = True
                        new_ac = input("Enter new Activity Code: ")
                        query = "update CCA set Activity_Code= (%s) where CCA_ID= (%s)"
                        value = (new_ac, cid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Activity Code Updated!")
                        print()

            elif choice == 2:
                mycursor.execute("select * from CCA")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == cid:
                        exists = True
                        new_an = input("Enter new Activity Name: ")
                        query = "update CCA set Activity_Name= (%s) where CCA_ID= (%s)"
                        value = (new_an, cid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Activity Name Updated!")
                        print()

            elif choice == 3:
                mycursor.execute("select * from CCA")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == cid:
                        exists = True
                        new_d = input("Enter new Activity Date: ")
                        query = "update CCA set Date= (%s) where CCA_ID= (%s)"
                        value = (new_d, cid)

                        try:
                            mycursor.execute(query, value)
                            mydb.commit()
                            print("Activity Date Updated!")
                            print()

                        except mysql.connector.errors.DataError as e:
                            print()
                            print("Error", e)
                            print()

            elif choice == 4:
                mycursor.execute("select * from CCA")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == cid:
                        exists = True
                        new_wstatus = input("Enter New Winner Status (Yes/No): ")
                        if (
                            new_wstatus == "YES"
                            or new_wstatus == "Yes"
                            or new_wstatus == "yes"
                        ):
                            stu_uid = int(input("Enter Winner's UID: "))
                            mycursor.execute("select * from student")
                            rec = mycursor.fetchall()
                            exists = False
                            for row in rec:
                                if row[0] == stu_uid:
                                    prize = input("Enter Prize: ")
                                    sql = "update CCA set Winner_UID=(%s), Prize=(%s) where CCA_ID=(%s)"
                                    val = (stu_uid, prize, cid)
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    exists = True
                                    print("Activity Updated!")
                                    break
                            if not exists:
                                print("Student's UID is incorrect.")
                                print("Go to Student section to see Student's UID")
                                print()

                        else:
                            sql = "update CCA set Winner_UID=(%s), prize=(%s) where CCA_ID=(%s)"
                            val = (None, None, cid)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            exists = True
                            print("Activity Updated!")

            elif choice == 5:
                break

            else:
                print("Invalid Choice")

            if not exists and choice >= 1 and choice <= 4:
                print("Invalid Details")

    def cca_menu_delete():
        """
        Delete CCA Record.
        NOTE: This process is irreversible.
        No parameters.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "CCA"
        sub2 = "<Delete>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        ask_cid = int(input("Enter CCA_ID of Activity you want to remove: "))
        sql = "select * from CCA where CCA_ID= (%s)"
        val = (ask_cid,)
        mycursor.execute(sql, val)
        rec = mycursor.fetchall()

        if len(rec) <= 0:
            print("Wrong CCA_ID")

        else:
            confirm_name = input("Confirm by entering Activity's name: ")
            for row in rec:
                if confirm_name == row[2]:
                    query = "Delete from CCA where CCA_ID= (%s)"
                    value = (ask_cid,)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print("Activity with Details")
                    print()
                    print("CCA_ID:", row[0])
                    print("Activity_Code:", row[1])
                    print("Activity_Name:", row[2])
                    print("Date:", row[3])
                    print("Winner_UID:", row[4])
                    print("Prize:", row[5])
                    print()
                    print("Was removed !")
                    print()

                else:
                    print("Incorrect name!")
                    print("(May be Case Sesitive)")
                    print()

    ###############################
    #       CCA Sub Functions     #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       Fees Sub Functions    #
    ###############################
    #          STARTS             #
    ###############################

    def fees_menu_add():
        """
        Add Fees.
        No parameters.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Fees"
        sub2 = "<Add>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        student_uid = int(input("Enter Student UID: "))

        mycursor.execute("select * from student")
        rec = mycursor.fetchall()
        exists = False
        for row in rec:
            if row[0] == student_uid:
                exists = True
                due_date = input("Enter Last Submission Date (YYYY-MM-DD): ")
                fee_status = input("This Student Submitted Fees? (Yes/No) ")

                if (
                    fee_status == "Yes"
                    or fee_status == "YES"
                    or fee_status == "yes"
                    or fee_status in "Yy"
                ):
                    submitted_date = input("Enter Submitted Date (YYYY-MM-DD): ")

                    sql = "insert into Fees(student_uid, due_date, fee_status, submitted_date) values(%s, %s, %s, %s)"
                    val = (student_uid, due_date, fee_status, submitted_date)

                    try:
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql1 = "select * from Fees where Student_UID =(%s) and Due_Date =(%s) and fee_status=(%s)"
                        val1 = (student_uid, due_date, fee_status)
                        mycursor.execute(sql1, val1)
                        result = mycursor.fetchall()
                        print()
                        for rw in result:
                            print("Fee Added with Details!")
                            print()
                            print("FID:", rw[0])
                            print("Student_UID:", rw[1])
                            print("Due_Date:", rw[2])
                            print("Fee_Status:", rw[3])
                            print("Submitted_Date:", rw[4])
                            print()
                        break

                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error", e)
                        print()

                elif fee_status == "no" or fee_status == "No" or fee_status == "NO":
                    sql = "insert into Fees(student_uid, due_date, fee_status, submitted_date) values(%s, %s, %s, %s)"
                    val = (student_uid, due_date, "No", None)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    sql1 = "select * from Fees where Student_UID =(%s) and Due_Date =(%s) and fee_status=(%s)"
                    val1 = (student_uid, due_date, fee_status)
                    mycursor.execute(sql1, val1)
                    result = mycursor.fetchall()
                    print()
                    for rw in result:
                        print("Fee Added with Details!")
                        print()
                        print("FID:", rw[0])
                        print("Student_UID:", rw[1])
                        print("Due_Date:", rw[2])
                        print("Fee_Status:", rw[3])
                        print("Submitted_Date:", rw[4])
                        print()

        if not exists:
            print("Student's UID is incorrect.")
            print("Go to Student section to see Students UID")
            print()

    def fees_menu_show():
        """
        Show all Fees.
        No parameters.
        """
        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Fees"
            sub2 = "<Show>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Show all in Tabular Form")
            print("2: Show all in Simple Form")
            print("3: Count Fees from Due Date")
            print("4: Return")
            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                mycursor.execute("SELECT * FROM Fees")
                rec = mycursor.fetchall()
                print("-" * 80)
                print(
                    f'{"FID":<8} | {"Student_UID":<8} | {"Due_Date":<10} | {"Fee_Status":<8} | {"Submitted_Date":<9}'
                )
                print("=" * 80)
                for row in rec:
                    print(f"{row[0]:<8} | {row[1]:<8} | {row[2]} | {row[3]} | {row[4]}")
                print("-" * 80)

                print()
                print(
                    'Note this table may look ugly because "None" type Cannot be formatted.'
                )
                print("Look this table in your mysql database for better view!")
                print()

            elif choice == 2:
                mycursor.execute("SELECT * FROM Fees")
                rec = mycursor.fetchall()
                print()
                print("Total rows are: ", len(rec))
                print("Printing each row")
                print()
                for row in rec:
                    print("FID:", row[0])
                    print("Student_UID:", row[1])
                    print("Due_Date:", row[2])
                    print("Fee_Status:", row[3])
                    print("Submitted_Date:", row[4])
                    print()

            elif choice == 3:
                mycursor.execute(
                    "select Due_Date, Count(*) from Fees group by Due_Date"
                )
                rec = mycursor.fetchall()
                print()
                print(f"{'Due_Date':<10} | {'Number_of_Fees'}")
                print("=" * 50)
                for row in rec:
                    print(f"{row[0]} | {row[1]}")
                print("-" * 50)
                print()

            elif choice == 4:
                break

            else:
                print()
                print("Invalid Choice")
                print()

    def fees_menu_search():
        """
        Search for Fees detail(s).
        No parameters.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Fees"
            sub2 = "<Search>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Search with FID")
            print("2: Search with Student_UID")
            print("3: Search with Due_Date")
            print("4: Search with Fee_Status")
            print("5: Search with Submitted_Date")
            print("6: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                ask_fid = input("Enter FID: ")
                sql = """SELECT * FROM Fees WHERE FID=(%s)"""
                val = (ask_fid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("FID:", row[0])
                        print("Student_UID:", row[1])
                        print("Due_Date:", row[2])
                        print("Fee_Status:", row[3])
                        print("Submitted_Date:", row[4])
                        print()
                else:
                    print("Any Fees Details with FID", ask_fid, "not found!")

            elif choice == 2:
                ask_sid = input("Enter Student UID: ")
                sql = """SELECT * FROM Fees WHERE Student_UID=(%s)"""
                val = (ask_sid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("FID:", row[0])
                        print("Student_UID:", row[1])
                        print("Due_Date:", row[2])
                        print("Fee_Status:", row[3])
                        print("Submitted_Date:", row[4])
                        print()
                else:
                    print("Any Fees Details with Student UID", ask_sid, "not found!")

            elif choice == 3:
                ask_dd = input("Enter Due Date: ")
                sql = """SELECT * FROM Fees WHERE Due_Date=(%s)"""
                val = (ask_dd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("FID:", row[0])
                        print("Student_UID:", row[1])
                        print("Due_Date:", row[2])
                        print("Fee_Status:", row[3])
                        print("Submitted_Date:", row[4])
                        print()
                else:
                    print("Any Fees Details with Due Date", ask_dd, "not found!")

            elif choice == 4:
                ask_fs = input("Enter Fee Status: ")
                sql = """SELECT * FROM Fees WHERE Fee_Status=(%s)"""
                val = (ask_fs,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("FID:", row[0])
                        print("Student_UID:", row[1])
                        print("Due_Date:", row[2])
                        print("Fee_Status:", row[3])
                        print("Submitted_Date:", row[4])
                        print()
                else:
                    print("Any Fees Details with Fee Status", ask_fs, "not found!")

            elif choice == 5:
                ask_sd = input("Enter Submitted Date: ")
                sql = """SELECT * FROM Fees WHERE Submitted_Date=(%s)"""
                val = (ask_sd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("FID:", row[0])
                        print("Student_UID:", row[1])
                        print("Due_Date:", row[2])
                        print("Fee_Status:", row[3])
                        print("Submitted_Date:", row[4])
                        print()
                else:
                    print("Any Fees Details with Submitted Date", ask_sd, "not found!")

            elif choice == 6:
                break

            else:
                print("Invalid Choice")

    def fees_menu_update():
        """
        Update Fee details.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Fees"
            sub2 = "<Update>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()

            print("1: Update Due_Date")
            print("2: Update Fee_Status")
            print("3: Update Student_UID")
            print("4: Return")
            print()

            choice = int(input(type_animation("Enter your choice: ")))
            print()
            exists = False
            if choice >= 1 and choice <= 4:
                fid = int(input("Enter FID of Fees: "))

            if choice == 1:
                mycursor.execute("select * from Fees")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == fid:
                        exists = True
                        new_ac = input("Enter new Due_Date (YYYY-MM-DD): ")
                        query = "update Fees set Due_Date= (%s) where FID= (%s)"
                        value = (new_ac, fid)

                        try:
                            mycursor.execute(query, value)
                            mydb.commit()
                            print("Due_Date Updated!")
                            print()

                        except mysql.connector.errors.DataError as e:
                            print()
                            print("Error", e)
                            print()

            elif choice == 2:
                mycursor.execute("select * from Fees")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == fid:
                        exists = True
                        new_ac = input("Enter new Fee_Status (Yes/No): ")
                        if (
                            new_ac == "Yes"
                            or new_ac == "YES"
                            or new_ac == "yes"
                            or new_ac in "Yy"
                        ):
                            submitted_date = input(
                                "Enter submitted_date (YYYY-MM-DD): "
                            )
                            query = "update Fees set Fee_Status= (%s), submitted_date=(%s) where FID= (%s)"
                            value = ("Yes", submitted_date, fid)

                            try:
                                mycursor.execute(query, value)
                                mydb.commit()
                                print("Status Updated!")
                                print()

                            except mysql.connector.errors.DataError as e:
                                print()
                                print("Error", e)
                                print()

                        elif (
                            new_ac == "NO"
                            or new_ac == "No"
                            or new_ac == "no"
                            or new_ac in "Nn"
                        ):
                            query = "update Fees set Fee_Status= (%s), submitted_date=(%s) where FID= (%s)"
                            value = ("No", None, fid)
                            mycursor.execute(query, value)
                            mydb.commit()
                            print("Status Updated!")
                            print()

                        else:
                            print("Invalid Choice")
                            print()

            elif choice == 3:
                mycursor.execute("select * from Fees")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == fid:
                        exists = True
                        stu_uid = int(input("Enter new Student_UID: "))
                        mycursor.execute("select * from student")
                        rec = mycursor.fetchall()
                        exists = False
                        for row in rec:
                            if row[0] == stu_uid:
                                sql = "update Fees set Student_UID=(%s) where FID=(%s)"
                                val = (stu_uid, fid)
                                mycursor.execute(sql, val)
                                mydb.commit()
                                exists = True
                                print("Student_UID Updated!")
                                break
                        if not exists:
                            print("Student's UID is incorrect.")
                            print("Go to Student section to see Student's UID")
                            print()

            elif choice == 4:
                break

            else:
                print("Invalid Choice")

            if not exists and choice >= 1 and choice <= 3:
                print("Invalid Details")

    def fees_menu_delete():
        """
        Delete Fee Record.
        NOTE: This process is irreversible.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Fees"
        sub2 = "<Delete>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        ask_fid = int(input("Enter FID of Fees you want to remove: "))
        sql = "select * from Fees where FID= (%s)"
        val = (ask_fid,)
        mycursor.execute(sql, val)
        rec = mycursor.fetchall()

        if len(rec) <= 0:
            print("Wrong FID")
            print()

        else:
            confirm = input(
                "Do you really want to Delete (This process is irreversible) (Yes/No): "
            )
            if (
                confirm == "Yes"
                or confirm in "Yy"
                or confirm == "yes"
                or confirm == "YES"
            ):
                sql = "delete from Fees where FID = (%s)"
                val = (ask_fid,)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Removed Successfully!")
                print("Exiting...")

            else:
                print(f"Fees Details with FID {ask_fid} was not removed!")
                print("Exiting...")
                print()

    ###############################
    #       Fees Sub Functions    #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #  Attendence Sub Functions   #
    ###############################
    #          STARTS             #
    ###############################

    def attendence_menu_add():
        """
        Add Attendence
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Attendence"
        sub2 = "<Add>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        student_uid = int(input("Enter Student UID: "))
        exists = False
        mycursor.execute("select * from student")
        rec = mycursor.fetchall()
        for row in rec:
            if row[0] == student_uid:
                exists = True
                date = input("Enter Date (YYYY-MM-DD): ")
                subject = input("Enter Subject: ")
                status = input("Enter status (P = Present, A = Absent) (P/A): ")

                if status in "Pp":
                    time_of_join = input("Enter time of join: (HH:MM:SS) ")
                    time_of_leave = input("Enter time of leave: (HH:MM:SS) ")
                    sql = """insert into Attendence
                    (student_uid, date, subject, status, time_of_join, time_of_leave) 
                    values(%s, %s,%s, %s, %s, %s)"""
                    val = (
                        student_uid,
                        date,
                        subject,
                        status,
                        time_of_join,
                        time_of_leave,
                    )
                    try:
                        mycursor.execute(sql, val)
                        mydb.commit()
                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error", e)
                        print("Enter Date in YYYY-MM-DD format!")
                        print("Enter Time in HH:MM:SS format!")
                        print()

                    sql1 = """
                    select * from Attendence 
                    where 
                    student_uid=(%s) and date=(%s) and 
                    status=(%s) and time_of_join=(%s) and 
                    time_of_leave=(%s)"""
                    val1 = (student_uid, date, status, time_of_join, time_of_leave)
                    mycursor.execute(sql1, val1)
                    r = mycursor.fetchall()
                    for i in r:
                        print()
                        print("Attendence Added with Details")
                        print()
                        print("AID:", i[0])
                        print("Student_UID:", i[1])
                        print("Date:", i[2])
                        print("Subject:", i[3])
                        print("Status:", i[4])
                        print("Time_of_Join:", i[5])
                        print("Time_of_Leave:", i[6])
                        print()

                elif status in "Aa":
                    sql = """insert into Attendence
                    (student_uid, date, subject, status, time_of_join, time_of_leave) 
                    values(%s, %s, %s, %s, %s, %s)"""
                    val = (student_uid, date, subject, "A", None, None)
                    mycursor.execute(sql, val)
                    mydb.commit()

                    sql1 = "select * from Attendence where student_uid=(%s) and date=(%s)and status=(%s)"
                    val1 = (student_uid, date, "A")
                    mycursor.execute(sql1, val1)
                    r = mycursor.fetchall()
                    for i in r:
                        print()
                        print("Attendence Added with Details")
                        print("AID:", i[0])
                        print("Student_UID:", i[1])
                        print("Date:", i[2])
                        print("Status:", i[3])
                        print("Time_of_Join:", i[4])
                        print("Time_of_Leave:", i[5])
                        print()

                else:
                    print("Invalid Choice!")

        if not exists:
            print()
            print("Incorrect Student UID")
            print("Check Student Section to get UID")
            print()

    def attendence_menu_show():
        """
        Show all Attendence.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Attendence"
            sub2 = "<Show>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Show all in Tabular Form")
            print("2: Show all in Simple Form")
            print("3: Count Fees from Due Date")
            print("4: Return")
            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                mycursor.execute("SELECT * FROM Attendence")
                rec = mycursor.fetchall()
                print("-" * 80)
                print(
                    f'{"AID":<8} | {"Student_UID":<8} | {"Date":<8} | {"Subject":<8} | {"Status":<8} | {"Time_of_Join":<9} | {"Time_of_Leave"}'
                )
                print("=" * 80)
                for row in rec:
                    print(
                        f"{row[0]:<8} | {row[1]:<8} | {row[2]} | {row[3]:<8} | {row[4]:<8} | {row[5]} | {row[6]}"
                    )
                print("-" * 80)

                print()
                print(
                    'Note this table may look ugly because "None" type Cannot be formatted.'
                )
                print("Look this table in your mysql database for better view!")
                print()

            elif choice == 2:
                mycursor.execute("SELECT * FROM Attendence")
                rec = mycursor.fetchall()
                print()
                print("Total rows are: ", len(rec))
                print("Printing each row")
                print()
                for row in rec:
                    print("AID:", row[0])
                    print("Student_UID:", row[1])
                    print("Date:", row[2])
                    print("Subject", row[3])
                    print("Status:", row[4])
                    print("Time_of_Join:", row[5])
                    print("Time_of_Leave:", row[6])
                    print()

            elif choice == 3:
                mycursor.execute(
                    "select Subject, count(Status) from Attendence group by Time_of_Join"
                )
                rec = mycursor.fetchall()
                print()
                print(f"{'Due_Date':<10} | {'Number_of_Fees'}")
                print("=" * 50)
                for row in rec:
                    print(f"{row[0]} | {row[1]} ")
                print("-" * 50)
                print()

            elif choice == 4:
                break

            else:
                print()
                print("Invalid Choice")
                print()

    def attendence_menu_search():
        """
        Search for Attendence detail(s).
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Attendence"
            sub2 = "<Search>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Search with AID")
            print("2: Search with Student_UID")
            print("3: Search with Date")
            print("4: Search with Subject")
            print("5: Search with Status")
            print("6: Search with Time_of_Join")
            print("7: Search with Time_of_Leave")
            print("8: Return")

            print()
            choice = int(input(type_animation("Enter your choice: ")))
            print()

            if choice == 1:
                ask_fid = input("Enter AID: ")
                sql = """SELECT * FROM Attendence WHERE AID=(%s)"""
                val = (ask_fid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print("Any Attendence Details with AID", ask_fid, "not found!")

            elif choice == 2:
                ask_sid = input("Enter Student UID: ")
                sql = """SELECT * FROM Attendence WHERE Student_UID=(%s)"""
                val = (ask_sid,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print(
                        "Any Attendence Details with Student UID", ask_sid, "not found!"
                    )

            elif choice == 3:
                ask_dd = input("Enter Date: ")
                sql = """SELECT * FROM Attendence WHERE Date=(%s)"""
                val = (ask_dd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print("Any Attendence Details with Date", ask_dd, "not found!")

            elif choice == 4:
                ask_fs = input("Enter Subject: ")
                sql = """SELECT * FROM Attendence WHERE Subject=(%s)"""
                val = (ask_fs,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print("Any Attendence Details with Subject", ask_fs, "not found!")

            elif choice == 5:
                ask_sd = input("Enter Status: ")
                sql = """SELECT * FROM Attendence WHERE Status=(%s)"""
                val = (ask_sd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print("Any Attendence Details with Status", ask_sd, "not found!")

            elif choice == 6:
                ask_sd = input("Enter Time_of_Join (HH:MM:SS) : ")
                sql = """SELECT * FROM Attendence WHERE Time_of_Join=(%s)"""
                val = (ask_sd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print(
                        "Any Attendence Details with Time_of_Join", ask_sd, "not found!"
                    )

            elif choice == 7:
                ask_sd = input("Enter Time_of_Leave (HH:MM:SS) : ")
                sql = """SELECT * FROM Attendence WHERE Time_of_Leave=(%s)"""
                val = (ask_sd,)
                mycursor.execute(sql, val)
                rec = mycursor.fetchall()
                if len(rec) >= 1:
                    print()
                    print("Total rows are: ", len(rec))
                    print("Printing each row")
                    print()
                    for row in rec:
                        print("AID:", row[0])
                        print("Student_UID:", row[1])
                        print("Date:", row[2])
                        print("Subject:", row[3])
                        print("Status:", row[4])
                        print("Time_of_Join:", row[5])
                        print("Time_of_Leave:", row[6])
                        print()
                else:
                    print(
                        "Any Attendence Details with Time_of_Leave",
                        ask_sd,
                        "not found!",
                    )
            elif choice == 8:
                break

            else:
                print("Invalid Choice")

    def attendence_menu_update():
        """
        Update Attendence.
        """

        while True:
            heading = "SCHOOL MANAGEMENT SYSTEM"
            sub1 = "Attendence"
            sub2 = "<Update>"

            print("=" * len(heading.center(100, "-")))
            print(heading.center(100))
            print(sub1.center(100))
            print(sub2.center(100, "-"))
            print("=" * len(heading.center(100, "-")))
            print()
            print("1: Update Date")
            print("2: Update Subject")
            print("3: Update Status")
            print("4: Update Student_UID")
            print("5: Return")
            print()

            choice = int(input(type_animation("Enter your choice: ")))
            print()
            exists = False
            if choice >= 1 and choice <= 4:
                aid = int(input("Enter AID of Attendence: "))

            if choice == 1:
                mycursor.execute("select * from Attendence")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == aid:
                        exists = True
                        new_ac = input("Enter new Date: ")
                        query = "update Attendence set Date= (%s) where AID= (%s)"
                        value = (new_ac, aid)
                        try:
                            mycursor.execute(query, value)
                            mydb.commit()

                            print("Date Updated!")
                            print()

                        except mysql.connector.errors.DataError as e:
                            print()
                            print("Error", e)
                            print("Enter Correct Date in YYYY-MM-DD format!")
                            print()

            elif choice == 2:
                mycursor.execute("select * from Attendence")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == aid:
                        exists = True
                        new_ac = input("Enter new Subject: ")
                        query = "update Attendence set Subject= (%s) where AID= (%s)"
                        value = (new_ac, aid)
                        mycursor.execute(query, value)
                        mydb.commit()
                        print("Subject Updated!")
                        print()

            elif choice == 3:
                mycursor.execute("select * from Attendence")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == aid:
                        exists = True
                        new_wstatus = input(
                            "Enter New Status P=Present, A=Absent (P/A) : "
                        )
                        if new_wstatus in "Pp":
                            time_of_join = input("Enter Time_of_Join (HH:MM:SS) : ")
                            time_of_leave = input("Enter Time_of_Leave (HH:MM:SS) : ")
                            sql = """
                            update Attendence 
                            set 
                            Status=(%s), Time_of_Join=(%s), Time_of_Leave=(%s) 
                            where AID=(%s)"""
                            val = ("P", time_of_join, time_of_leave, aid)
                            mycursor.execute(sql, val)

                            try:
                                mydb.commit()
                                exists = True
                                print("Status Updated!")
                                print()
                                break

                            except mysql.connector.errors.DataError as e:
                                print()
                                print("Error", e)
                                print()

                        elif new_wstatus in "Aa":
                            sql = """update Attendence 
                            set 
                            Status=(%s), Time_of_Join=(%s), Time_of_Leave=(%s) 
                            where AID=(%s)"""
                            val = ("A", None, None, aid)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            exists = True
                            print("Activity Updated!")
                            print()

                        else:
                            print("Invalid Choice")
                            print()

            elif choice == 4:
                mycursor.execute("select * from Attendence")
                result = mycursor.fetchall()
                for r_col in result:
                    if r_col[0] == aid:
                        exists = True
                        stu_uid = int(input("Enter new Student_UID: "))
                        mycursor.execute("select * from student")
                        rec = mycursor.fetchall()
                        exists = False
                        for row in rec:
                            if row[0] == stu_uid:
                                sql = "update Attendence set Student_UID=(%s) where AID=(%s)"
                                val = (stu_uid, aid)
                                mycursor.execute(sql, val)
                                mydb.commit()
                                exists = True
                                print("Student_UID Updated!")
                                print()
                                break
                        if not exists:
                            print("Student's UID is incorrect.")
                            print("Go to Student section to see Student's UID")
                            print()

            elif choice == 5:
                break

            else:
                print("Invalid Choice")

            if not exists and choice >= 1 and choice <= 4:
                print("Invalid Details")

    def attendence_menu_delete():
        """
        Delete Attendence Record.
        NOTE: This process is irreversible.
        """

        heading = "SCHOOL MANAGEMENT SYSTEM"
        sub1 = "Attendence"
        sub2 = "<Delete>"

        print("=" * len(heading.center(100, "-")))
        print(heading.center(100))
        print(sub1.center(100))
        print(sub2.center(100, "-"))
        print("=" * len(heading.center(100, "-")))
        print()

        ask_aid = int(input("Enter AID of Attendence you want to remove: "))
        print()
        sql = "select * from Attendence where AID= (%s)"
        val = (ask_aid,)
        mycursor.execute(sql, val)
        rec = mycursor.fetchall()

        if len(rec) <= 0:
            print("Wrong AID")

        else:
            confirm_name = input("Confirm by entering Subject : ")
            for row in rec:
                if confirm_name == row[3]:
                    query = "Delete from Attendence where AID= (%s)"
                    value = (ask_aid,)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print("Activity with Details")
                    print()
                    print("AID:", row[0])
                    print("Student_UID:", row[1])
                    print("Date:", row[2])
                    print("Subject:", row[3])
                    print("Status:", row[4])
                    print("Time_of_Join:", row[5])
                    print("Time_of_Leave:", row[6])
                    print()
                    print("Was removed !")
                    print()

                else:
                    print("\nIncorrect name!")
                    print("(May be Case Sesitive)")

    ###############################
    #   Attendence Sub Functions  #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    ###############################
    #       SUB Functions         #
    ###############################
    #          ENDS               #
    ###############################

    # ====================================================================#

    # At last calling main function.
    # Without this nothing will work.
    main()


except Exception as e:
    """
    If entered user credentials are incorrect,
    then raise appropriate error.
    """

    print()
    print("Error", e)
    print("Exiting ...")
    print()

