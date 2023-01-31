import random
import operator
ops: dict = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv

             }


class Math:
    bin_operator = '+'

    def __init__(self, floor, ceil) -> None:
        self.floor = floor
        self.ceil = ceil

    def get_problem(self):
        number1 = random.randint(self.floor, self.ceil)
        number2 = random.randint(self.floor, self.ceil)
        print(f'Your problem is {number1} {self.bin_operator} {number2}')
        guess = int(input('Enter your answer: '))
        answer = ops[self.bin_operator](number1, number2)
        if guess == answer:
            return 'Right'
        return f'Mistake, correct answer is {answer}'


class Sub(Math):
    bin_operator = '-'


class Mul(Math):
    bin_operator = '*'


class Div(Math):
    bin_operator = '/'

    def get_problem(self):
        while True:
            number1 = random.randint(self.floor, self.ceil)
            number2 = random.randint(self.floor, self.ceil)
            if number2 % number1 == 0:
                break
        print(f'Your problem is {number2} {self.bin_operator} {number1}')
        guess = int(input('Enter your answer: '))
        answer = ops[self.bin_operator](number2, number1)
        if guess == answer:
            return 'Right'
        return f'Mistake, correct answer is {answer}'


relationships: dict = {'+': Math,
                       '-': Sub,
                       '*': Mul,
                       '/': Div}

print('Hey, its new math game.')
while True:
    opeartor = input('Choose game mode, for it, choose operator: ')
    floor = int(input('Choose floor of interval: '))
    ceil = int(input('Choose ceil of interval: '))
    quantity = int(input('Choose quantity of problems in one level: '))
    for i in range(quantity):
        object = relationships[opeartor](floor, ceil)
        print(object.get_problem())
    print()
    print('Level end')
