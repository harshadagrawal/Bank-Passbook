import mysql.connector as m

# method for new account create
def create_acc():
    #connecting to mysql
    mydb = m.connect(host="localhost",user="root",password="honey@123")
    cursor = mydb.cursor()
    #creating database
    cursor.execute("create database if not exists bank")
    cursor.execute("use bank")
    #creating table 
    cursor.execute("create table if not exists passbook(Name varchar(100) NOT NULL, Account_no int PRIMARY KEY auto_increment, DOB DATE , Address varchar(100), Mobile_no BIGINT, Balance int)")
    #datas to be inserted into table
    Name=input("Customer Name: ")
    DOB=input("Date of Birth(yyyy-mm-dd): ")
    Address=input("Address: ")
    Mobile_no=int(input("Mobile number: "))
    Balance=int(input("Opening Balance: "))
    #inserting values into table
    query="insert into passbook(Name,DOB,Address,Mobile_no,Balance) values(%s,%s,%s,%s,%s)"
    customer=(Name,DOB,Address,Mobile_no,Balance)
    cursor.execute(query,customer)
    mydb.commit()
    print("Transection Successful")

# Show customers
def show():
    mydb = m.connect(host="localhost",user="root",password="honey@123",database="bank")
    cursor = mydb.cursor()
    cursor.execute("Select Name,Account_No,date_format(DOB,'%d-%M-%Y'),Address from passbook")
    data =cursor.fetchall()
    for i in data:
        print("Name          : ",i[0])
        print("Account_No.   : ",i[1])
        print("Date_of_Birth : ",i[2])
        print("Address       : ",i[3],"\n")
# show()       
        
# method for checck balance in perticular account 
def check_bal():
    #connecting to database
    mydb = m.connect(host="localhost",user="root",password="honey@123",database="bank")
    cursor = mydb.cursor()
    acc_no=[(int(input("Enter account no.: ")))]
    query = "select balance from passbook where Account_no = %s"
    cursor.execute(query,acc_no)
    bal = cursor.fetchall()
    print("\nAccount Balance is: ",bal[0][0])

# method for money deposite in account
def deposite():
    mydb = m.connect(host="localhost",user="root",password="honey@123",database="bank")
    cursor = mydb.cursor()
    amt = (int(input("Enter Amount: ")))
    acc_no = (int(input("Enter Account no.: ")))
    query1 = "UPDATE passbook SET balance=balance + %s WHERE Account_no = %s"
    info = (amt,acc_no)
    cursor.execute(query1,info)
    # bal = cursor.fetchall()
    mydb.commit()
    print("\nTransection Successful")

# method for money withdrawl
def withdrawl():
    mydb = m.connect(host="localhost",user="root",password="honey@123",database="bank")
    cursor = mydb.cursor()
    Amt=(int(input("Enter Amount: ")))
    Acc_no=(int(input("Enter acc_no: ")))
    query="update passbook set balance=balance-%s where Account_no = %s"
    info=(Amt,Acc_no)
    cursor.execute(query,info)
    mydb.commit()
    print("Transection Successful")
    
# Exit
def exit():
    print("Thank you")


print("""
1. Create Account
2. Check Balance
3. Deposit an Amount
4. Withdraw an Amount
5. Show Customers
0. Exit """)

while True:
    a=int(input("\nChoose Correct Option and Press Enter: "))
    if a==1:
        create_acc()
        continue
    elif a==2:
        check_bal()
        continue
    elif a==3:
        deposite()
        continue
    elif a==4:
        withdrawl()
        continue
    elif a==5:
        show()
        continue
    elif a==0:
        exit()
        break
    else:
        print("Invalid Input")
        break