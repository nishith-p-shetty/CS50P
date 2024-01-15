import emoji

def main():
    while True:
        try:
            str = input("Input: :")
            print(emoji.emojize('Output: :'+str.strip(), language='alias'))
            break
        except:
            pass

if __name__ == "__main__":
    main()