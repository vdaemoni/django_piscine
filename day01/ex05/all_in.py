import sys


def get_value_by_key(states, capital_cities, needed_key):
    if states.get(needed_key):
        return capital_cities[states[needed_key]]
    return None


def get_key_by_value(dictionary, needed_value):
    for key, item in dictionary.items():
        if item == needed_value:
            return key
    return None


def print_capital_city(parameter):
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
    value = get_value_by_key(states, capital_cities, parameter)
    key = get_key_by_value(capital_cities, parameter)
    if value:
        print(value, "is the capital of", parameter)
    elif key:
        print(parameter, "is the capital of", get_key_by_value(states, key))
    else:
        print(parameter, "is neither a capital city nor a state")


def parse_argv(argv):
    arg_list = argv.split(",")
    for arg in arg_list:
        arg = ' '.join(arg.split())
        if arg == "":
            continue
        print_capital_city(arg.title())


def main():
    if len(sys.argv) == 2:
        parse_argv(sys.argv[1])

if __name__ == '__main__':
    main()
