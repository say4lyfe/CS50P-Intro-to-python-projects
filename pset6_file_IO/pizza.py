import csv
import sys
from tabulate import tabulate

table = []

while True:
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        if sys.argv[1].endswith("csv"):
            pizza, _ = sys.argv[1].capitalize().split(".")
            food = f"{pizza} Pizza"
            with open (sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.append({food: row[food], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(table, headers="keys", tablefmt="grid"))
                break
                
        else:
            sys.exit("Not a CSV file")

    except(FileNotFoundError):
        sys.exit("File does not exist")
