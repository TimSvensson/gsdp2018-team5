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
    display_sub_bar2()
    choice = ''
    while choice != "q":    

    # Let users know what they can do.
        print("\n[1] OPTION1")
        print("[2] OPTION2")
        print("[3] OPTION3")
        print("[q] Go back")
    
        choice = raw_input("Please select an option above? ")
        
        # Respond to the user's choice.
        if choice == '1':
            print("\nOPTION 1")
            
        elif choice == '2':
            print("\nOPTION 2")
            
        elif choice == '3':
            print("\nOPTION 3")
        elif choice == 'q':
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")    



def ware_menu():
    
    os.system('clear')
    display_title_bar()
    display_sub_bar1()
    choice = ''
    temp = ''
    hum = ''
    while choice != "q":    

    # Let users know what they can do.
        print("\n[1] Show a map of the Warehouse")
        print("[2] Show sensor data")
        print("[3] Where is the robot right now?")
        print("[q] Go back")
    
        choice = raw_input("Please select an option above? ")
        
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
    
        choice = raw_input("Please select an option above? ")
        
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