import pdb

def divide_numbers(a, b):
    pdb.set_trace()   # breakpoint
    result = a / b
    return result

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

ans = divide_numbers(x, y)
print("Result =", ans)