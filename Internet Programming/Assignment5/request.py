# Name: Wade Moulton
# Date: 10/27/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_5


# references used for assignment:
# given ppt slides and https://requests.readthedocs.io/en/master/user/quickstart/

# first import requests
import requests

# get user input for website and output file name
user_input = input("Enter a website and file name separated by a space (<website> <filename>): ")

# split the website and output into array to separate
user_input = user_input.split(" ")
# assign user values to variables if appropriate # of args
# if not right # of args raise exception
if len(user_input) < 2:
    raise ValueError("Must have a website and output file name.")
(user_input_url, user_input_filename) = user_input

# check for .txt and http:// in the user inputs and add if needed
if ".txt" not in user_input_filename:
    user_input_filename += ".txt"
if "http://" not in user_input_url:
    user_input_url = f"http://{user_input_url}"

# next send http request
req = requests.get(user_input_url)
# raise an exception if bad request made
req.raise_for_status()

# assign status code to a variable and print to console
status_code = req.status_code
print("{:<15}{:<20}\n{:<15}{:<20}".format("Request to: ", user_input_url, "Status code: ", status_code))

# try to create response file
try:
    # check that status code is good and then assign the response text to variable]
    if status_code == 200:
        res_text = req.text

        # create or override file and set encoding to utf-8
        res_file = open(user_input_filename, "w", encoding="utf-8")

        # write response text content to file
        res_file.write(res_text)
        # close the file
        res_file.close()
        # print confirmation that file was created
        print("{:<15}{:<20}".format("File created: ", user_input_filename))

        # ask if user would like to print full response instead of doing automatically
        print_full_response = input("Would you like to print the full response to console (y/n): ")
        if print_full_response.lower() == "y":
            print(res_text)

# catch any additional exceptions and print to console
except Exception as e:
    print(e)


