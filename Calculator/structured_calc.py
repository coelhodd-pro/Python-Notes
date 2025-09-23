from structured_calc_funcs import *

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