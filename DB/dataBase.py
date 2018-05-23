#!/usr/bin/env python3

import MySQLdb as mdb
import sys
sys.path.append('../client-server')

import client
import util

def openConnection():
    db_connection = mdb.connect(host="localhost",
                                user="root",
                                passwd="GSPDT15",
                                db="automated_warehouse_management")

    return db_connection

def cursor():
    conn = openConnection()
    return conn.cursor()

def getStorageUnitData():
    db_cursor = cursor()
    db_cursor.execute('SELECT * FROM `storage_unit`')
    
    data = db_cursor.fetchall()

def getSensorData():
    db_cursor = cursor()
    db_cursor.execute('SELECT * FROM `sensor_data`')
    
    data = db_cursor.fetchall()

def getEV3Data():
    db_cursor = cursor()
    db_cursor.execute('SELECT * FROM `ev3_robot`')
    
    data = db_cursor.fetchall()

def closeConnection():
    conn = openConnection()
    conn.close()


# Connect to the socker server client

c = client.client(HOST, PORT, util._db)
c.connect()

while True:
    c.send(receiver, content)
    msg = c.read()

    if util._ard in dct:
        temperature =  dct._temp
        humidity = dct._hum
        
        conn = openConnection()
        db_cursor = cursor()
        db_cursor.execute('INSERT INTO `sensor_data` (humidity, temperature) VALUES ({}, {})'.format(humidity, temperature))

        conn.commit()

    elif util._ev3_s in dct:
        status = dct._stat
        ev3_position = dct._pos

        conn = openConnection()
        db_cursor = cursor()
        db_cursor.execute('INSERT INTO `ev3_robot` (status, ev3_position) VALUES ({}, {})'.format(status, ev3_position))

        conn.commit()


c.disconnect()

if __name__ == '__main__':
    openConnection()
    getStorageUnitData()
    getSensorData()
    getEV3Data()
    closeConnection()
