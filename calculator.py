import re

def perform_calculation(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        try:
            return x / y
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "Please enter a valid operator: +, -, * or /"

# Takes input for numbers and operator separately
try:
    x = int(input("Please enter the first number: "))
    y = int(input("Please enter the second number: "))
    operator = input("Please enter the operator (+, -, /, or *): ")

    calculation = f"{x} {operator} {y}" 

    # Writes calculation to the file
    try:
        with open('Calculator_history.txt', 'a') as file:
            file.write(calculation + '\n')
    except IOError:
        print("File I/O error occurred")

    result = perform_calculation(x, y, operator)
    print(result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")

# Reading equations from the text file
try:
    with open('Calculator_history.txt', 'r') as file:
        equations = file.readlines()
        print("Equations in the file:")
        for equation in equations:
            print(equation.strip())

except FileNotFoundError:
    print("File not found. No history available.")