import random
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate


class CoffeeMachine:

    def __init__(self):
        self.reserve = 10

    def repair(self):
        self.reserve = 10

    class EmptyCup(HotBeverage):

        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):

        def __init__(self):
            super().__init__(self, "This coffee machine has to be repaired.")

    def serve(self, drink):
        if self.reserve <= 0:
            raise CoffeeMachine.BrokenMachineException
        elif random.random() < .5:
            self.reserve -= 1
            return CoffeeMachine.EmptyCup()
        else:
            self.reserve -= 1
        return drink()


def tests():
    machine = CoffeeMachine()

    for _ in range(22):
        try:
            print(machine.serve(random.choice(
                [Coffee, Tea, Cappuccino, Chocolate])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            machine.repair()


if __name__ == '__main__':
    tests()
