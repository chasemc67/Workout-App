from Person import Person

person = Person()

person.weight = 5
person.height = 10

print(person.getBMI())
assert(person.getBMI() == 0.05)
