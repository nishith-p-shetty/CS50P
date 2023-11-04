def main():
    str = input("What time is it? ").strip()
    ct = convert(str)
    if 7.0 <= ct <= 8.0:
        print("breakfast time")
    elif 12.0 <= ct <= 13.0:
        print("lunch time")
    elif 18.0 <= ct <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()