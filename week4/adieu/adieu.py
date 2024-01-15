def main():
    names = []
    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            if len(names) == 1:
                print(f"\nAdieu, adieu, to {names[0]}")
                break
            if len(names) == 2:
                print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")
                break
            print("\nAdieu, adieu, to", end="")
            for name in names[:-1]:
                print(f" {name},", end='')
            print(f" and {names[-1]}")
            break

if __name__ == "__main__":
    main()