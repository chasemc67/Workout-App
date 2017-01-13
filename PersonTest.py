from Person import Person

person = Person()
person.jumpHeight = 200
person.bodyMass = 65

#print("getVertJump: " + str(person.getVertJump()))
assert person.getVertJump() == 13029.5

person.sumOfFolds = 10
person.age = 20
print("getBodyFatThreeFemale: " + str(person.getBodyFatThreeFemale()))
