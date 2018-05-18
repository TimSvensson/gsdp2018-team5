import sys

json_ui  = 'ui'
json_db  = 'database'
json_ard = 'arduino'
json_ev3 = 'ev3'
json_err = 'error'

i_ui  = 1
i_db  = 2
i_ard = 3
i_ev3 = 4
i_err = -1

json_receivers = json_ui, json_db, json_ard, json_ev3

def i_to_json(_i):
    i = int(_i)
    if (i==i_ui):
        return json_ui
    elif (i==i_db):
        return json_db
    elif (i==i_ard):
        return json_ard
    elif (i==i_ev3):
        return json_ev3
    else:
        return json_err

def json_to_i(json):
    if (json==json_ui):
        return i_ui
    elif (json==json_db):
        return i_db
    elif (json==json_ard):
        return i_ard
    elif (json==json_ev3):
        return i_ev3
    else:
        return i_err

if (__name__ == "__main__"):
    arg = " ".join(sys.argv[1:]).strip()
    try:
        int(arg)
        s = i_to_json(arg)
        print(s)
    except ValueError:
        i = json_to_i(arg)
        print(i)
