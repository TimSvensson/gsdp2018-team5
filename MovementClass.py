#!/usr/bin/env python3
from time import sleep

class MovementController(leftMotor, rightMotor):

    def __init__(self, leftMotor, rightMotor):
        #set wheel motor for MovementController
        self.leftMotor = leftMotor;
        self.rightMotor = rightMotor
        #set up connection
        assert self.leftMotor.connected
        assert self.rightMotor.connected

    #set motor to rotate clock-wise
    def setNormal(self):
        self.leftMotor.polarity = "normal"
        self.rightMotor.polarity = "normal"

    #set motor to rotate counter clock-wise
    def setInverse(self):
        self.leftMotor.polarity = "inversed"
        self.rightMotor.polarity = "inversed"

    #reset all the config
    def reset(self):
        self.leftMotor.reset()
        self.rightMotor.reset()

    #set robot to run forward with speed of 100
    def forward(self):
        setNormal()
        self.leftMotor.run_forever(speed_sp=100)
        self.rightMotor.run_forever(speed_sp=100)

    #set robot to run backward with speed of 100
    def backward(self):
        setInverse()
        self.leftMotor.run_forever(speed_sp=100)
        self.rightMotor.run_forever(speed_sp=100)

    #set robot to turn left
    def turnLeft(self):
        setNormal()
        self.leftMotor.run_forever(speed_sp=20)
        self.rightMotor.run_forever(speed_sp=100)

    #set robot to turn right
    def turnRight(self):
        setNormal()
        self.leftMotor.run_forever(speed_sp=100)
        self.rightMotor.run_forever(speed_sp=20)


    def pickUp(self):
        self.middleMotor.polarity = "inversed" # this will make the motor rotates clock-wise, which means going down
        self.middleMotor.run_forever(speed_sp=50) # speed 50 is pretty enough to lift package up
        sleep(1.5) # wait until the robot lower its arm to drop the package.
        self.middleMotor.stop() # stop rotates
        self.middleMotor.reset() # reset the config
