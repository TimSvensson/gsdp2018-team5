import sys
import json
import socket
import struct

# Different message flags
_push   = 'push'
_pop    = 'pop'
_type   = 'type'
_empty  = 'empty'
_cont   = 'contents'
_msg    = 'message'
_rec    = 'receiver'

# Recipient
_to_all = 'to_all'
_to_srv = 'to_server'
_to_db  = 'to_db'
_to_ui  = 'to_ui'
_to_ev3 = 'to_ev3'
_to_ard = 'to_arduino'

# Different types of clients
_test   = 'test'
_db     = 'database'
_ev3_s  = 'ev3_status'
_ev3_j  = 'ev3_job'
_ui     = 'user-interface'
_ard    = 'arduino'

# Arduino sensors
_hum    = 'humidity'
_temp   = 'temperature'

# EV3
# status
_stat   = 'status'
_pos    = 'position'
#job
_to     = 'to'
_from   = 'from'

# Wareohuse
_wh     = 'warehouse'


def ard_to_dct(hum, temp):
    return {_ard: True, _hum: hum, _temp: temp}

def ev3_status_to_dct(stat, pos):
    return {_ev3_s: True, _stat: stat, _pos: pos}

def ev3_job_to_dct(f, to):
    return {_ev3_j: True, _from: f, _to: to}

def warehouse_to_dct(a,b,c,d,_in,out):
    return {_wh: True, 'a':a, 'b':b, 'c':c, 'd':d, 'in':_in, 'out':out}

# taken from
# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

    