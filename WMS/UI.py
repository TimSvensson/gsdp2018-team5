import os, sys

cu_path = os.path.dirname(os.path.abspath(__file__)) + '/../client-server'
print(cu_path)
sys.path.insert(0, cu_path)

import util, client
#!/usr/bin/python
# -*- coding: unicode -*-

# con - the CONnection to the server
con = None

ard_sensors = {util._ard:True, util._hum:'', util._temp:''}
wh_items    = {util._wh:True, 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
ev3_status  = {util._ev3_s:True, util._stat:'', util._pos:''}

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
        update()
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
            con.send(util._to_ev3, {_ev3_j:True, _from:source, _to:destination})
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

        update()

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
            print("Temperature: " + ard_sensors[util._temp])
            print("Humidity : " + ard_sensors[util._hum])
            
        elif choice == '3':
            print("\nLocation {]".format(ev3_status[util._pos]))
        elif choice == 'q':
            main_menu()
        else:
            print("\nI didn't understand that choice.\n")    



def main_menu():
    display_title_bar()
    choice = ''

    while choice != "q":

        update()

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


def update():
    recipient = util._db
    db_fetch = {util._db_f: True} #database fetch
    con.send(recipient, db_fetch)
    resp = con.read()

    if util._ev3_s in resp:
        ev3_status[util._pos] = resp[util._pos]
        ev3_status[util._stat] = resp[util._stat]
    if util._wh in resp:
        wh_items['a'] = resp['a']
        wh_items['b'] = resp['b']
        wh_items['c'] = resp['c']
        wh_items['d'] = resp['d']
        wh_items['e'] = resp['e']
        wh_items['f'] = resp['f']
    if util._ard in resp:
        ard_sensors[util._temp] = resp[util._temp]
        ard_sensors[util._hum] = resp[util._hum]

if __name__ == '__main__':
    HOST, PORT = sys.argv[1], int(sys.argv[2])
    con = client.client(HOST,PORT,util._ui)
    con.connect()
    main_menu()
    con.disconnect()

