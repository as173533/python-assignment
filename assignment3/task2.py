import math

def square_root(num):
    return math.sqrt(num)
def logarithm(num):
    return math.log(num)
def sine(num):
    return math.sin(num)


num = int(input("Enter a number: "))
print(f"Square root: {square_root(num)}")
print(f"Logarithm: {logarithm(num)}")
print(f"Sine: {sine(num)}")