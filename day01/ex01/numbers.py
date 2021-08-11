def parse_file():
    fd = open('numbers.txt', 'r')
    line = fd.read().replace('\n', '').replace(',', '\n')
    print(line)
    fd.close()

if __name__ == '__main__':
    parse_file()
