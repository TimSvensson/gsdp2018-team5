#!/usr/bin/env python3
from time import sleep
import ev3dev.ev3 as ev3
import RoutingClass as Route
import ArmClass as Arm
import MovementClass as Movement

def lineFollowing(cs, mc):
    mc.setNormal()
    stop = False
    while not stop:
        if (cs.value() == 1):
            mc.turnLeft()
        elif (cs.value() == 6):
            mc.turnRight()
        elif (cs.value() == 4):
            mc.stop()
            stop = True

        mc.setSpeed(50)

def turnLeft(gs, degree):

def turnRight(gs, degree):

def foward():

def backward():

if __name__ == "__main__":
    rm = ev3.LargeMotor('outC')
    lm = ev3.LargeMotor('outB')
    lf = ev3.MediumMotor('outA')
    gs = ev3.GyroSensor()
    cs = ev3.ColorSensor()

    mc = Movement.MovementController(lm, rm)
    ac = Arm.ArmController(lf)
    rc = Route.RoutingController()

    assert cs.connected
    assert gs.connected

    cs.mode = "COL-COLOR"
    gy.mode = "GYRO-ANG"

    rc.findPath()
