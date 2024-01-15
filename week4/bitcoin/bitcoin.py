import sys
import requests


def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        price = response.json()["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()
    
    if len(sys.argv) == 2:
        try:
            nos = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

    amount = price * nos
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()