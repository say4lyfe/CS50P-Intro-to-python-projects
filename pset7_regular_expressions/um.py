import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    i = 0
    find = re.findall(r"\bum\b", s, re.IGNORECASE)
    for um in find:
        i = i+ 1
    return i
        


if __name__ == "__main__":
    main()