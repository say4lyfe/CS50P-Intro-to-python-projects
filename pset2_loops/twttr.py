def main():
    long = input("Input: ")
    x = []
    y = []
    for char in long:
        if char in "aeiouAEIOU":
            x.append(char)
        else:
            y.append(char)
    short = "".join(y)
    print(f"Output: {short}")
    
main()