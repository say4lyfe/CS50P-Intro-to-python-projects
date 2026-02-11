expression = input("expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x + z))
if y == "-":
    print(float(x - z))
if y == "*":
    print(float(x * z))
if y == "/":
    print(float(x / z))
