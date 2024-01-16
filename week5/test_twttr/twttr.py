def main():
    str = input("Input: ").strip()
    sword = shorten(str)
    print(f"Output: {sword}")



def shorten(word):
    sword = ""
    ovl = ['a', 'e','i','o','u','A','E','I','O','U']
    for i in word:
        if i not in ovl:
            sword += i
    return sword

if __name__ == "__main__":
    main()