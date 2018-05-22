import sys

class arduino_data():
    def __init__(self, humidity, temperature):
        self.humidity = humidity
        self.temperature = temperature

    def from_json(dct):
        if 'arduino_data' in dct:
            return arduino_sensor_data(dct['humidity'], dct['temperature'])
        return dct

    def __str__(self):
        return "hum {}, temp {}".format(self.humidity, self.temperature)

class ev3_status():
    def __init__(self, status, position):
        self.status = status
        self.position = position

    def from_json(self, dct):
        if 'ev3_status' in dct:
            return ev3_status(dct['status'], dct['position'])
        return dct

class warehouse_data():
    pass

class ev3_job():
    def __init__(self, pick_up, drop_off):
        self.pick_up = pick_up
        self.drop_off = drop_off

    def from_json(self, dct):
        if 'ev3_job' in dct:
            return ev3_job(dct['pick_up'], sct['drop_off'])
        return dct
