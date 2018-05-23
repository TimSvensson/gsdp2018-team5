import os, sys
#!/usr/bin/python
# -*- coding: unicode -*-



def display_title_bar():

    os.system('clear')

    # Display a title bar.
    print("\t*****************************************************")
    print("\t***  Welcome to our Warehouse Management System!  ***")
    print("\t*****************************************************")

def display_sub_bar1():

    print("\t\t****************************")
    print("\t\t***  CREATE A JOB MENU!  ***")
    print("\t\t****************************")


def display_sub_bar2():

    print("\t\t****************************")
    print("\t\t****  WAREHOUSE MENU!  *****")
    print("\t\t****************************")

def is_valid_char(c):
    if c in ['a','b','c','d','A','B','C','D']:
      
        return True
    else:
        print("\nPlease choose between the character [A,B,C,D]")
        return False


def is_job_done(src, dst):
    if (src != '' and dst != ''):
        return True
    else:
        return False

def display_ware():

    print("\n     In") 
    print("++++++|+++++++")
    print("+A----|-----B+")
    print("++++++|+++++++")
    print("+C----|-----D+")
    print("++++++|++++++")
    print("     Out")


def create_menu():

    os.system('clear')
    
    display_title_bar()
    display_sub_bar1()
    #init of variables
    choice = ''
    source = ''
    destination = ''

    while choice != "q":    

    # Let users know what they can do.
        print("\n[1] GET FROM: " + source.upper())
        print("[2] DROP AT: " + destination.upper())
        
        #if source and destination is chosed then show option excecute 
        if (is_job_done(source, destination)):
            print("[3] EXCECUTE JOB ORDER ")
        print("[q] Cancel")
        choice = input("Please select an option above? ")

        # Respond to the user's choice.
        if choice == '1':
            while not is_valid_char(source):
                source = input("Select source of the package: ")

        elif choice == '2':
            while not is_valid_char(destination):
                destination = input("Select the destination for the package:  ")
            
        elif choice == '3':
            print("\nCONGRATULATIONS YOU MADE A JOB ORDER")
            source = ''
            destination = ''

        elif choice == 'q':
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")    



def ware_menu():
    
    os.system('clear')
    display_title_bar()
    display_sub_bar2()
    
    #init of variables
    choice = ''
    temp = ''
    hum = ''

    while choice != "q":    

    # Let users know what they can do.
        print("\n[1] Show a map of the Warehouse")
        print("[2] Show sensor data")
        print("[3] Where is the robot right now?")
        print("[q] Go back")
    
        choice = input("Please select an option above? ")
        
        # Respond to the user's choice.
        if choice == '1':
            display_ware()
            
        elif choice == '2':
            print("\nHere we will present the sensor data of Humidity and Temperature")
            print("Temperature: " + temp)
            print("Humidity : " + hum)
            
        elif choice == '3':
            print("\nLocation of the robot atm")
        elif choice == 'q':
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")    



def main_menu():
    display_title_bar()
    choice = ''

    while choice != "q":    

    # Let users know what they can do.
        print("\n[1] Inspect the Warehouse")
        print("[2] Create a job")
        print("[q] Quit")
        
        choice = input("Please select an option above? ")
        
        # Respond to the user's choice.
        if choice == '1':
            ware_menu()
            
        elif choice == '2':
            create_menu()
        elif choice == 'q':
            print("\nThanks for visiting our System. Bye.")
        else:
            print("\nI didn't understand that choice.\n")



main_menu()