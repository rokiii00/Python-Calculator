def add():
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    return num1 + num2

def sub():
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    return num1 - num2

def mult():
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    return num1 * num2

def div():
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    try:
        return num1 / num2
    except ZeroDivisionError:
        return (f"{num1} / {num2} = Error: Division by zero")

'''
num1 = 2
num2 = 1

print(add(num1, num2))
print(sub(num1, num2))
print(mult(num1, num2))
print(div(num1, num2))
'''

while True:
    print("Choose an operation:")
    op = input(" + Addition\n - Subtraction\n * Multiply\n / Divide\n" )

    if op == "+":
        print(add())
    elif op == "-":
        print(sub())
    elif op == "*":
        print(mult())
    elif op == "/":
        print(div())
    else:
        print("Invalid Operation")

    inp = input("Would you like to Continue? [Y]es or [N]o: ").upper()
    if inp == "N":
        break
