cc = input("camelCase: ").strip()
print("snake_case: ", end='')
for i in cc:
    if i.islower():
        print(i, end='')
    else:
        print("_", i.lower(), end='', sep='')