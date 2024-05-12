# Sum
def add(n1, n2):
    return (n1 + n2)

# subtract
def subtract(n1, n2):
    return (n1 - n2)

# multiply
def multiply(n1, n2):
    return (n1 * n2)

# divide
def divide(n1, n2):
    return (n1 / n2)


def wanna_continue():
    user_answer = input("Do you wanna continue 'Yes' or 'No'? ").lower()
    if (user_answer == "yes"):
        return True
    else:
        return False

#Dictionary to store the function for calculator with the symbol 

calculator = {
    "+":add, 
    "-":subtract,
    "*":multiply,
    "/":divide,
}

#The main part of the programe
n1 = float(input("Enter the first number: "))
want_continue = True
while want_continue:
    for key in calculator:
        print(key)
    operation = str(input("What operation do you want to do ? "))
    n2 = float(input("Enter the second number: "))
    result = calculator[operation](n1, n2)
    print(result)
    want_continue = wanna_continue()
    if want_continue:
        n1 = result

