import sys
import csv

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1], 'r') as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], 'w') as opf:
                    writer = csv.DictWriter(opf, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for r in reader:
                        lname, fname = r['name'].split(',')
                        writer.writerow({"first": fname.strip(), "last": lname.strip(), "house": r['house']})
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()