'''
#defining functions
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2} ")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}" )
    
def print_one(arg1):
        print(f"arg1: {arg1} ")

def print_none():
    print("I got nothing." )

print_two("Rae", "Sams")
print_two_again("Rae", "Sams")
print_one("Rae")
print_none()
'''


'''
#defining functions and calling it in differnt ways
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} Cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers. ")
    print("Man, thats enough for a party! ")
    print("Get a blanket. \n")


print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do maths inside too: ")
cheese_and_crackers(10 +20, 5+6)

print("And we can combine the two, cariables and maths: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
'''


'''functions and files
#
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek (0)

def print_a_line(line_count, f):
    print(line_count, f.read())

current_file = open(input_file)

print("First lets print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape. ")
rewind(current_file)

print("let's print three lines: ")
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
'''

'''
#function to return something
def add(a,b):
    print(f"ADDING: {a} + {b} ")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING: {a} - {b} ")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING: {a} x {b} ")
    return a * b

def divide(a, b):
    print(f"DIVIDING: {a} / {b} ")
    return a // b

print("Let's do some math with just functions: ")

age = add(30, 5)
weight = subtract(78, 4)
height = multiply(40, 2)
iq = divide(100, 2)

print(f"AGE: {age}\n WEIGHT: {weight}\n HEIGHT: {multiply}\n IQ: {iq}")
'''


