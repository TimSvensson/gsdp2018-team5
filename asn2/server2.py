import os
from socket import *
import ev3dev.ev3 as ev3
from time import sleep
from ev3dev.auto import *

host = ""
port = 14000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ('Adding button')
btn = Button()
def forward(lm, rm):
    lm.polarity = "normal"
    rm.polarity = "normal"
    lm.run_forever(speed_sp=100)
    rm.run_forever(speed_sp=100)
    #sleep(time)
    #lm.stop()
    #rm.stop()
def turnright(lm, rm):
    sleep(0.5)
    gy.mode='GYRO-RATE'
    gy.mode='GYRO-ANG'
    lm.polarity = "normal"
    rm.polarity = "normal"
    lm.run_forever(speed_sp=100)
    rm.run_forever(speed_sp=0)
    #while gy.value()< 90:
        #sleep(0.02)
    #lm.stop()
    #rm.stop()
print "Waiting to receive messages..."
rm = ev3.LargeMotor('outC')
lm = ev3.LargeMotor('outB')
lf = ev3.MediumMotor('outA')
gy = ev3.GyroSensor()
assert gy.connected
assert rm.connected
assert lm.connected
assert lf.connected
while not btn.any():
    (data, addr) = UDPSock.recvfrom(buf)
    data=str(data, encoding="utf-8")
    print "Received message: " + data
    if data=="go forward":
        forward(lm, rm)
    elif data=="turn right"
        turnright(lm, rm)
UDPSock.close()
os._exit(0)
