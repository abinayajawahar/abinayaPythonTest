from uuid import NAMESPACE_X500
import mysql.connector
from mysql.connector import Error
connection=mysql.connector.connect(host="localhost",user="root",database="atm_db",password="root")


print("welcome to atm")
n=int(input("press 1 for login & 0 for register:"))
password=""
myname=""
depo=""
id=""
if n == 0:
     name=input("enter name:")
     accn=int(input("enter account no:"))
     t=int(input("enter starting amount u want to deposite"))
     pw=int(input("set ur  password:"))
     
     
     
     myname=name
     password=pw
     depo=t
     id=accn
     val=(myname,password,depo,id)
     
     sql="insert into atm_reg(my_name,pass_word, de_po,i_d) values (%s,%s,%s,%s)"
     mycursor= connection.cursor()
     
     mycursor.execute(sql,val) 
     connection.commit() 
     
     
if n == 1:
         info=int(input("enter ur id:"))
         passw=int(input("enter password:"))
         mycursor=connection.cursor()
         mycursor.execute("""select * from atm_reg where i_d='%s'"""% (info))
         row=mycursor.fetchone()
         if mycursor.rowcount==1:
             
             mycursor.execute("""select * from atm_reg where pass_word='%s'"""% (passw))
             row=mycursor.fetchone()
             if mycursor.rowcount==1:
                 print("login successful")
                 d=int(input("enter 1 for withdrawl or 0 for deposite & 3 for exit:"))
                 if d == 1:
                    a=int(input("how much u want to withdrawl:"))
                    mycursor.execute("""select de_po from atm_reg where pass_word='%s'"""% (passw))
                    col=mycursor.fetchone() 
                    x=list(col)
                    for i in x:
                        z=(int(i))
                        c=z-a
                        mycursor.execute("update atm_reg set de_po='%s'"%(c,passw))
                        
                 if d == 0:
                     a=int(input("how much u want to deposite:"))
                     mycursor.execute("""select de_po from atm_reg where pass_word='%s'""" %(passw))
                     col=mycursor.fetchone()
                     for i in x:
                         z=(int(i))
                         c=z+a
                         mycursor.execute("update atm_reg set de_po='%S'"%(c,passw))
                 if d == 3:
                     exit(0)
                 else:
                     print("invalid password")
                 
         else:
            print("account doesn't exist")
            connection.commit()                                         
     