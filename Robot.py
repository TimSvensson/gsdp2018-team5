#!/usr/bin/env python3
from time import sleep
import ev3dev.ev3 as ev3
import RoutingClass as Route
import ArmClass as Arm
import MovementClass as Movement

path = []
currentPos = ""
action = []

def lineFollowing(cs, gs, mc, ac):
    mc.setNormal()
    stop = False
    while not stop:
        print ("COlor: ", cs.value())
        if (cs.value() == 6):
            mc.turnLeft()
        elif (cs.value() == 1):
            mc.turnRight()
        mc.setSpeed(300)
        if (cs.value() == 5):
            print("Pickup")
            mc.stop()
            ac.pickUp()
            # stop = True
            turnAround(gs, 180, mc)
        if (cs.value() == 3):
            processRoute(gs, mc)
        if (cs.value() == 4):
            print("PutDown")
            mc.stop()
            ac.putDown()
            mc.setInverse()
            mc.forward()
            sleep(1)
            mc.setNormal()
            turnAround(gs, 180, mc)
            # stop = True
            if (len(path) == 0):
                stop = True

# def pickUp
#
def turnRight(gs, degree, mc):
    sleep(0.3)
    tmp = gs.value()
    while(abs(gs.value() - tmp) <= degree):
        mc.turnRight()

def turnLeft(gs, degree, mc):
    # sleep(0.1)
    tmp = gs.value()
    mc.setLeftInverse()
    while(abs(gs.value() - tmp) <= degree):
        # mc.turnLeft()
        mc.setLeftSpeed(10)
        mc.setRightSpeed(200)
    mc.setNormal()

def turnAround(gs, degree, mc):
    mc.setLeftSpeed(200)
    mc.setRightInverse()
    mc.setRightSpeed(0)
    gs.mode = "GYRO-RATE"
    gs.mode = "GYRO-ANG"
    tmp = gs.value()
    while(abs(gs.value() - tmp) <= degree):
        print("tmp: ",tmp)
        print("value: ",gs.value())
        print(abs(gs.value() - tmp))
        pass
    mc.setNormal()
    mc.stop()

def forward():
    # sleep(0.4)
    mc.forward()
    sleep(0.4)

def processRoute(gs, mc):
    global path
    print (path)
    if path[0] == "left":
        turnLeft(gs, 82, mc)
    elif path[0] == "right":
        turnRight(gs, 90, mc)
    else:
        forward()
    path.pop(0)
# def turnRight(gs, degree):
#
# def foward():
#
# def backward():

if __name__ == "__main__":
    global path
    global currentPos

    rm = ev3.LargeMotor('outC')
    lm = ev3.LargeMotor('outB')
    lf = ev3.MediumMotor('outA')
    gs = ev3.GyroSensor()
    cs = ev3.ColorSensor()

    mc = Movement.MovementController(lm, rm)
    ac = Arm.ArmController(lf)
    rc = Route.RoutingController('start', 'd')
    currentPos = 'd'
    path = rc.findPath()
    path = path + rc.findPath(currentPos, 'end')
    path = path + rc.findPath('end', 'c')
    path = path + rc.findPath('c', 'end')
    print(path)

    assert cs.connected
    assert gs.connected

    cs.mode = "COL-COLOR"
    gs.mode = "GYRO-ANG"

    try:
        lineFollowing(cs, gs, mc, ac)
        mc.stop()
        # ac.pickUp()
        # mc.stop()
    except KeyboardInterrupt:
        mc.stop()

    #red: 5
    #black: 1
    #white: 6
    #blue: 2
    #green: 3
