import sys


def get_key_from_value(dictionary, needed_value):
    for key, item in dictionary.items():
        if item == needed_value:
            return key
    return None


def print_capital_city(city):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    check = get_key_from_value(capital_cities, city)
    if check:
        print(get_key_from_value(states, check))
    else:
        print("Unknown capital city")


def main():
    if len(sys.argv) == 2:
        print_capital_city(sys.argv[1])

if __name__ == '__main__':
    main()
