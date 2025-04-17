from random import randint as generate_number, choice
import utils.calculator as calc
from utils.templates import Person


print(calc.multiplication(7, 2))

print(generate_number(1, 10))
print(choice([1, 2, 3]))


friend = Person("Jane", 25)
print(friend)