#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if(username.lower() == 'admin' and password == '12345'):
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temperature):
    # your code here
    if(temperature > 85):
        return "It's too dang hot out there!"
    if(temperature > 40 and temperature < 65):
        return "It's a little chilly out there!"
    if(temperature < 40):
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    if(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif(num % 3 == 0):
        return "Fizz"
    elif(num % 5 == 0):
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # your code here
    if(operation == '+' or operation == '-' or operation == '*' or operation == '/'):
        calc_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*":num1 * num2,
        "/": num1 / num2
        }
    
        return calc_map.get(operation)
    else:
        print("Invalid operation!")
        return None