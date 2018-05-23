import os, sys
#!/usr/bin/python
# -*- coding: unicode -*-



def display_title_bar():
    os.system('clear')
    # Display a title bar.
    print("\t*****************************************************")
    print("\t***  Welcome to our Warehouse Management System!  ***")
    print("\t*****************************************************")

def display_job_bar():
    print("\t\t****************************")
    print("\t\t***  CREATE A JOB MENU!  ***")
    print("\t\t****************************")


def display_ware_bar():
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

    print("\n     End")
    print("   ───▄───")
    print("      │") 
    print("╔═════│══════╗")
    print("║     │      ║")
    print("║D■───█────■C║")
    print("║     │      ║")
    print("╠═════│══════╣")
    print("║     │      ║")
    print("║B■───█────■A║")
    print("║     │      ║")
    print("╚═════│══════╝ ")
    print("      │") 
    print("   ───▀───")
    print("    Start")


def create_menu():
    #clear terminal screen
    os.system('clear')   
    display_title_bar()
    display_job_bar()
    #init of variables
    choice = ''
    source = ''
    destination = ''

    while choice != "q":    
    # Let users know what they can do.
        print("\n----------------------------")
        print("[1] PICK UP PACKAGE AT LOCATION: " + source.upper())
        print("[2] DELIVER PACKAGE AT LOCATION: " + destination.upper())
        
        #if source and destination is chosed then show option excecute 
        if (is_job_done(source, destination)):
            print("[3] EXCECUTE JOB ORDER")
        print("[q] Cancel")
        print("----------------------------")
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
    #clear terminal screen
    os.system('clear')
    display_title_bar()
    display_ware_bar()
    
    #init of variables
    choice = ''
    temp = ''
    hum = ''

    while choice != "q":    

    # Let users know what they can do.

        print("\n----------------------------")
        print("[1] Show a map of the Warehouse")
        print("[2] Show sensor data")
        print("[3] Location of the robot?")
        print("[q] Go back")
        print("----------------------------")
    
        choice = input("Please select an option above? ")
        
        # Respond to the user's choice.
        if choice == '1':
            display_ware()
            
        elif choice == '2':
            print("\nHere we will present the sensor data of Humidity and Temperature")
            print("Temperature: " + temp)
            print("Humidity : " + hum)
            
        elif choice == '3':
            print("\nThe location of the robot is currently unknown")

        elif choice == 'q':
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")    



def main_menu():
    display_title_bar()
    choice = ''

    while choice != "q":    

    # Let users know what they can do.
        print("\n----------------------------")
        print("[1] Inspect the Warehouse")
        print("[2] Create a job")
        print("[q] Quit")
        print("----------------------------")

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