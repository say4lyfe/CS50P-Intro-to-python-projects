camelCase = input("camelCase: ")
x = list(camelCase)
for char in camelCase:
    if char.isupper():
        i = x.index(char)
        x.insert(i, "_")
snake_case = "".join(x)
print(snake_case.lower())