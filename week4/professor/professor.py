import random

def main():
    prob = 0
    score = 0
    wrng = 0
    while True:
        try:
            lvl = get_level()
            x, y = generate_integer(lvl)
            while prob < 10:
                if wrng != 3:
                    ans = int(input(f"{x} + {y} = "))
                    if x+y == ans:
                        score += 1
                        prob += 1
                        wrng = 0
                        x,y = generate_integer(lvl)
                    else:
                        print("EEE")
                        wrng += 1
                else:
                    print(f"{x} + {y} = {x+y}")
                    prob += 1
                    wrng = 0
                    x,y = generate_integer(lvl)
            print(f"Score: {score}")
            break
        except:
            pass

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()