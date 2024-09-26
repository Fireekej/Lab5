import math

def compute_function(x):
    if x >= 3:
        return math.sin(x)
    elif 0 <= x < 3:
        return math.cos(x)
    elif x < 0:
        return math.tan(x)

x = float(input("Enter the value of x: "))
result = compute_function(x)
print(f"y = {result}")
