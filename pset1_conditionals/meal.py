def main():
    meal = input("what time is it? ")
    if 7.0 <= convert(meal) <= 8.0:
        print("breakfast time")
    if 12.0 <= convert(meal) <= 13.0:
        print("lunch time")
    if 18.0 <= convert(meal) <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return float(hours + minutes)

if __name__ == "__main__":
    main()