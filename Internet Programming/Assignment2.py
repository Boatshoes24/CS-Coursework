# Name: Wade Moulton
# Date: 9 / 12 / 2020
# Class: CS 4720
# Section: W01
# Assignment: 2
# Instructor: Dr.Sarah North


def square_number(num):
    result = num ** 2
    return f'The square of {num} is {result}!'


def fix_start(text):
    letter = text[0]
    new_string = text[1:].replace(letter, '*')
    new_string = letter + new_string
    return new_string


def not_bad(text):
    not_index = -1
    bad_index = -1
    if text.find('not'):
        not_index = text.find('not')
    if text.find('bad'):
        bad_index = text.find('bad') + 3
    if -1 < not_index < bad_index:
        new_string = text[:not_index] + 'good' + text[bad_index:]
        return new_string
    return text


print(not_bad("This dinner is not that bad!"))