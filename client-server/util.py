import sys
import json

# Different message flags
_push   = 'push'
_pop    = 'pop'
_type   = 'type'
_empty  = 'empty'
_cont   = 'cont'
_msg    = 'msg'
_rec    = 'rec'

_to_all = 'to_all'
_to_srv = 'to_srv'
_to_db  = 'to_db'
_to_ui  = 'to_ui'
_to_ev3 = 'to_ev3'
_to_ard = 'to_ard'

# Different types of clients
_test   = 'test'
_db     = 'db'
_ev3    = 'ev3'
_ui     = 'ui'
_ard    = 'ard'

class data():
    def obj_from_dct():
        pass
    def dct_from_obj():
        pass

class arduino_data(data):
    def __init__(self, humidity, temperature, uv):
        self.humidity = humidity
        self.temperature = temperature
    def obj_from_dct(dct):
        if self.__class__.__name__ in dct:
            return arduino_data(
                dct['humidity'], dct['temperature'])
        return dct
    def dct_from_obj(self):
        dct = {}
        dct.update({'{}'.format(self.__class__.__name__): True})
        dct.update({'humidity':self.humidity})
        dct.update({'temperature': self.temperature})
        return dct

class ev3_status(data):
    def __init__(self, status, position):
        self.status = status
        self.position = position
    def obj_from_dct(self, dct):
        if self.__class__.__name__ in dct:
            return ev3_status(dct['status'], dct['position'])
        return dct
    def dct_from_obj(self):
        dct = {}
        dct.update({'{}'.format(self.__class__.__name__): True})        
        dct.update({'status':self.status})
        dct.update({'position':self.position})
        return dct

class warehouse_data(data):
    def __init__(self, storage_units):
        self.storage_units = storage_unit
    def obj_from_dct(self, dct):
        if self.__class__.__name__ in dct:
            del dict[self.__class__.__name__]
            return warehouse_data(dct)
    def dct_from_obj(dct):
        dct = {}
        dct.update({'{}'.format(self.__class__.__name__): True})
        return dct

class ev3_job(data):
    def __init__(self, pick_up, drop_off):
        self.pick_up = pick_up
        self.drop_off = drop_off
    def obj_from_dct(self, dct):
        if self.__class__.__name__ in dct:
            return ev3_job(dct['pick_up'], sct['drop_off'])
        return dct
    def dct_from_obj(self):
        dct = {}
        dct.update({'{}'.format(self.__class__.__name__): True})
        dct.update({'pick_up':self.pick_up})
        dct.update({'drop_off':self.drop_off})
        return dct

if __name__ == "__main__":
    a1 = arduino_data(-100,1,None)
    a_dct1 = a1.obj_to_dct()
    print(a_dct1)
    a2 = arduino_data.dct_to_obj(a_dct1)
    if a1.humidity == a2.humidity and\
            a1.temperature == a1.temperature and\
            a1.uv == a2.uv:
        print("Arduino test result: a1 == a2! :-)")
    else:
        print("Arduino test result: a1 != a2! :-(")
