To use the client in your desired application you should first and foremost import the files client-server/client.py and client-server/util.py, both are needed.

To connect to the _Server_, which should be running in it's own terminal in the LAN, you use the following:

> _client = client.client(HOST, PORT, TYPE)

HOST and PORT are the host and port of the Server (should be printed out in the terminal the Server is running on).
TYPE is the _type_ of client you wish to run. For example, if you wish to connect to the server as the ev3-app you set TYPE=util._ev3 or if you wish to connect as the arduino you use TYPE=util._ard. TYPE is used by the server to figure our if you are the recipient of a message or not.

To connect the client to the server you write this:

> _client.connect()

... and to disconnect you use:

> _client.disconnect()

To send a message to someone, you'll use this command:

> _client.send(recipient, dict)

where _recipient_ is whom you wish to send your message to and _dict_ is a dictionary representation of what you wish to tell them.
All acceptable recipients can be found in util.py.
The dict should be constructed by one of the functions in util.py that are of the form *X_to_dct(...)*, they create a dictionary with the data you wish to send.

To see if someone sent you a message, use:

> dict = _client.read()

The received message is a dictionary. To check for what is available in the message received and to get the value out, use:

> if util._X in dict:
>     x = dict[util._X]

See client-server/util.py for further detail. (edited)
