def write_on_file(content):
    with open("register_sys_db.txt", "a") as file:
        file.write(content + "\n")

def main():
    print("Provide data in the following format: Phone Number - Name")
    print("Type 'quit' to stop the program.")
    while True:
        u_input = input(">>> ")
        if u_input == "quit":
            break
        else:
            write_on_file(u_input)

main()