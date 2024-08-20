import sqlite3

connection = sqlite3.connect("Complaints.db")
cursor = connection.cursor()

sql_comm = """CREATE TABLE IF NOT EXISTS complain (
ID INTEGER PRIMARY KEY,
customername TEXT,
complaint TEXT,
status TEXT DEFAULT 'UNRESOLVED'
);"""
cursor.execute(sql_comm)

def NewComplaint():
    name = input("Enter Your Name:")
    comp = input("Enter Your Complaint:")

    sql_com = """INSERT INTO complain(customername, complaint) VALUES (?, ?);"""
    cursor.execute(sql_com, (name, comp))
    connection.commit()
    print("Complaint registered successfully.")
    result = cursor.execute("""SELECT ID FROM complain WHERE customername = ? and complaint = ?""", (name,comp))
    cusid = result.fetchall()
    print("Complaint Id:",cusid) 
    option()

def changestat():
    name1 = input("Enter Your name:")
    id1 = int(input("Enter your Complaint Id:"))
    cursor.execute("""UPDATE complain SET status = 'RESOLVED' WHERE ID = ? AND customername = ?""", (id1, name1))
    connection.commit()
    result = cursor.execute("""SELECT * FROM complain WHERE customername = ? AND ID = ?""", (name1, id1))
    print("Complaint status updated successfully.")
    print(result.fetchall())
    option()

def option():
    print("1. New Complaint\n2. Change Status\n3. Exit")
    option = int(input("Enter The Option(1/2/3):"))

    if option == 1:
        NewComplaint()
    elif option == 2:
        changestat()
    elif option == 3:
        print("Thank You")
        connection.close()
    else:
        print("Invalid option. Please choose again.")
        option()

option()

connection.close()