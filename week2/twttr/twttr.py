str = input("Input: ").strip()
ovl = ['a', 'e','i','o','u','A','E','I','O','U']
print("Output: ", end='')
for i in str:
    if i not in ovl:
        print(i, end='')