import sys


def print_capital_city(state):
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
    if states.get(state):
        print(capital_cities[states[state]])
    else:
        print("Unknown state")


def main():
    if len(sys.argv) == 2:
        print_capital_city(sys.argv[1])

if __name__ == '__main__':
    main()
