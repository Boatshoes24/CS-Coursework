# Name: Wade Moulton
# Date: 10/11/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_4-Sockets

import socket
from polynomials import evaluate, bisection

# creating constant variables for the server port and address using localhost address
SERVER_PORT = 12345
SERVER_ADDR = '127.0.0.1'

# create globals for various errors that might be encountered
ARG_EXCEPTION = "XToo few arguments"
VALUE_EXCEPTION = "XCould not convert string to float"
REQUEST_EXCEPTION = "XIncorrect command type"
TOLERANCE_EXCEPTION = "XInvalid tolerance"

# create socket and start listening
listener = socket.socket()
listener.bind((SERVER_ADDR, SERVER_PORT))
listener.listen(0)
print("Server started. Listening on " + SERVER_ADDR + ":" + str(SERVER_PORT))


# infinite loop so that server can always accept connections
while True:
    # assign and print client connection info
    (sock, address) = listener.accept()
    print(f"Received connection from: {address}")
    # assign encoded data to variable and create a new variable to store decode data
    encoded_data = sock.recv(2048)
    client_data = ""

    # iterate and decode through data and assign to decoded variable
    while len(encoded_data) > 0:
        client_data += encoded_data.decode()
        encoded_data = sock.recv(2048)

    try:
        # print received data and split data into list
        print(f"RECV: {client_data}")
        client_data = client_data.split(" ")
        if len(client_data) < 1:
            raise Exception(ARG_EXCEPTION)

        # splitting first value to get the command and storing in request_start
        request = client_data[0]
        request_start = request[0]

        # if request is for evaluation function
        if request_start == "E":
            if len(client_data) < 2:
                raise Exception(ARG_EXCEPTION)

            # evaluation function expects an x value and a polynomial list
            # first convert x_value to float
            x_value = float(request[1:])
            # convert remaining list values to floats for the polynomial values
            poly_values = [float(i) for i in client_data[1:]]
            # call function evaluate and assign return to response
            response = f"E{evaluate(x_value, poly_values)}"

        # if request is for bisection function
        elif request_start == "S":
            if len(client_data) < 3:
                raise Exception(ARG_EXCEPTION)

            # bisection function expects a value, b value, polynomial list, and tolerance value
            # first convert a and b values to floats
            a_value = float(request[1:])
            b_value = float(client_data[1])
            # convert remaining list values to floats for the polynomial values except the last value
            poly_values = [float(i) for i in client_data[2:len(client_data) - 1]]
            # convert tolerance value to float and check to make sure it is non-negative and not equal to 0
            tolerance = float(client_data[-1])
            if tolerance <= 0:
                raise Exception(TOLERANCE_EXCEPTION)
            # call function bisection and assign return response
            response = f"S{bisection(a_value, b_value, poly_values, tolerance)}"

        # this exception will be raised when first value is not E or S and no other exceptions have been raised
        else:
            raise Exception(REQUEST_EXCEPTION)

    # using the built in ValueError exception for issues converting strings to floats
    except ValueError:
        response = VALUE_EXCEPTION
    # catch any other errors in case they need to be handled
    except Exception as err:
        response = str(err)

    # send response to client and close socket
    print(f"SEND: {response}")
    sock.sendall(response.encode())
    sock.close()