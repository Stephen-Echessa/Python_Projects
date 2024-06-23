# CALCULATOR

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    num1 = float(input("What is the first number?: "))
    num2 = float(input("What is the second number?: "))

    for operation in operations:
        print(operation)

    operator = input("Pick an operation symbol from the ones above: ")

    answer = operations[operator](num1,num2)

    print(f"{num1} {operator} {num2} = {answer}")

    should_continue = True

    while should_continue:
        continuation = input(f"Type 'y' to continue calculating with {answer} and 'n' to start a new calculation. ")
        if continuation=='y':
            operator = input("Pick an operation symbol: ")
            num3 = float(input("What is the next number? "))
            answer = operations[operator](answer,num3)
            print(answer)
        else:
            should_continue=False
            calculator()

calculator()