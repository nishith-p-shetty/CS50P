import sys

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            with open(sys.argv[1], 'r') as file:
                lines = file.readlines()
                count = 0
                for line in lines:
                    if not (line.strip().startswith("#") or line.strip()==''):
                        count += 1
                print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()