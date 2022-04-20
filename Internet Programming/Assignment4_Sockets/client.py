# Name: Wade Moulton
# Date: 10/11/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_4-Sockets

import socket

# creating constant variables for the server port and address using localhost address
SERVER_PORT = 12345
SERVER_ADDR = "127.0.0.1"

# create sender socket and connect to server
sender = socket.socket()
sender.connect((SERVER_ADDR, SERVER_PORT))

# supplied testing strings list for this assignment
testing_strings = ["E1.0 -945 1689 -950 230 -25 1",
                   "S0 2 -945 1689 -950 230 -25 1 1e-15",
                   "G4.1 0 0",
                   "4 1 0",
                   "E1.0",
                   "S1.0",
                   "S0 2 -945 1689 -950 230 -25 1 -1e-15",
                   "Not a number",
                   "S0 2 -945 1689 -950 230 -25 1 0",
                   "S0 2 -945 1689 -950 230 G 1 1e-15"]

# iterate through each item in testing strings list
for msg in testing_strings:
    # first print message being sent and then assign encoded message to variable and send to server
    print(f"SEND: {msg}")
    encoded_msg = msg.encode()
    sender.sendall(encoded_msg)

    # close connection and receive encoded data from server
    # assign encoded data to variable
    sender.shutdown(1)
    encoded_data = sender.recv(2048)
    response = ""

    # iterate through encoded data, decode, and assign to string variable
    while len(encoded_data) > 0:
        response += encoded_data.decode()
        encoded_data = sender.recv(2048)

    # output response string from server
    print(f"RECV: {response}")

    # close sender socket
    sender.close()
    # on the last iteration a new connection is opened and server responds with string index out of range
    # create if statement to ensure new connection is not made on last iteration of testing strings list
    if msg != testing_strings[len(testing_strings) - 1]:
        sender = socket.socket()
        sender.connect((SERVER_ADDR, SERVER_PORT))

# make sure sender socket is closed
sender.close()
