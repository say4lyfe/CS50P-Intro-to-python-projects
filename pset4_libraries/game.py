import random
while True:
    try:
        lvl = int(input("Level: "))
        if lvl <= 0:
            continue
        else:
            n = random.randint(1, lvl)
            while True:
                guess = int(input("Guess:"))
                if guess <= 0:
                    continue
                if guess < n:
                    print("Too small!")
                elif guess > n:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        break

    except(ValueError):
        continue