def menu():  #"Function declaration"
       print ("WELCOME TO INDIAN RAILWAY MANAGEMENT SYSTEM".center(80))#"Heading"
       while True:
             print("="*80)
             print("\t\t\t\t RAILWAY")#"Display menu for user"
             print("="*80)
             print("\t\t\t1. UPDATE TRAIN DETAILS.")
             print("\t\t\t2. TRAIN DETAILS. ")
             print("\t\t\t3. RESERVATION OF TICKETS.")
             print("\t\t\t4. CANCELLATION OF TICKETS.")
             print("\t\t\t5. DISPLAY PNR STATUS.")
             print("\t\t\t6. QUIT.")
             print("** -office use.")
             ch=int(input("\t\t\t ENTER YOUR CHOICE : "))
             os.system('cls')
             print("\n\n\n\n\n\n\r\t\t\t\t LOADING..")
             os.system('cls')
             if ch==1: #"UPDATE TRAIN DETAILS choice"

                    j="password"
                    r=input("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tENTER THE PASSWORD: ")
                    print("\n\n\n\n\n\n\r\t\t\t\t ")
                    os.system('cls')
                    if(j==r):

                           x='y'
                           while (x.lower()=='y'):                                 
                                  tr.getinput() #"Function calling from module train"                                 
                                  print("\n\n\n\n\n\n\n\n\n\n\n\t\t UPDATING TRAIN LIST PLEASE WAIT..",time.sleep(1))
                                  print (("."),time.sleep(0.5))
                                  print(("."), time.sleep(2))
                                  os.system('cls')
                                  print ("\n\n\n\n\n\n\n\n\n\n\n")
                                  x=input("\t\t DO YOU WANT TO ADD ANY MORE TRAINS DETAILS ?")
                                  os.system('cls')
                                  continue
                    elif(j!=r):

                             print("\n\n\n\n\n")
                             print("WRONG PASSWORD".center(80))
             elif ch==2:#"TRAIN DETAILS choice"
                    tr.output()                     
             elif ch==3:#"RESERVATION OF TICKETS choice"
                             print("="*80)
                             print("\t\t\tRESERVATION OF TICKETS")
                             print('='*80)
                             tick.reservation()
             elif ch==4:#"CANCELLATION OF TICKETS choice"
                             print("="*80)
                             print("\t\t\t\tCANCELLATION OF TICKETS")
                             print("="*80)
                             tick.cancellation()
             elif ch==5:#"DISPLAY PNR STATUS choice"
                             print ("="*80)
                             print("PNR STATUS".center(80))
                             print("="*80)
                             tick.display()
             elif ch==6:#"QUIT choice"
                             os.system('cls')          
                             print(" THANK YOU.....".center(80))
                             print("\n\t\t\t\tDONE BY:-")
                             print("\t\t\t\t MUSKAN SHARMA")
                             print("\t\t\t\t XII-A")
                             print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tLOADING",time.sleep(1))
                             print (".")
                             time.sleep(0.5)
                             print(".")
                             time.sleep(2)
                             os.system('cls')
                             quit()
             else:#"for no. greater than 6"
                    print("Please Enter valid choice number")
#MAIN CODE USED
#__main__

#"Importing module to be used in program"

import time
import random
import os
import tickets as tick
import train as tr

menu()#"Function calling"
