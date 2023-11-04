str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
accepted_str = ["42", "Forty Two", "forty-two", "forty two"]
if str.strip().lower().replace('-', ' ') in accepted_str:
    print("Yes")
else:
    print("No")