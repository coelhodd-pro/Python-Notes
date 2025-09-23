def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: Division by zero.")

def main():
    while True:
        # No exception handling was used in this example
        a = int(input("Provide the first number: "))
        b = int(input("Provide the second number: "))
        op = input("Provide the desired operation[+, -, *, /]: ")

        if op == "+":
            print(addition(a, b))
        elif op == "-":
            print(subtraction(a, b))
        elif op == "*":
            print(multiplication(a, b))
        elif op == "/":
            print(division(a, b))
        else:
            print("Operation not available. Try again.")

main()