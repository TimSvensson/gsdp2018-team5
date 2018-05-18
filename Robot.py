#!/usr/bin/env python3
from time import sleep
import ev3dev.ev3 as ev3
import RoutingClass as Route
import ArmClass as Arm
import MovementClass as Movement

def lineFollowing(cs, gs, mc, ac):
    mc.setNormal()
    stop = False
    while not stop:
        if (cs.value() == 6):
            mc.turnLeft()
        elif (cs.value() == 1):
            mc.turnRight()
        mc.setSpeed(200)
        if (cs.value() == 5):
            mc.stop()
            # pickUp(ac)
            stop = True
        if (cs.value() == 3):
            sleep(0.6)
            turnRight(gs, 90, mc)
# def pickUp
#
def turnRight(gs, degree, mc):
    tmp = gs.value()
    while(abs(gs.value() - tmp) <= degree):
        mc.turnRight()
# def turnRight(gs, degree):
#
# def foward():
#
# def backward():

if __name__ == "__main__":
    rm = ev3.LargeMotor('outC')
    lm = ev3.LargeMotor('outB')
    lf = ev3.MediumMotor('outA')
    gs = ev3.GyroSensor()
    cs = ev3.ColorSensor()

    mc = Movement.MovementController(lm, rm)
    ac = Arm.ArmController(lf)
    rc = Route.RoutingController('start', 'end')

    assert cs.connected
    assert gs.connected

    cs.mode = "COL-COLOR"
    gs.mode = "GYRO-ANG"

    print (cs.value())
    print (gs.value())

    try:
        lineFollowing(cs, gs, mc, ac)
        mc.stop()
        ac.pickUp()
        mc.stop()
    except KeyboardInterrupt:
        mc.stop()

    #red: 5
    #black: 1
    #white: 6
    #blue: 2
    #green: 3
