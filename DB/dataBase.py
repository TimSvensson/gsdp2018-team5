#!/usr/bin/env python3

import MySQLdb as mdb
import time
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
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'A\'')
    a = db_cursor.fetchall()
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'B\'')
    b = db_cursor.fetchall()
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'C\'')
    c = db_cursor.fetchall()
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'D\'')
    d = db_cursor.fetchall()
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'E\'')
    e = db_cursor.fetchall()
    
    db_cursor.execute('SELECT * FROM `storage_unit` WHERE storage_unit_name = \'F\'')
    f = db_cursor.fetchall()

    return{util._wh:True, 'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f }

def getSensorData():
    db_cursor = cursor()
    
    db_cursor.execute('SELECT humidity FROM `sensor_data`')
    humidity = db_cursor.fetchall()
    
    db_cursor.execute('SELECT temperature FROM `sensor_data`')
    temperature = db_cursor.fetchall()

    return{util._ard:True, util._hum:humidity, util._temp:temperature}

def getEV3Data():
    db_cursor = cursor()
    
    db_cursor.execute('SELECT status FROM `ev3_robot`')
    status = db_cursor.fetchall()
    
    db_cursor.execute('SELECT ev3_position FROM `ev3_robot`')
    position = db_cursor.fetchall()

    return{util._ev3_s:True, util._stat:status, util._pos:position}

def closeConnection():
    conn = openConnection()
    conn.close()


# Connect to the socker server client

def client_func():

    PORT = int(sys.argv[1])
    HOST = "localhost"
    c = client.client(HOST, PORT, util._db)
    c.connect()


    conn = openConnection()
    db_cursor = cursor()

    while True:
        
        time.sleep(1) # One Second Delay
        
        while True:

            dct = c.read()
    
            
            if util._ard in dct:
                temperature =  dct[util._temp]
                humidity = dct[util._hum]
                db_cursor.execute('INSERT INTO `sensor_data` (humidity, temperature) VALUES ({}, {})'.format(humidity, temperature))
                conn.commit()
    
            elif util._ev3_s in dct:
                status = dct[util._stat]
                ev3_position = dct[util._pos]
                db_cursor.execute('INSERT INTO `ev3_robot` (status, ev3_position) VALUES ({}, {})'.format(status, ev3_position))
                conn.commit()
    
            elif util._wh in dct:
                a = dct['a']
                b = dct['b']
                c = dct['c']
                d = dct['d']
                e = dct['e']
                f = dct['f']
    
                lst = []
                lst.append(a)
                lst.append(b)
                lst.append(c)
                lst.append(d)
                lst.append(e)
                lst.append(f)
    
                db_cursor.execute('SELECT storage_unit_name from `storage_unit`')
                storage_unit_names = db_cursor.fetchall()
                for row in storage_unit_names:
                    for items in lst:
                        db_cursor.execute('UPDATE TABLE `storage_unit` SET no_of_items = {} WHERE storage_unit_name = {}'.format(items, row))
                conn.commit()
    
            elif util._db_f in dct:
                warehouse = getStorageUnitData()
                arduino = getSensorData()
                ev3_data = getEV3Data()
    
                dct = {}
                dct.update(arduino)
                dct.update(ev3_data)
                dct.update(warehouse)
                c.send(util._to_srv, dct)

            elif util._empty in dct:
                break

    c.disconnect()

if __name__ == '__main__':
    client_func()
