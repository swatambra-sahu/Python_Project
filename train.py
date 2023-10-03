def __init__():#"Declaration of module through _init_"
             trainno=0
             no_ofaclstclass=0
             no_ofac2ndclass=0
             no_ofac3rdclass=0
             no_ofsleeper=0
             totalseats=0
             trainname=""
             startingpt=""
             destination=""
    
def getinput():
             import os    
             import mysql.connector#"importing module required for MySQL and Python connection"
             mycon=mysql.connector.connect(host="localhost",user="root",passwd="dell",database="railways")#"using database railways"
             cursor=mycon.cursor()
             cursor.execute("create table trdetails (trainno integer,trainname varchar(50), no_ofac1stclass integer, no_ofac2ndclass integer,no_ofac3rdclass integer,no_ofsleeper integer,startingpt varchar(50),destination varchar(50));")
             #"creating table in MySQL through Python"
             print("="*80)
             print("\t\t\t ENTER THE TRAIN DETAILS")
             print("="*80)
             trainname=input("ENTER THE TRAIN NAME : ").upper()
             trainno=int(input("ENTER THE TRAIN NUMBER: "))
             no_ofac1stclass=int(input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED :"))
             no_ofac2ndclass=int(input("ENTER NO OF AC SECOND CLASS SEATS TO BE RESERVED :"))
             no_ofac3rdclass=int(input("ENTER NO OF AC THIRD CLASS SEATS TO BE RESERVED : "))
             no_ofsleeper=int(input("ENTER NO OF SLEEPER CLASS SEATS TO BE RESERVED:"))
             startingpt=input("ENTER THE STARTING POINT :")
             destination=input("ENTER THE DESTINATION POINT:")
             #"input train details from user"
             query="INSERT INTO trdetails(trainno,trainname, no_ofac1stclass, no_ofac2ndclass,no_ofac3rdclass,no_ofsleeper,startingpt,destination) VALUES({},'{}',{},{},{},{},'{}','{}')".format(trainno,trainname, no_ofac1stclass, no_ofac2ndclass,no_ofac3rdclass,no_ofsleeper,startingpt,destination)
             #"inserting data in table in MySQL through Python"
             cursor.execute(query)
             mycon.commit()
             os.system('cls')
             mycon.close()

def output():
             import os
             import mysql.connector
             mycon=mysql.connector.connect(host="localhost",user="root",passwd="dell",database="railways")
             cursor=mycon.cursor() 
             cursor.execute("SELECT * FROM trdetails")
             data=cursor.fetchone()#"for fetching 1 data from database"
             print("*"*80)
             print("\t\t\t\tTRAIN DETAILS")
             print("*"*80)
             input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
             os.system('cls')
             print("="*80)                    
             print("THE TRAIN NUMBER IS : ",data[0])
             print("THE ENTERED TRAIN NAME IS :", data[1])
             print("NO_OF AC FIRST CLASS SEATS RESERVED ARE ",data[2])
             print("NO_OF AC SECOND CLASS SEATS RESERVED ARE:",data[3])
             print("NO_OF AC THIRD CLASS SEATS RESERVED ARE:",data[4])
             print("NO_OF SLEEPER CLASS SEATS RESERVED ARE :",data[5])
             print("STARTING POINT ENTERED IS:",data[6])
             print("DESTINATION POINT ENTERED IS: ",data[7])
             print("="*80)
             mycon.close()#"linking through MySQL closed"
             input("PRESS ENTER TO GO TO MAIN MENU")






                                          
