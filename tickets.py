def __init__(): #"function definition"
       no_ofac1stclass=0 
       total=0
       no_ofac2ndclass=0
       no_ofac3rdclass=0
       no_ofsleeper=0
       no_oftickets=0
       name=""
       age=""
       resno=0
       status="" #"function body"

def display(): #"to display PNR status"
       import train as tr
       import time
       import random
       import os
       import mysql.connector
       mycon=mysql.connector.connect(host="localhost",user="root",passwd="dell",database="railways")
       cursor=mycon.cursor()
       cursor.execute("SELECT * FROM tickets")
       data=cursor.fetchone()
       name,age,PNRno,type_ofclass,status,booked_seats=data[0],int(data[1]),int(data[2]),data[3],data[4],int(data[5])
       f=0
       n=int(input("ENTER PNR NUMBER :"))
       print("\n\n")
       print("FETCHING DATA..".center(80))
       time.sleep(1) #"Time module used"
       print('PLEASE WAIT...!!'.center(80))
       time.sleep(1)
       os.system('cls')  #"os module used"
       
       if(n==PNRno):
            f=1
            print("="*80)
            print("PNR STATUS".center(80))
            print ("="*80)
            print("PASSENGER'S NAME:",name)
            print("PASSENGER'S AGE:",age)
            print("PNR NO:",PNRno)
            print("TYPE_OFCLASS:",type_ofclass)
            print("STATUS:",status)
            print("NO OF SEATS BOOKED:",booked_seats)
            mycon.close()
            input("PRESS ENTER TO GO TO BACK MENU".center(80))
       if (f==0):
               print("WRONG PNR NUMBER...!")#"if PNRno doesn't matches "
               input("PRESS ENTER TO GO TO BACK MENU".center(80))

def pending(resno,no_oftickets,x):#"if ticket in waiting list"
       import time
       status="WAITING LIST"
       print ("PNR NUMBER :",resno)
       time.sleep(1.2)
       print ("STATUS=",abs(x),"seat(s) on",status)
       print ("NO OF SEATS BOOKED : ",no_oftickets) 
       input("PRESS ENTER TO GO TO BACK MENU".center(80))

def confirmation(resno):  #"if ticket comfirmed"     
       import time
       status="CONFIRMED" 
       print ("PNR NUMBER",resno)
       time.sleep(1.2)
       print("STATUS=",status)
       input("PRESS ENTER TO GO TO BACK MENU".center(80))
       return status 

def cancellation():
       import time
       import os
       import pickle
       import mysql.connector
       mycon=mysql.connector.connect(host="localhost",user="root",passwd="dell",database="railways")
       cursor=mycon.cursor()
       cursor.execute("SELECT * FROM tickets") 
       data=cursor.fetchone()
       name,age,PNRno,type_ofclass,status,booked_seats=data[0],int(data[1]),int(data[2]),data[3],data[4],int(data[5])
       
       r=int(input("ENTER PNR NUMBER :"))  
       
       if(r==PNRno):
              cursor.execute("DROP table IF EXISTS tickets;") 
              mycon.commit()
              mycon.close()
              print("TICKET CANCELLED")
       else:
              print("NO SUCH RESERVATION NUMBER FOUND")
              time.sleep(2)                                                                                 
              os.system("cls")
                                                                                  
