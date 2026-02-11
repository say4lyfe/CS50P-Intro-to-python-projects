def main():
    Greet = input("Greeting: ")
    print(value(Greet))


def value(greeting):
    sup = greeting.strip().lower()
    if sup.__contains__("hello"):
        return 0

    elif sup[0] == "h":
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
