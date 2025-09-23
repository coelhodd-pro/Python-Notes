class Calculator:
    def __init__(self):
        pass 

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("ERROR: Division by zero!")

def main():
    calc = Calculator()
    while True:
        a = int(input("Provide the first number: "))
        b = int(input("Provide the second number: "))
        op = input("Provide the desired operation: ")

        if op == "+":
            print(calc.addition(a, b))
        elif op == "-":
            print(calc.subtraction(a, b))
        elif op == "*":
            print(calc.multiplication(a, b))
        elif op == "/":
            print(calc.division(a, b))
        else:
            print("Operation not available. Try Again.")
        
main()