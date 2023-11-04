str = input("Expression: ").strip()
exp = str.split()
if exp[1] == '+':
    print(float(exp[0]) + float(exp[2]))
elif exp[1] == '-':
    print(float(exp[0]) - float(exp[2]))
elif exp[1] == '*':
    print(float(exp[0]) * float(exp[2]))
elif exp[1] == '/':
    print(float(exp[0]) / float(exp[2]))