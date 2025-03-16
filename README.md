# PythonTCP demo for CECS 327
## Instructions for Users
There are two files to run in python, Client.py and Server.py. You can run them with their respective python commands ``python Client.py`` and ``python Server.py``.

Running the Server file will prompt the user for an IP address, which will be the current computer's private IP address, and a port number to open on the current computer as well. You will need to port forward the private ip and port you used as input on your router to expose this server to the internet.

Running the Client file will prompt the user for 2 things first, an IP address and a port number to connect to. If connecting locally, input the private IP address of the server, if connecting over the internet input the public IP of the router the server is port forwarded on. The port is similar, either the port opened on a private network, but if over the internet, whatever port you port forwarded on the router. If the given IP address has no exposed given port, an error message will display and you will be prompted to try again. If connection is successful, the user will be prompted to input a message to send, which the server will receive and reply with the same message but all upper case. You can continue to send messages to the server by selecting "Y" or "y" after sending a message to send another.
