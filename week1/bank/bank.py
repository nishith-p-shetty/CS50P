str = input("Greeting: ").strip()
if str[0].lower() != 'h':
    print("$100")
else:
    if str.split(',')[0].lower() == "hello":
        print("$0")
    else:
        print("$20")