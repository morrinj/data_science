#membership operators
fruits = ['apple', 'banana', 'cherry']
print ('apple' in fruits)  # True
print ('mango' not in fruits)  # True

#works on strings
print('ello'in 'Hello')

#works on dicts 
d ={'a': 1, 'b':2}
print('a'in d)
print(1 in d)  # False, checks keys only
print(1 in d.values())  # True, checks values

#identity operators
#use 'is' ONLY for none,true ,false
x = None
print(x is None)  # True
 #Warning: 'is' vs '=='
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True
print(a is b)  # False
print(a is c)  # True