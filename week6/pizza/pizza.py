import sys
import csv
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()