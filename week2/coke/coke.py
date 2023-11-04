chg = 50
print(f"Amount Due: {chg}")
while chg > 0:
    str = int(input("Insert Coin: "))
    if str == 25:
        chg -= 25
    elif str == 10:
        chg -= 10
    elif str == 5:
        chg -= 5
    print(f"Amount Due: {chg}")
if chg == 0:
    print(f"Change Owed: {chg}")
else:
    chg*=-1
    print(f"Change Owed: {chg}")