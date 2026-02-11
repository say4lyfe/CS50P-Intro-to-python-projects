def main():
    fraction = convert(input("Fraction: "))
    print(gauge(fraction))

def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")

        x = int(numerator)
        y = int(denominator)

        if x < 0 or y <= 0 or x > y:
            raise ValueError

        return round((x / y) * 100)

    except (ValueError, ZeroDivisionError):
        raise ValueError

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage:.0f}%"

    elif 0 <= percentage <= 1:
        return "E"

    elif 99 <= percentage <= 100:
        return "F"

if __name__ == "__main__":
    main()
