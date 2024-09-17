import os
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


operation = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": division,
    "%": modulo
}


def calculator():
    while True:
        num1 = int(input("Enter your first number: "))

        while True:
            print("Available operations: + - * / %")
            select_symbol = input("Pick a symbol from above: ")

            if select_symbol not in operation:
                print("Invalid operation. Please try again.")
                continue

            num2 = int(input("Enter your second number: "))
            calculator_function = operation[select_symbol]
            output = calculator_function(num1, num2)

            if isinstance(output, str):
                print(output)
            else:
                print(f"{num1} {select_symbol} {num2} = {output}")

            should_continue = input( "Enter 'yes' to continue with the previous result, 'no' to start fresh, or 'x' to exit: ").strip().lower()

            if should_continue == "yes":
                num1 = output
            elif should_continue == "no":
                break
            elif should_continue == "x":
                print("Exiting...")
                return
            else:
                print("Invalid input. Please enter 'yes', 'no', or 'x'.")

        # Clear the screen (works on Windows only)
        os.system("cls" if os.name == "nt" else "clear")


calculator()
