import random


def main():
    score = 0
    n = get_level()
    i = 0
    while i < 10:
        x = generate_integer(n)
        y = generate_integer(n)
        for _ in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                z = x + y
                if ans != z:
                    print("EEE")
                    continue
                else:
                    break
            except(ValueError):
                print("EEE")
        if ans != z:
            print(f"{x} + {y} = {z}")
        if ans == z:
            score = score + 1
        i = i + 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            num = int(input("Level: "))
            if 0 < num < 4:
                return num
            else:
                continue
        except(ValueError):
            continue

def generate_integer(level):
    if level == 1:
        value = random.randint(0,9)
    else:
        value = random.randint(10**(level - 1), 10**level - 1)
    return value

if __name__ == "__main__":
    main()