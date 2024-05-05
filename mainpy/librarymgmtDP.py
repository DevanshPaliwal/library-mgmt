#Library Management
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="librarymanagement")

def addnew():
    x=input("\nEnter book id:")
    y=input("Enter book name:")
    z=input("Enter author name:")
    c=input("Enter year of launch:")  
    mycursor=mydb.cursor()
    sql="INSERT INTO books VALUES ("+x+",'"+y+"','"+z+"',"+c+")"
    mycursor.execute(sql)
    mydb.commit()
    print("Book Added")
def srchbook():
    q=input("\nEnter book name to search:")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM books WHERE BookName = '"+q+"'")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
def updatebook():
    a=input("\nEnter BookID to change:")
    t=input("Enter new BookID:")
    u=input("Enter new Book Name:")
    o=input("Enter Author name:")
    p=input("Enter new value for year of launch:")
    mycursor=mydb.cursor()
    sql="UPDATE books SET BookID="+t+" , BookName='"+u+"' , Author='"+o+"' , Yearoflaunch="+p+" WHERE BookID="+a+""
    mycursor.execute(sql)
    mydb.commit()
    print("Book updated")
def dltbook():
    t=input("Enter BookID to delete:")
    mycursor=mydb.cursor()
    mycursor.execute("DELETE FROM books WHERE BookID = '"+t+"'")
    mydb.commit()
    print("Book deleted")
def addmember():
        x=input("\nEnter member id:")
        y=input("Enter member name:")
        z=input("Enter year of joining:")
        c=input("Enter member city:")
        mycursor=mydb.cursor()
        sql="INSERT INTO members VALUES ("+x+",'"+y+"',"+z+",'"+c+"')"
        mycursor.execute(sql)
        mydb.commit()
        print("Member Added")
def srchmemb():
    q=input("\nEnter member name to search:")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM members WHERE M_Name = '"+q+"'")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
def updatememb():
    a=input("\nEnter Member ID to change:")
    t=input("Enter new Member ID:")
    u=input("Enter new Member Name:")
    o=input("Enter Year of joining:")
    p=input("Enter Member City:")
    mycursor=mydb.cursor()
    sql="UPDATE members SET M_ID="+t+" , M_Name='"+u+"' , YearOfJoining='"+o+"' , M_City='"+p+"' WHERE M_ID="+a+""
    mycursor.execute(sql)
    mydb.commit()
    print("Member updated")
def dltmemb():
    t=input("Enter Member ID to delete:")
    mycursor=mydb.cursor()
    mycursor.execute("DELETE FROM members WHERE M_ID = '"+t+"'")
    mydb.commit()
    print("Member deleted")    

x=0
while(x!=9):
    x=int(input(" Press 1 to add new book.\n"
            "\n Press 2 to search for a book.\n"
            "\n Press 3 to update a book.\n"
            "\n Press 4 to delete a book.\n"
            "\n Press 5 to add new member.\n"
            "\n Press 6 to search for a member.\n"
            "\n Press 7 to update a member data.\n"
            "\n Press 8 to delete a member data.\n"
            "\n Press 9 to exit.\n"
            "\n Enter your choice:"))
    if x==1:
         addnew()
    elif x==2:
        srchbook()
    elif x==3:
         updatebook()
    elif x==4:
         dltbook()
    elif x==5:
           addmember()
    elif x==6:
        srchmemb()
    elif x==7:
        updatememb()
    elif x==8:
        dltmemb()
    elif x==9:
        print("Thanks for using")
    else:
        print("Enter valid number")
        
