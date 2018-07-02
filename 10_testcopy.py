import copy

numbers=['1','2','3',['4','5']]
num1=copy.copy(numbers)
num2=copy.deepcopy(numbers)

num1.append('6')

print('numbers:',numbers)
print('numbers memory address:',id(numbers))
print('numbers[3] memory address',id(numbers[3]))
print('num1:',num1)
print('num1 memory address:',id(num1))
print('num1[3] memory address',id(num1[3]))
print('num1[4] memory address',id(num1[4]))
print('num2:',num2)
print('num2 memory address:',id(num2))
print('num2[3] memory address',id(num2[3]))


num1[3].append('6')

print('numbers:',numbers)
print('num1:',num1)
print('num2',num2)


