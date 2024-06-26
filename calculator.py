from logo import logo

def add(n1, n2):
    """ With 3 double quote signs I can document my function. Docstrings."""
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def square(n1, n2):
    return n1 ** n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square
}


def calculator():
    """Recursive function"""
    print(logo)
    proceed = True

    first_number = float(input("What's the first number?\n"))
    second_number = float(input("What's the second number?\n"))
    chosen_operation = input("Choose an operation from the list above\n")

    result = operators[chosen_operation](first_number, second_number)
    input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit\n")
    while proceed:
        for symbol in operators:
            print(symbol)
        next_operation = input("Choose an operation from the list above\n")
        next_number = float(input("What's the next number?\n"))

        # Access operators dict - chosen_operation = operators[key] value ex. add
        calculate = operators[chosen_operation]
        # result = add(first_number, second_number)
        final_result = calculate(result, next_number)

        print(f"Current result is: {final_result}")

        more = input(f"Type 'y' to continue calculating with {final_result}, or type 'n' to exit\n")
        if more == 'n':
            proceed = False
            print(f"{result} {next_operation} {second_number} = {final_result}")
        else:
            # Recursion
            calculator()


calculator()
