#main
from cmath import e
from secrets import choice
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="automobile_dealer"
)
mycursor=mydb.cursor()

print("\n\n         Welcome to Automobile Dealer Management Software        ")
while True:
    print("\n\n")
    mainchoice=int(input("1)DATA DISPLAY\n2)DATA ENTRY\n3)DATA DELETION\n4)EXIT\nENTER YOUR CHOICE: "))
    if mainchoice==1:
        service=int(input("1) SHOW AVAILABLE CAR BRANDS\n2) CAR DETAILS\n3) SHOW PRICE\n4) SHOW CUSTOMER DETAILS\n5) SHOW EMPLOYEE DETAILS\n6) SHOW INVOICE\n7) SHOW PAYMENT INFO\n8) EXIT\n9)RETURN HOMEPAGE\nENTER YOUR CHOICE: "))  
        if(service==1):
            query="SELECT * FROM BRAND"
            mycursor.execute(query)
            for x in mycursor:
                print(x)
        elif(service==2):
            choice=int(input("1)SEARCH BY BRAND_ID\n2)SEARCH BY BRAND NAME\n3)SEARCH BY FUEL TYPE\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter BRAND ID: ").split()))
                query="SELECT * FROM C_DETAILS WHERE BID = %s"     
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==2:
                choice1=list(map(str,input("Enter BRAND NAME: ").split()))
                query="SELECT * FROM C_DETAILS WHERE BRAND_NAME = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==3:
                choice1=list(map(str,input("Enter FUEL TYPE: ")))
                query="SELECT * FROM C_DETAILS WHERE FUEL = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==4:
                exit()
        elif(service==3):
            choice=int(input("1)SEARCH BY CAR_ID\n2)SEARCH BY BRAND ID\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="SELECT * FROM PRICE WHERE C_ID = %s"   
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==2:
                choice1=list(map(str,input("Enter BRAND ID: ").split()))
                query="SELECT * FROM PRICE WHERE BID = %s"     
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==3:
                exit()
        elif(service==4):
            choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
            query="SELECT * FROM CUSTOMER WHERE UID = %s"
            mycursor.execute(query,choice1)
            for x in mycursor:
                print(x)
        elif(service==5):
            choice=int(input("1)SEARCH BY EMPLOYEE ID\n2)SEARCH BY EMP SERVICE\n3)SEARCH BY NUMBER\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter EMPLOYEE ID: ").split()))
                query="SELECT * FROM EMPLOYEE WHERE E_ID = %s"     
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==2:
                choice1=list(map(str,input("Enter SERVICE: ").split()))
                query="SELECT * FROM EMPLOYEE WHERE SERVICE = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==3:
                choice1=list(map(str,input("Enter EMPLOYEE NUMBER: ").split()))
                query="SELECT * FROM EMPLOYEE WHERE NUMBER = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==4:
                exit()
        elif(service==6):
            choice=int(input("1)SEARCH BY INVOICE ID\n2)SEARCH BY CUSTOMER ID\n3)ALL RECORDS\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter INVOICE ID: ").split()))
                query="SELECT * FROM INVOICE WHERE INV_ID = %s"     
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==2:
                choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
                query="SELECT * FROM INVOICE WHERE UID = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==3:
                query="SELECT * FROM INVOICE"      
                mycursor.execute(query)
                for x in mycursor:
                    print(x)
            elif choice==4:
                exit()
        elif(service==7):
            choice=int(input("1)SEARCH BY PAYMENT ID\n2)SEARCH BY CUSTOMER ID\n3)SEARCH BY INVOICE ID\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==3:
                choice1=list(map(str,input("Enter INVOICE ID: ").split()))
                query="SELECT * FROM PAYMENT WHERE INV_ID = %s"     
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==2:
                choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
                query="SELECT * FROM PAYMENT WHERE UID = %s"      
                mycursor.execute(query,choice1)
                for x in mycursor:
                    print(x)
            elif choice==1:
                query="SELECT * FROM PAYMENT WHERE PID = %s"      
                mycursor.execute(query)
                for x in mycursor:
                    print(x)
            elif choice==4:
                exit()
        elif(service==8):
            exit()
        elif(service==9):
            continue
    elif mainchoice==2:
        service=int(input("1) ENTER CAR BRANDS\n2)ENTER CAR DETAILS\n3)ENTER CAR PRICE\n4)ENTER CUSTOMER DETAILS\n5) ENTER EMPLOYEE DETAILS\n6) CREATE INVOICE\n7) UPDATE PAYMENT INFO\n8) EXIT\nENTER YOUR CHOICE: "))
        if(service==1):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                bid=input("Enter BRAND ID: ")
                bname=input("Enter BRAND NAME: ")
                origin=input("Enter ORIGIN COUNTRY: ")
                quantity=int(input("Enter Total Quantity: "))
                finallist=(bid.upper(),bname.upper(),origin.upper(),quantity)
                query="INSERT INTO BRAND (BID, BRAND_NAME, ORIGIN, MODELS) VALUES (%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")
        elif(service==2):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                bid=input("Enter BRAND ID: ")
                bname=input("Enter BRAND NAME: ")
                cid=input("Enter CAR ID: ")
                cname=input("Enter CAR NAME: ")
                vari=input("Enter CAR VARIANT: ")
                eng=int(input("Enter ENGINE CAPACITY: "))
                scpc=int(input("Enter SEATING CAPACITY: "))
                f=input("Enter FUEL TYPE(P/D/E): ")            
                finallist=(bid.upper(),bname.upper(),cid.upper(),cname.upper(),vari.upper(),eng,scpc,f.upper())
                query="INSERT INTO C_DETAILS (BID, BRAND_NAME, C_ID, CAR_NAME, VARIANT, ENGINE_CAPACITY, SEATING_CAPACITY, FUEL) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")
        elif(service==3):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                prid=input("Enter PRICE ID: ")
                bid=input("Enter BRAND ID: ")
                cid=input("Enter CAR ID: ")
                price=int(input("Enter PRICE: "))       
                finallist=(prid.upper(),bid.upper(),cid.upper(),price)
                query="INSERT INTO PRICE (PR_ID, BID, C_ID, PRICE) VALUES (%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")
        elif(service==4):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                uid=input("Enter CUSTOMER ID: ")
                cname=input("Enter CAR NAME: ")
                add=input("Enter  ADDRESS: ")
                ph=input("Enter PHONE NUMBER: ")
                ser=input("Enter SERVICE: ")
                email=input("Enter EMAIL ID: ")
                cid=input("Enter CAR ID: ")
                eid=input("Enter ASSISTED EMPLOYEE ID: ")
                finallist=(uid.upper(),cname.upper(),add.upper(),ph,ser.upper(),email,cid.upper(),eid.upper())
                query="INSERT INTO CUSTOMER (UID,CNAME,ADDRESS,PNUMBER,SERVICE,EMAIL,C_ID,E_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")
        elif(service==5):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                eid=input("Enter EMPLOYEE ID: ")
                empname=input("Enter EMPLOYEE NAME: ")
                ser=input("Enter SERVICE: ")
                ph=input("Enter PHONE NUMBER: ")
                finallist=(eid.upper(),empname.upper(),ser.upper(),ph)
                query="INSERT INTO EMPLOYEE (E_ID,EMP_NAME,SERVICE,NUMBER) VALUES (%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")    
        elif(service==6):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                inid=input("Enter INVOICE ID: ")
                uid=input("Enter CUSTOMER ID: ")
                custname=input("Enter CUSTOMER NAME: ")
                ph=input("Enter PHONE NUMBER: ")
                trf=input("Enter TRANSACTION REFERENCE NO: ")
                cid=input("Enter CAR ID: ")
                finallist=(inid.upper(),uid.upper(),custname.upper(),ph,trf,cid)
                query="INSERT INTO INVOICE (INV_ID,UID,NAME,PNUMBER,TRANSACTION_REF,C_ID) VALUES (%s,%s,%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n") 
        elif(service==7):
            ctr=int(input("Enter Total Number of Entries: "))
            for i in range(ctr):
                inid=input("Enter INVOICE ID: ")
                pid=input("Enter PAYMENT ID: ")
                uid=input("Enter CUSTOMER ID: ")
                trf=input("Enter TRANSACTION REFERENCE NO: ")
                rmk=input("Enter REMARKS: ")
                finallist=(inid.upper(),pid.upper(),uid.upper(),trf,rmk.upper())
                query="INSERT INTO PAYMENT (INV_ID,PID,UID,TRANSACTION_REF,REMARKS) VALUES (%s,%s,%s,%s,%s);"
                mycursor.execute(query,finallist)
                mydb.commit()
                print(i+1,"RECORDS INSERTED\n\n")    
        elif(service==8):
            exit()  
        elif(service==9):
            continue
    elif mainchoice==3:
        service=int(input("1) DELETE AVAILABLE CAR BRANDS\n2)DELETE CAR DETAILS\n3)DELETE PRICES\n4)DELETE CUSTOMER DETAILS\n5)DELETE EMPLOYEE DETAILS\n6)DELETE INVOICE\n7)DELETE PAYMENT INFO\n8) EXIT\nENTER YOUR CHOICE: "))  
        if(service==1):
            choice=int(input("1)DELETE BY BRAND_ID\n2)DELETE BY BRAND NAME\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter BRAND ID: ").split()))
                query="DELETE FROM BRAND WHERE BID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter BRAND NAME: ").split()))
                query="DELETE FROM BRAND WHERE BRAND_NAME = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                exit()
        elif(service==2):
            choice=int(input("1)DELETE BY CAR ID\n2)DELETE BY BRAND NAME\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="DELETE FROM C_DETAILS WHERE C_ID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter BRAND NAME: ").split()))
                query="DELETE FROM C_DETAILS WHERE BRAND_NAME = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                exit()
        elif(service==3):
            choice=int(input("1)DELETE BY PRICE ID\n2)DELETE BY CAR ID\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter PRICE ID: ").split()))
                query="DELETE FROM PRICE WHERE PR_ID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="DELETE FROM PRICE WHERE C_ID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                exit()
        elif(service==4):
            choice=int(input("1)DELETE BY CUSTOMER ID\n2)DELETE BY CAR ID\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
                query="DELETE FROM CUSTOMER WHERE UID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="DELETE FROM CUSTOMER WHERE C_ID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                exit()
        elif(service==5):
            choice=int(input("1)DELETE BY EMPLOYEE ID\n2)DELETE BY PHONE NUMBER\n3)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter EMPLOYEE ID: ").split()))
                query="DELETE FROM EMPLOYEE WHERE E_ID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter PHONE NUMBER: ").split()))
                query="DELETE FROM EMPLOYEE WHERE NUMBER = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                exit()
        elif(service==6):
            choice=int(input("1)DELETE BY INVOICE ID\n2)DELETE BY CUSTOMER ID\n3)DELETE BY CAR ID\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter INVOICE ID: ").split()))
                query="DELETE FROM INVOICE WHERE INV_ID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
                query="DELETE FROM INVOICE WHERE UID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="DELETE FROM INVOICE WHERE C_ID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==4:
                exit()
        elif(service==7):
            choice=int(input("1)DELETE BY INVOICE ID\n2)DELETE BY CUSTOMER ID\n3)DELETE BY PAYMENT ID\n4)EXIT\nENTER YOUR CHOICE: "))
            if choice==1:
                choice1=list(map(str,input("Enter INVOICE ID: ").split()))
                query="DELETE FROM PAYMENT WHERE INV_ID = %s"     
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==2:
                choice1=list(map(str,input("Enter CUSTOMER ID: ").split()))
                query="DELETE FROM PAYMENT WHERE UID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==3:
                choice1=list(map(str,input("Enter CAR ID: ").split()))
                query="DELETE FROM PAYMENT WHERE PID = %s"      
                mycursor.execute(query,choice1)
                mydb.commit()
                print("STATEMENT EXECUTED!")
            elif choice==4:
                exit()
        elif(service==8):
            exit()
        elif(service==9):
            continue
    elif mainchoice==4:
        print("GoodBye!")
        break
