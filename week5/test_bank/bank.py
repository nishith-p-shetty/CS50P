def main():
    str = input("Greeting: ").strip()
    print(value(str))

def value(greeting):
    if greeting[0].lower() != 'h':
        return("$100")
    else:
        if greeting.split(',')[0].lower() == "hello":
            return("$0")
        else:
            return("$20")


if __name__ == "__main__":
    main()