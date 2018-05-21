#!/usr/bin/env python3
from time import sleep

class RoutingController:
    WAREHOUSE_MAP = {
        'start' : [
            {
                'left': 'b'
            }, {
                'right': 'a'
            }, {
                'forward': 'cross2'
            }
        ],
        'a' : [
            {
                'left': 'start'
            }, {
                'right': 'cross2'
            }, {
                'forward': 'b'
            }
        ],
        'b' : [
            {
                'left': 'cross2'
            }, {
                'right': 'start'
            }, {
                'forward': 'a'
            }
        ],
        'cross2' : [
            {
                'left': 'd'
            }, {
                'right': 'c'
            }, {
                'forward': 'end'
            }
        ],
        'c' : [
            {
                'left': 'cross1'
            }, {
                'right': 'end'
            }, {
                'forward': 'd'
            }
        ],
        'd' : [
            {
                'left': 'end'
            }, {
                'right': 'cross1'
            }, {
                'forward': 'c'
            }
        ],
        'cross1' : [
            {
                'left': 'a'
            }, {
                'right': 'b'
            }, {
                'forward': 'start'
            }
        ],
        'end' : [
            {
                'left': 'c'
            }, {
                'right': 'd'
            }, {
                'forward': 'cross1'
            }
        ]
    }

    def __init__(self, start, end):
        #set wheel motor for MovementController
        self.start = start
        self.end = end
        self.route = []

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def resetRoute(self):
        self.route = []

    def findPath(self, start='', end=''):
        self.resetRoute()
        if (start == ''):
            start = self.start

        if (end == ''):
            end = self.end

        tmpKey = ""
        tmpValue = ""
        found = 0
        finish = 0
        while not finish:
            for key, value in self.WAREHOUSE_MAP.items():
                if (key == start):
                    for value1 in value:
                        for key2,value2 in value1.items():
                            if ('cross' in value2):
                                tmpKey = key2
                                tmpValue = value2

                            if (end == value2):
                                found = 1
                                finish = 1
                                self.route.append(key2)
                    if (found == 0):
                        start = tmpValue
                        self.route.append(tmpKey)
                        break
        return self.route
