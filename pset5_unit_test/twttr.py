def main():
    big = input("Input: ")
    small = shorten(big)
    print(f"Output: {small}")

def shorten(word):
    x = []
    y = []
    for char in word:
        if char in "aeiouAEIOU":
            x.append(char)
        else:
            y.append(char)
    short = "".join(y)
    return short


if __name__ == "__main__":
    main()
