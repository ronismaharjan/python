# we can use *args in the function to get many argument as needed
def add(*args):
    # this is a docstring
    ''' this function can take any number of arguments and return sum of given number'''
    total = 0

    for n in args:
        total += n
    return total


result = add()
print(result)


# We us **kwargs if we want to use keyword arguments like sum( a = 10, b= 23) here we can use a and b without defining in function

def calculate(**kwargs):
    a = kwargs.get("color")
    for (key, value) in kwargs.items():
        print(value)
        print(a)


calculate(a=0, b=2, color="red")
