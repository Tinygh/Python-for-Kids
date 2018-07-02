import copy
class Car:
	"""docstring for Car __init__(self, arg)"""
	pass
car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

print(car2.wheels)
print(car3.wheels)
print('memory address')
print('car1 memorry address:',id(car1))
print('car2 memorry address:',id(car2))
print('car3 memorry address:',id(car3))
