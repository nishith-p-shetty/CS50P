def main():
    items = {}
    while True:
        try:
            item = input().strip().upper()
            if item not in items:
                items[item] = 1
            else:
                items[item] = items[item]+1
        except EOFError:
            for i in sorted(items):
                print(f"{items[i]} {i}")
            break
        except KeyError:
            pass
    
main()