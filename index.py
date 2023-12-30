import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="12345")
c=con.cursor()

c.execute("create database if not exists school")

c.execute("use school")

c.execute("create table if not exists student(admno int auto_increment,name varchar(30),class varchar(2),address varchar(40),mbno char(10))")

c.execute("create table if not exists salary(empid int,name varchar(30),basic bigint,hra bigint,da bigint,gross_sal bigint,net_sal bigint) ")

c.execute("create table if not exists teacher(empid int auto_increment,name varchar(30),dept varchar(20),bas_sal int,mbno char(10))")

c.execute("create table if not exists fees(admno int,name varchar(30),class varchar(2),deposit bigint,month varchar(10))")

con.commit()

 # Function to add a student

def ast():                 
    n=input("Student name:")
    c=input("Class:")
    a=input("Address:")
    p=input("Mobile Number:")
    data=(n,c,a,p)
    data1=[c,n]
    sql="insert into student values(admno,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    c=con.cursor()
    sql1="select * from student where class=%s and name=%s"
    c.execute(sql1,data1)
    w=c.fetchall()
    for i in w:
        print("Your admission number is :",i[0])
    con.commit()
    print("Data entered successfully")
    print(">----------------------------------------------------------<")
    main()


 # Function to remove a student
 
def rst():        
    c=input("Class :")
    r=input("Admission Number:")
    data=(c,r)
    sql="delete from student where class=%s and admno=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------<")
    main()

 # Function to add a teacher

def addt():                             
    n=input("Teacher name: ")
    p=input("Department: ")
    s=input("Salary: ")
    m=input("Mobile Number: ")
    data=(n,p,s,m)
    data1=(n,s)
    sql="insert into teacher values(empid,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    sql2="select * from teacher where name=%s and dept=%s"
    c.execute(sql2,[n,p])
    w=c.fetchall()
    for i in w:
        print("Your Employee ID  :",i[0])
        admno=i[0]
    data1=(admno,n,s)
    c=con.cursor()
    sql1="insert into salary values(%s,%s,%s,(0.3)*basic,(0.2)*basic,basic+hra+da,gross_sal-(0.12)*basic)"
    c.execute(sql1,data1)
    con.commit()
    print("Data Entered Succesfully")
    print(">----------------------------------------------------------<")
    main()


# Function to remove a teacher

def remt():                       
    n=input("Teacher name:")
    eid=input("Employee ID.:")
    data=(n,eid)
    sql="delete from teacher where name=%s and empid=%s;"
    c=con.cursor()
    c.execute(sql,data)
    c=con.cursor()
    sql1="delete from salary where name=%s and empid=%s"
    c.execute(sql1,data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------<")
    main()


# Function to deposit fees and check due status for a particular class

def fees():
    print("1.DEPOSIT FEES","2.CHECK DUE STATUS",sep="\n")
    ch=int(input("Enter choice :"))
    if ch==1:
        n=input("Enter admission number")
        sql="select * from student where admno=%s"
        c=con.cursor()
        c.execute(sql,(n,))
        d=c.fetchall()
        for i in d:
            n=input("Deposit Amount :")
            r=input("Month :")
            sql1="insert into fees values(%s,%s,%s,%s,%s)"
            c=con.cursor()
            c.execute(sql1,(i[0],i[1],i[2],n,r,))
            con.commit()
        print("Data Entered Successfully")
        print(">----------------------------------------------------------<")
        main()
    elif ch==2:
        m=input("Class :")
        n=input("Check Due for Month :")
        sql2="select * from fees where month=%s and class=%s"
        c=con.cursor()
        c.execute(sql2,(n,m,))
        e=c.fetchall()
        l=[]
        for i in e:
            l.append(i[1])
        c=con.cursor()
        sql3="select * from student where class=%s"
        c.execute(sql3,(m,))
        f=c.fetchall()
        l1=[]
        g={}
        for i in f:
            g[i[0]]=i[1]
            l1.append(i[1])
        con.commit()
        print("List of Defaulters :")
        for i in g:
            if g[i] not in l:
                print("Admission Number :",i)
                print("Name :",g[i])
                print(">----------------------------<")
    else:
        print("Wrong Option")
    print(">----------------------------------------------------------")
    main()

# Function to generate salary slip given an employee ID

def dppays():
    n=input("Employee Id :")
    data=[n,]
    sql="select * from salary where empid=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("Name  :",i[1])
        print("Basic Salary :",i[2])
        print("HRA             :",i[3])
        print("DA                :",i[4])
        print("Gross Salary :",i[5])
        print("Net salary(After PF deductions)  :",i[6])
        print(">----------------------------------------------------------<")
    main()


# Function to show name of all students with information in classwise manner

def dpclass():
    cl=input("Class:")
    print(">----------------------------------------<")
    data=[cl]
    sql="select * from student where class=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("ID :",i[0])
        print("Name:",i[1])
        print("Class:",i[2])
        print("Address:",i[3])
        print("Phone:",i[4])
        print(">----------------------------------------<")
    con.commit()
    main()

# Function to show name of all teachers with information department wise manner

def dteacher():
    d=input("Department:")
    print(">----------------------------------------<")
    sql="select * from teacher WHERE dept=%s"
    c=con.cursor()
    c.execute(sql,(d,))
    d=c.fetchall()
    for i in d:
        print("ID :",i[0])
        print("Name:",i[1])
        print("Department :",i[2])
        print("Mobile Number:",i[4])
        print(">----------------------------------------<")
    print(">----------------------------------------------------------<")
    main()

# Main Function to start the program and showcase visually 

def main():
    print("""                                           Welcome to School Managment Program
                                                  DIGITAL WORLD SCHOOL
                               1. ADD STUDENT                2. REMOVE STUDENT
                               3. ADD TEACHER               4. REMOVE TEACHER
                               5. FEE STATUS                    6. GENERATE SALARY SLIP
                               7. DISPLAY CLASS             8. TEACHER'S LIST

                                                      Press E for exit""")
    
    choice=input("Enter Task no.:")
    print(">----------------------------------------<")
    if choice =='1':
        ast()
    elif choice=='2':
        rst()
    elif choice=='3':
        addt()
    elif choice=='4':
        remt()
    elif choice=='5':
        fees()
    elif choice=='6':
        dppays()
    elif choice=='7':
        dpclass()
    elif choice=='8':
        dteacher()
    elif choice=="E" or 'e':
        exit()
    else:
        print("Wrong Choice..............")
        main()

def pswd():
    p=input("Password:")
    if p=="123":
        main()
    else:
        print("Wrong password")
        pswd()
pswd()



        
        
        
        

    
    