def reservation():
       import mysql.connector
       import train as tr
       import time
       import random
       import os
       train_no=int(input("ENTER THE TRAIN NO:"))
       f=0
       mycon=mysql.connector.connect(host="localhost",user="root",passwd="dell",database="railways")
       cursor=mycon.cursor()
       cursor.execute("SELECT * FROM trdetails")
       data=cursor.fetchone()#"train data imported"
       n=data[0]
       no_of1stACclass=int(data[2])
       no_of2ndACclass=int(data[3])
       no_of3rdACclass=int(data[4])
       no_ofsleeperclass=int(data[5])
       if(train_no==n):
          print("TRAIN NAME IS :",data[1])
          f=1   
          print("-"*80)  
          if(f==1):
            cursor.execute("create table tickets (name varchar(50),age integer,PNRno integer,type_ofclass varchar(50),status varchar(30),booked_seats integer);")
            mycon.commit()
            name=input("ENTER THE PASSENGER'S NAME: ")
            age=int(input("PASSENGER'S AGE: "))
            print("\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN:- ")
            print("1.AC FIRST CLASS")
            print("2.AC SECOND CLASS")
            print("3.AC THIRD CLASS")
            print("4.SLEEPER CLASS")
            c=int(input("\t\t\tENTER YOUR CHOICE="))
            os.system("cls")
            amt1=0            
            if(c==1): #"for ac 1st class"
                   no_oftickets=int(input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED :"))
                   for i in range(1,no_oftickets+1):
                      amt1=1000*no_oftickets
                   print("PROCESSING..",time.sleep(0.5))
                   print(".",time.sleep(0.3))
                   print(".")
                   time.sleep(2)
                   os.system("cls")
                   print ("TOTAL AMOUNT TO BE PAID=",amt1)
                   resno=random.randint(1000,2546) 
                   x=no_of1stACclass-no_oftickets
                   if(x>0):                          
                      status=confirmation(resno)#"function calling"
                      query="INSERT INTO tickets(name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"AC FIRST CLASS","COMFIRMED",no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                   else:
                      status=pending(resno,no_oftickets,x)
                      query="INSERT INTO tickets(name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"AC FIRST CLASS","WAITING LIST",no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                                       
            elif(c==2):#"for ac 2nd class"
                   no_oftickets=int(input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED : ")) 
                   for i in range(1,no_oftickets+1):  
                      amtl=900*no_oftickets
                   print("PROCESSING..",time.sleep(0.5))
                   print(".",time.sleep(0.3))
                   print (".",time.sleep(2))
                   os.system("cls")
                   print("TOTAL AMOUNT TO BE PAID= ",amtl)
                   resno=random.randint(1000,2546)
                   
                   x=no_of2ndACclass-no_oftickets
                   if(x>0):                          
                      status=confirmation(resno)#"function calling"
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"AC SECOND CLASS",status,no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                      
                   else:
                      status=pending(resno,no_oftickets,x)
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"AC SECOND CLASS","WAITING LIST",no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                      
                         
            elif(c==3):#"for ac 3rd class"
                    no_oftickets=int(input("ENTER NO OF THIRD CLASS AC SEATS TO BE BOOKED : "))
                    for i in range(1,no_oftickets+1):  
                        amtl=800*no_oftickets
                    print("PROCESSING..",time.sleep(0.5))
                    print(".",time.sleep(0.3))
                    print (".")
                    time.sleep(2)
                    os.system("cls")
                    print("TOTAL AMOUNT TO BE PAID= ",amtl)
                    resno=random.randint(1000,2546)
                    
                    x=no_of3rdACclass-no_oftickets
                    if(x>0):                          
                      status=confirmation(resno)#"function calling"
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"THIRD CLASS AC",status,no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                      
                    else:
                      status=pending(resno,no_oftickets,x)
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"THIRD CLASS AC","WAITING LIST",no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                      
                           
            elif(c==4):#"for sleeper class"
                 no_oftickets=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED : "))
                 for i in range(1,no_oftickets+1):  
                   amtl=550*no_oftickets
                 print("PROCESSING..",time.sleep(0.5))
                 print(".",time.sleep(0.3))
                 print (".")
                 time.sleep(2)
                 os.system("cls")
                 print("TOTAL AMOUNT TO BE PAID= ",amtl)
                 resno=random.randint(1000,2546)
                 x=no_ofsleeperclass-no_oftickets
                 if(x>0):                          
                      status=confirmation(resno)#"function calling"
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"SLEEPER CLASS",status,no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                      
                 else:
                      status=pending(resno,no_oftickets,x)
                      query="INSERT INTO tickets (name,age,PNRno,type_ofclass,status,booked_seats) VALUES('{}',{},{},'{}','{}',{})".format(name,age,resno,"SLEEPER CLASS","WAITING LIST",no_oftickets)
                      cursor.execute(query)
                      mycon.commit()
                      mycon.close()
                           
            else:
                 print("Please Enter valid choice number") #"for no. greater than 4" 
       if(f==0):#"for wrong train no."
           time.sleep(2)
           print("\n\n\n\n\n\n\t\t\t\t NO SUCH TRAINS FOUND !!")
           time.sleep(2)

