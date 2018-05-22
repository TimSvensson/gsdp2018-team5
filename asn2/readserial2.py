# temporary work in windows system
import serial
import json
import time
# Save as client.py 
# Message Sender
import os
from socket import *
host = "169.254.208.174" # car's ip
port = 14000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

def readserial(port1):
    ser = serial.Serial(port1, 9600, timeout=0.5)
    humidity = 0
    tem = 0
    while (1):
        data = ser.readline()
        print(data)
        if len(data) == 5:
            humidity = int.from_bytes(data[1:3], byteorder='big') / 10
            print(humidity)

            tem = int.from_bytes(data[3:5], byteorder='big') / 10
            print(tem)

            dict_json = {}
            dict_json['humidity'] = humidity
            dict_json['temperature'] = tem

            print(dict_json)

            # json_str = json.dumps(dict_json)
            #
            # print(json_str)

            file = open('test.json', 'w', encoding='utf-8')
            json.dump(dict_json, file, ensure_ascii=False)
            file.close()

            ser.close()
            print('read serial successed, JSON created')

            break

            # file = open('test.json', 'r', encoding='utf-8')
            # s = json.load(file)
            # print(s)

    return humidity, tem

if __name__ == '__main__':
    port1 = 'COM3'

    print('start to read %s' % (port1))

    while (1):
        humidity, tem = readserial(port1)
        time.sleep(2)
       
        if humidity < 50:
            data="go forward"
        else:
            data="turn right"
        data=bytes(data, encoding = "utf8")
   
        UDPSock.sendto(data, addr)
        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)
