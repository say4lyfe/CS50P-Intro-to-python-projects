import sys

code = []
not_code = []
i = 0

while True:
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        if sys.argv[1].endswith("py"):
            with open (sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith("#"):
                        not_code.append(line)
                    elif line.strip() != "":
                        code.append(line)
                        i = i + 1
            print(i)
            break

        else:
            sys.exit("Not a Python file")

    except(FileNotFoundError):
        sys.exit("File does not exist")