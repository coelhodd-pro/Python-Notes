while True:
    first_number = int(input("Provide the first number: "))
    second_number = int(input("Provide the second number: "))

    operation = input("Provide the desired operation[+, -, *, /]: ")

    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "*":
        print(first_number * second_number)
    elif operation == "/":
        if second_number == 0:
            print("ERROR: Division by zero!")
        else:
            print(first_number / second_number)
    else:
        print("Operation not available. Try again.")