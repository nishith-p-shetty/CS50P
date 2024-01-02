def get_ans():
    while True:
        try:
            x,y = input("Fraction: ").split('/')
            x = int(x)
            y = int(y)
        except (ValueError, ZeroDivisionError):
                pass
        else:
            if x <= y:
                frac = (x/y)*100
                if frac <= 1:
                    print('E')
                elif frac >= 99:
                    print('F')
                else:
                    print(str(round(frac)) + "%")
                break

get_ans()