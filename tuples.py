# Empty tuple
t0 = ()
t1 = (42,)       # This IS a tuple
t2 = (42)        
print(type(t0))
print(type(t1))
print(type(t2))
# Multi-element tuples
coords   = (10.5, 20.3)           # latitude, longitude
person   = ('Alice', 30, 'F')     # name, age, gender
rgb      = (255, 128, 0)          # red-green-blue colour
mixed    = (1, 'hello', True)

print(coords)
print(person)
print(rgb)
print(mixed)
# Tuple packing — parentheses are optional
point = 3, 4                      
print(point)
# Convert other sequences to tuple
from_list = tuple([1, 2, 3])      # (1, 2, 3)
from_str  = tuple('abc')          # ('a', 'b', 'c')
 
print(from_list)
print(from_str)
print(type(coords))   # <class 'tuple'>
print(type(from_list)) # <class 'tuple'>