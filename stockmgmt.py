#to connect mysql database to python
import mysql.connector as sql

#connecting sql and python
mycon=sql.connect(host="localhost",user="root",passwd="Super@30",database="stockmgmt")
cursor=mycon.cursor()

#to display data in tabular format
from prettytable import PrettyTable

#importing date
from datetime import date
today=date.today()

while True:
    breakout = False
    login_who=int(input("Login Who: \n1.Admin\n2.Customer\n3.Supplier "))
    addTableHead=1
    while True:
        if login_who == 1:
            admin_login = input("Enter Admin Username : ")
            admin_pswd  = input("Enter Password : ")
            # Use placeholders in the SQL query
            query = "SELECT COUNT(*) FROM admin WHERE id=%s AND pswd=%s"
            params = (admin_login, admin_pswd)
            cursor.execute(query, params)
            valid = cursor.fetchone()[0]
            while valid:
                what_you_want_do=int(input("What you want to do:\n1.Check Stock\n2.Order Stock\n3.Exit "))
                if what_you_want_do == 1:

                    #print_stock

                    print("Existing stock")
                    cursor.execute("select * from stock")
                    data=cursor.fetchall()
                    table=PrettyTable(['Sno','PID','PName','Price','Quantity'])
                    sno=1
                    for row in data:
                        a,b,c,d=row
                        l=[sno,a,b,c,d]
                        table.add_row(l)
                        sno+=1
                    print(table)

                elif what_you_want_do == 2:

                    #order_stock
                    pid=int(input("Enter PID to Order :"))
                    quantity=int(input("Enter Quantity :"))
                    cursor.execute("insert into orders values({},{})".format(pid,quantity))       #updating the quantity in database 
                    mycon.commit()
                    print("Order Placed Successfully")

                elif what_you_want_do == 3:
                    #print("Wrong Choice")
                    breakout = True
                    break
                else:
                    print("wrong choice")
                    breakout = True
                    break
            if breakout == True:
                breakout = False
                break
                    
            else:
                print("Invalid User\n")
        elif login_who == 2:
            cust_login = input("Enter Customer Username : ")
            cust_pswd  = input("Enter Password : ")
            # Use placeholders in the SQL query
            query = "SELECT COUNT(*) FROM customer WHERE id=%s AND pswd=%s"
            params = (cust_login, cust_pswd)
            cursor.execute(query, params)
            valid = cursor.fetchone()[0]
            if valid == True:
                total_amt = 0
                #print stock
                print("Existing stock")
                cursor.execute("select * from stock")
                data=cursor.fetchall()
                table=PrettyTable(['Sno','PID','PName','Price','Quantity'])
                sno=1
                for row in data:
                    a,b,c,d=row
                    l=[sno,a,b,c,d]
                    table.add_row(l)
                    sno+=1;
                print(table)
                while True:
                    table=PrettyTable(['Sno','PID','PName','Price','Quantity'])       #creating table format
                    order_placed = False
                    enter_item_code = input("Enter PID to Add Cart || Enter F to Finish :")
                    if enter_item_code != 'F':
                        order_placed = True
                        cursor.execute("select * from stock where pid=%s",(int(enter_item_code),))                                          #executing the command in mysql database
                        data=cursor.fetchall()                                                                              #fetching the output from cursor
                        for row in data:
                            sno=1
                            a,b,c,d=row
                            l=[sno,a,b,c,d]
                            table.add_row(l)
                       
                        print(table) 
                        
                        quantity=int(input("Enter Quantity :"))
                        remaining_in_stock = d - quantity
                        cursor.execute("UPDATE Stock SET Quantity={} where pid={}".format(remaining_in_stock,int(enter_item_code)))
                        mycon.commit()
                        if addTableHead == 1:
                            checkout_table=PrettyTable(['Sno','PID','PName','Price','Quantity'])
                        addTableHead+=1
                        tablerow = [addTableHead-1,a,b,c*quantity,quantity]
                        total_amt += c*quantity
                        checkout_table.add_row(tablerow)
                    else:

                        #Payment
                        breakout=True
                        if order_placed == True:
                            print(checkout_table)
                            print("Total Amount to be Paid :",total_amt)
                            total_amt=0
                        break
                if breakout == True:
                    breakout = False
                    break
            
            else:
                print("Invalid User\n")
        else:
            
            ssup_login = input("Enter Supplier Username : ")
            ssup_pswd  = input("Enter Password : ")
            # Use placeholders in the SQL query
            query = "SELECT COUNT(*) FROM supplier WHERE id=%s AND pswd=%s"
            params = (ssup_login, ssup_pswd)
            cursor.execute(query, params)
            valid = cursor.fetchone()[0]
            if valid == True:
                print("Remaining Orders")
                cursor.execute("select * from orders")
                data=cursor.fetchall()
                table=PrettyTable(['Sno','PID','Quantity'])
                sno=1
                for row in data:
                    a,b=row
                    l=[sno,a,b]
                    table.add_row(l)
                    sno+=1;
                print(table)

                supply=input("Supply y or no n :")
                if supply == 'n':
                    #breakout = True
                    break
                else:
                    enter_item_code = int(input("Enter PID to Supply :"))
                    cursor.execute("select * from stock where pid=%s",(int(enter_item_code),))                                          #executing the command in mysql database
                    old_data=cursor.fetchone()
                    olda,olb,oldc,oldd = old_data
                    cursor.execute("select * from orders where pid=%s",(int(enter_item_code),))                                          #executing the command in mysql database
                    data=cursor.fetchone()
                    a,b=data
                    cursor.execute("UPDATE Stock SET Quantity={} where pid={}".format(b+oldd,enter_item_code))
                    mycon.commit()
                    cursor.execute("Delete from orders where pid={}".format(enter_item_code,))
                    mycon.commit()
            else:
                print("Invalid User\n")
                break
