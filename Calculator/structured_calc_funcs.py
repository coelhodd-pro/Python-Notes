def addition(first_number, second_number):
    print(first_number + second_number)

def subtraction(first_number, second_number):
    print(first_number - second_number)

def multiplication(first_number, second_number):
    print(first_number * second_number)

def division(first_number, second_number):
    try:
        print(first_number / second_number)
    except ZeroDivisionError:
        print("ERROR: Division by zero!")