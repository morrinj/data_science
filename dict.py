# Empty dict
d = {}    # or: d = dict()
 
# Dictionary literal
student = {'name': 'Alice', 'age': 22, 'gpa': 3.8}
print(student)   # {'name': 'Alice', 'age': 22, 'gpa': 3.8}
 
# Mixed value types
record = {
    'id':      12345,
    'name':    'Alice Doe',
    'scores':  [85, 92, 78],   # list as value
    'active':  True,
    'email':   None
}
print(record)
# From keyword arguments
d2 = dict(name='Bob', age=25, city='Kigali')
print(d2)   # {'name': 'Bob', 'age': 25, 'city': 'Kigali'}
 
# From a list of (key, value) pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
d3 = dict(pairs)   # {'a': 1, 'b': 2, 'c': 3}
print(d3)