import sys
# addr ev3dev
# name 00:17:E9:F8:72:06
import bluetooth

serverMACAddress = '00:17:E9:F8:72:06'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

currentPos = 5
currentAction = 0

mapPos = ['Null', 'A', 'B', 'C', 'D', 'Start', 'End']
mapAc = ['Null', 'Do nothing', 'Pick Up', 'Put Down']
command = {}

def menu():
    done = False
    while not done:
        print("SIMPLE EV3-APP MENU:\n1.Set command for robot\n2.Show current command\n3.Apply command\n4.Quit")
        choice = input("Your choice: ")
        # try:
        choice = int(choice)
        if (choice > 0 and choice < 5):
            if (choice == 1):
                location()
                action()
            elif (choice == 2):
                show()
            elif (choice == 3):
                apply()
            else:
                print("Goodbye")
                done = True
        else:
            print("Invalid option")
        # except:
        #     print("Invalid option")


def location():
    global currentPos
    done = False
    while not done:
        print("Select location:\n1.A\n2.B\n3.C\n4.D\n5.Start\n6.End\n")
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if (choice > 0 and choice < 7):
                if (currentPos == choice):
                    showPos()
                    print("Same LOCATION cant be select twice in a row")
                else:
                    currentPos = choice
                    done = True
            else:
                print("Invalid Option !\n")
        except:
            print("Invalid Option!\n")
            done = False

def action():
    global command
    global currentAction
    done = False
    while not done:
        print("Select action:\n1.Nothing\n2.Pick Up\n3.Drop Down\n")
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if (choice > 0 and choice < 4):
                if (currentAction != 0 and currentAction == choice):
                    showAction()
                    print("Same ACTION cant be perform twice in a row!\n")
                else:
                    currentAction = choice
                    command[mapPos[currentPos]] = mapAc[currentAction]
                    done = True
            else:
                print ("Invalid Options!\n")
        except:
            print("Invalid Option!\n")
            done = False

def showPos():
    print ("The current position of the robot: ", mapPos[currentPos])

def showAction():
    print ("The current action of the robot: ", mapAc[currentAction])

def show():
    for location, action in command.items():
        print("Go to ", location, " : do ", action)
    print(str(command))

def apply():
    s.send(str(command))
    data = s.recv(2048)
    print(data)
if __name__ == "__main__":
    menu()
    s.close()
    # print("The command should be in this format A|B. It means, go to A")
    # text = input('Command format (A|B):') # Note change to the old (Python 2) raw_input
    # if text == "quit":
    #     break
    # s.send(text)
# sock.close()
