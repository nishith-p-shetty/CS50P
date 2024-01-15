import random

def main():
    guess, rand = -1, -2
    while guess != rand:
        try:
            lvl = input("Level: ").strip()
            lvl = int(lvl)
            if lvl < 1:
                continue
        except:
            pass
        else:
            rand = random.randint(1, lvl)
            guess = -1
            while guess != rand:
                try:
                    guess = int(input("Guess: ").strip())
                    if guess == rand:
                        print("Just right!")
                        break
                    elif guess > rand:
                        print("Too large!")
                    else:
                        print("Too small!")
                except:
                    pass


if __name__ == "__main__":
    main()