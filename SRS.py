import mysql.connector as db #SQL interface
conn = db.connect(
        host="localhost",
        user="root",
        database="sysadmin",
        password="mysql")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS STUDENT1(
                ROLL_NO INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                FATHER_NAME TEXT NOT NULL,
                MOBILE_NO INT NOT NULL,
                AGE INT NOT NULL,
                DEPARTMENT TEXT NOT NULL)""") 
cur.execute("""CREATE TABLE IF NOT EXISTS RESULT1(
                ROLL_NO INT PRIMARY KEY NOT NULL,
                EXAMINATION TEXT NOT NULL,
                COMPUTER INT  NOT NULL,
                MATH TEXT NOT NULL,
                PHYSICS INT NOT NULL,
                CHEMISTRY INT NOT NULL,
                ENGLISH INT NOT NULL,
                FOREIGN KEY (ROLL_NO) REFERENCES STUDENT1(ROLL_NO))""")
conn.commit()




def insert_data():
    ch="y"
    while(ch=="y" or ch=="Y"):
           i=0
           stu_roll_no=int(input("\n\nENTER THE ROLL NUMBER :"))

           q0 = "SELECT * FROM STUDENT1 where ROLL_NO=%s"
           cur.execute(q0, (stu_roll_no,))
           a=cur.fetchall()
           for row in a:
               if(stu_roll_no == row[0]):
                   print("\nTHIS ROLL NUMBER ALREADY EXISTS")
                   print("\n1.UPDATE THE EXISTING RECORD\n2.INSERT NEW RECORD\nPRESS ANY KEY TO GO BACK")
                   sel=input("\nENTER CHOICE : ")
                   if sel=='1':
                       update_data()
                       i=1
                       ch="n"
                   elif sel=='2':
                       ch="y"
                       i=1
                   else:
                       admin()
                       ch="n"
                       i=1
                           
               else:
                   break
           if i!=1:
               stu_name=input("ENTER STUDENT NAME :")
               father_name=input("ENTER  FATHER NAME :")
               mobile=input("ENTER THE MOBILE NO :")
               while(len(mobile)!=10):
                   mobile=input("\nPLEASE ENTER 10-DIGIT MOBILE NUMBER :")
               stu_mobile_no=int(mobile)

               stu_age=int(input("ENTER STUDENT AGE :"))
               while(stu_age<=0 or stu_age>=30):
                   stu_age=int(input("\nENTER CORRECT STUDENT AGE"))
               
               stu_dept=input("ENTER THE DEPARTMENT NAME :")
               stu_dept.upper()
               exam=input("ENTER EXAMINATION NAME :")
               computer=int(input("ENTER MARKS IN COMPUTER :"))
               math=int(input("ENTER MARKS IN MATH :"))
               physics=int(input("ENTER MARKS IN PHYSICS :"))
               chemistry=int(input("ENTER MARKS IN CHEMISTRY :"))
               english=int(input("ENTER MARKS IN ENGLISH :"))

               cur.execute("insert into student1 (ROLL_NO,NAME,FATHER_NAME,MOBILE_NO,AGE,DEPARTMENT) values (%s, %s, %s, %s, %s, %s)",(stu_roll_no,stu_name,father_name,stu_mobile_no,stu_age,stu_dept))
               cur.execute("insert into result1 (ROLL_NO,EXAMINATION,COMPUTER,MATH,PHYSICS,CHEMISTRY,ENGLISH) values (%s, %s, %s, %s, %s, %s, %s)",(stu_roll_no,exam,computer,math,physics,chemistry,english))

               print("\n\nRECORD ENTERED SUCCESSFULLY")
               conn.commit()
               ch=input("\n\nWANT TO INSERT ANOTHER RECORD ? (Y/N) : ")

def  update_data():
    ch="y"
    u=0
    rn=int(input("\nENTER STUDENT ROLL NUMBER TO UPDATE RECORD :"))
    q0 = "SELECT * FROM STUDENT1 where ROLL_NO=%s"
    cur.execute(q0, (rn,))
    a=cur.fetchall()
    for row in a:
        if(rn == row[0]):
            while(ch=="y" or ch=="Y"):
                u=1
                print("\n1.UPDATE STUDENT NAME ")
                print("2.UPDATE FATHER NAME ")
                print("3.UPDATE MOBILE NUMBER ")
                print("4.UPDATE STUDENT AGE ")
                print("5.UPDATE DEPARTMENT ")
                print("6.UPDATE MARKS IN COMPUTER ")
                print("7.UPDATE MARKS IN MATH ")
                print("8.UPDATE MARKS IN PHYSICS ")
                print("9.UPDATE MARKS IN CHEMISTRY ")
                print("10.UPDATE MARKS IN ENGLISH ")
                print("11.UPDATE EXAMINATION NAME ")
                choice = int(input("\nENTER YOUR CHOICE : "))

                if (choice == 1):
                    up_name = input("\nENTER STUDENT NAME :")
                    q5 = "UPDATE STUDENT1 SET NAME=%s where ROLL_NO=%s"
                    cur.execute(q5, (up_name, rn,))
                    print("\nNAME SUCCESSFULLY UPDATED")

                elif(choice==2):
                    up_f_name = input("\nENTER FATHER NAME :")
                    q6 = "UPDATE STUDENT1 SET FATHER_NAME=%s where ROLL_NO=%s"
                    cur.execute(q6, (up_f_name, rn,))
                    print("\nFATHER NAME UPDATED SUCCESSFULLY")

                elif(choice == 3):
                    mn = input("\nENTER MOBILE NUMBER :")
                    while(len(mn)!=10):
                        mn=input("\nPLEASE ENTER 10-DIGIT MOBILE NUMBER :")
                    up_mn=int(mn)
                    q7 = "UPDATE STUDENT1 SET MOBILE_NO=%s where ROLL_NO=%s"
                    cur.execute(q7, (up_mn, rn,))
                    print("\nMOBILE NUMBER UPDATED SUCCESSFULLY")

                elif(choice == 4):
                    up_age = int(input("\nENTER STUDENT AGE :"))
                    while(up_age<=0 or up_age>30):
                             up_age=int(input("\nENTER CORRECT STUDENT AGE"))                    
                    q15 = "UPDATE STUDENT1 SET AGE=%s where ROLL_NO=%s"
                    cur.execute(q15, (up_age, rn,))
                    print("\nAGE UPDATED SUCCESSFULLY")
                    
                elif(choice == 5):
                    up_dept = input("ENTER DEPARTMENT NAME :")
                    q8 = "UPDATE STUDENT1 SET DEPARTMENT=%s where ROLL_NO=%s"
                    cur.execute(q8, (up_dept, rn,))
                    print("\nDEPARTMENT UPDATED SUCCESSFULLY")

                elif(choice == 6):
                    up_computer = int(input("ENTER MARKS IN COMPUTER :"))
                    q9 = "UPDATE RESULT1 SET COMPUTER=%s where ROLL_NO=%s"
                    cur.execute(q9, (up_computer, rn,))
                    print("\nMARKS IN COMPUTER UPDATED SUCCESSFULLY")

                elif(choice == 7):
                    up_math = int(input("ENTER MARKS IN MATH :"))
                    q10 = "UPDATE RESULT1 SET MATH=%s where ROLL_NO=%s"
                    cur.execute(q10, (up_math, rn,))
                    print("\nMARKS IN MATH UPDATED SUCCESSFULLY")

                elif(choice == 8):
                    up_physics = int(input("ENTER MARKS IN PHYSICS :"))
                    q11 = "UPDATE RESULT1 SET PHYSICS=%s where ROLL_NO=%s"
                    cur.execute(q11, (up_physics, rn,))
                    print("\nMARKS IN PHYSICS UPDATED SUCCESSFULLY")

                elif(choice == 9):
                    up_chemistry = int(input("ENTER MARKS IN CHEMISTRY :"))
                    q12 = "UPDATE RESULT1 SET CHEMISTRY=%s where ROLL_NO=%s"
                    cur.execute(q12, (up_chemistry, rn,))
                    print("\nMARKS IN CHEMISTRY UPDATED SUCCESSFULLY")

                elif(choice == 10):
                    up_english = int(input("ENTER MARKS IN ENGLISH :"))
                    q13 = "UPDATE RESULT1 SET ENGLISH=%s  where ROLL_NO=%s"
                    cur.execute(q13, (up_english, rn,))
                    print("\nMARKS IN ENGLISH UPDATED SUCCESSFULLY")

                elif(choice == 11):
                    up_exam =input("ENTER EXAMINATION NAME :")
                    q14 = "UPDATE RESULT1 SET EXAMINATION=%s where ROLL_NO=%s"
                    cur.execute(q14, (up_exam, rn,))
                    print("\nEXAMINATION NAME UPDATED SUCCESSFULLY")
                else:
                    print("\nINVALID CHOICE\nCHOOSE AGAIN\n")
                    ch="y"
                    u+=1
                conn.commit()
                if u==1:
                    ch=input("\nWANT TO UPDATE MORE RECORDS ? (Y/N): ")
    if u==0:
        print("\nTHIS ROLL NUMBER DOES NOT EXISTS IN RECORD")
        print("\n1. INSERT THIS INTO DATABASE\n2. BACK TO ADMIN MODE")
        sel=int(input("\nENTER CHOICE : "))
        if sel==1:
            insert_data()
        else:
            admin()

def delete_data():
    ch="y"
    while(ch=="y" or ch=="Y"):
        d=0
        rn = int(input("\nENTER THE STUDENT ROLL NUMBER TO DELETE RECORD:"))
        q0 = "SELECT * FROM STUDENT1 where ROLL_NO=%s"
        cur.execute(q0, (rn,))
        a=cur.fetchall()
        for row in a:
            if(rn == row[0]):
                q3 = "delete from RESULT1 where ROLL_NO=%s"
                cur.execute(q3, (rn,))
                q4 = "delete from STUDENT1 where ROLL_NO=%s"
                cur.execute(q4, (rn,))
                print("\nRECORD DELETED SUCCESSFULLY")
                
                d=1

                ch=input("\nWANT TO DELETE MORE RECORDS ? (Y/N) : ")
        if d==0:
            print("\nNO SUCH RECORD EXISTS IN THE DATABASE")
            admin()
    conn.commit()    
def user():
    ch="y"
    while ch=="y" or ch=="Y":
        v=0
        rn=int(input("\nENTER THE ROLL NO :"))
        q1 = "SELECT * FROM STUDENT1 where ROLL_NO=%s"
        cur.execute(q1, (rn,))
        a=cur.fetchall()
        for row in a:
            if(rn == row[0]):
                print("\nROLL NUMBER  :", row[0])
                print("STUDENT NAME :", row[1])
                print("FATHER NAME:", row[2])
                print("PHONE NUMBER :", row[3])
                print("STUDENT AGE :", row[4])
                print("DEPARTMENT :", row[5])
                v=1
            else:
                break    
        q2 = "SELECT * FROM RESULT1 where ROLL_NO=%s"
        cur.execute(q2, (rn,))
        b=cur.fetchall()
        for row1 in b:
            if(rn==row1[0]):
                print("\nEXAMINATION NAME :", row1[1])
                print("MARKS IN COMPUTER :", row1[2])
                print("MARKS IN MATH :", row1[3])
                print("MARKS IN PHYSICS :", row1[4])
                print("MARKS IN CHEMISTRY :", row1[5])
                print("MARKS IN ENGLISH :", row1[6])
                v=2
            else:
                break
        if v!=2:
            print("\nTHERE IS NO SUCH RECORD")
            sel=int(input("\n1.VIEW ANOTHER\n2.EXIT\nENTER CHOICE : "))
            if sel==1:
                ch="y"
            elif sel==2:
                break
        else:
            ch=input("\nWANT TO VIEW ANOTHER RECORD ? (Y/N): ")
    conn.commit()
def login():
    username=input("\nENTER THE USERNAME :")
    if(username=="Admin" or username=="admin" or username=="ADMIN"):
        password=input("ENTER THE PASSWORD :")
        if(password=="12345"):
            print("\nLOGIN SUCCESSFUL")
            admin()
        else:
            print("\nINVALID CREDENTIALS")
            login()
    else:
        print("\nINVALID CREDENTIALS")
        login()

def view():
    q1 = "SELECT * FROM STUDENT1"
    cur.execute(q1)
    a=cur.fetchall()
    print("\n........STUDENT TABLE........")
    for row in a:
            print("\n\nROLL NUMBER  :", row[0])
            print("STUDENT NAME :", row[1])
            print("FATHER NAME:", row[2])
            print("PHONE NUMBER :", row[3])
            print("STUDENT AGE :", row[4])
            print("DEPARTMENT :", row[5])    
    q2 = "SELECT * FROM RESULT1"
    cur.execute(q2)
    b=cur.fetchall()
    print("\n........RESULT TABLE........")
    for row1 in b:
            print("\n\nROLL NUMBER  :", row1[0])
            print("EXAMINATION NAME :", row1[1])
            print("MARKS IN COMPUTER :", row1[2])
            print("MARKS IN MATH :", row1[3])
            print("MARKS IN PHYSICS :", row1[4])
            print("MARKS IN CHEMISTRY :", row1[5])
            print("MARKS IN ENGLISH :", row1[6])    

def admin():
    ch="y"
    while(ch=="y" or ch=="Y"):

        print("\n1. INSERT NEW RECORD IN DATABASE")
        print("2. UPDATE RECORD IN DATABASE")
        print("3. DELETE RECORD FROM DATABASE")
        print("4. SHOW DATABASE")
        print("5. EXIT")
        choice = int(input("\nENTER YOUR CHOICE :"))
        if (choice==1):
            insert_data()
        elif (choice== 2):
            update_data()
        elif (choice==3):
            delete_data()
        elif(choice==4):
            view()   
        elif(choice==5):
            cur.close()
        else:
            print("\nPLEASE ENTER THE VALID CHOICE")
            admin()
        ch=input("\nWANT TO CONTINUE TO ADMIN MODE ?(Y/N) : ")
    
        
#menu
ch="y"
while(ch=="y" or ch=="Y"):
        print("\n\n----------STUDENT RECORDS SYSTEM----------")
        print("\n\n\n1. ADMINISTRATION MODE")
        print("2. USER MODE")
        print("3. EXIT")
        choice=int(input("\nENTER YOUR CHOICE :"))
        if(choice == 1):
                login()
                ch="n"
        elif(choice == 2):
                user()
                ch="n"
        elif(choice == 3):
            cur.close()
            break
        else:
            print("\nINVALID CHOICE")
cur.close()
