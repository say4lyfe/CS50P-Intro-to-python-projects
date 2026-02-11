import sys
import csv

table = []

while True:
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        if sys.argv[1].endswith("csv"):
            with open (sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.append({"name": row["name"], "house": row["house"]})

                fieldnames = ["first", "last", "house"]
                with open (sys.argv[2], "w") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in table:
                        last, first = row["name"].split(",")
                        writer.writerow({"first": first.lstrip(), "last": last, "house": row["house"]})
               
        break

    except(FileNotFoundError):
        sys.exit("Could not read invalid_file.csv")