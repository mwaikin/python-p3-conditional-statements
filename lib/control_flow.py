#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
     if (username == "ADMIN" or username == "admin") and password == "12345":
         return "Access granted"
     else:
         return "Access denied"    

print(admin_login("admin", "12345"))

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        response = "brisk"
    elif  40 <= temperature <= 65:
        response = "a little chilly"   
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"

    return f"It's {response} out there!"

print(hows_the_weather(34))


def fizzbuzz(num):
    # your code here
    if  num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num

print(fizzbuzz(15)) 

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 -num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Division by zero error")
    else:
        print("Invalid operation!")
        return None

print(calculator("*", 4, 2)) 