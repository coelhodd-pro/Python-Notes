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

while True:
    try:
        f_n = int(input("Provide the first number: "))
        s_n = int(input("Provide the second number: ")) 
    except ValueError:
        print("Please provide numbers for the calculator. Try again.")

    operation = input("Provide the desired operation[+, -, *, /]: ")

    match operation:
        case "+":
            addition(f_n, s_n)
        case "-":
            subtraction(f_n, s_n)
        case "*":
            multiplication(f_n, s_n)
        case "/":
            division(f_n, s_n)
        case _:
            print("Operation not available. Try again.")