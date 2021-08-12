class Intern:

    def __init__(self, Name=None):
        if Name is None:
            self.Name = "My name? I’m nobody, an intern, I have no name."
        else:
            self.Name = Name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


def tests():
    intern = Intern()
    print(intern)
    test = Intern("test")
    print(test)
    try:
        intern.work()
        print("here")
    except Exception as e:
        print(e)
    print(test.make_coffee())


if __name__ == '__main__':
    tests()
