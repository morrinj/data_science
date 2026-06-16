# Default parameter values
def power(base, exponent=2):   # exponent defaults to 2
    return base ** exponent
 
print(power(3))       # 9    — uses default exponent=2
print(power(3, 3))    # 27   — overrides default
print(power(2, 10))   # 1024
 
# Keyword arguments — pass by name, any order
def describe(name, age, school):
    return f'{name}, age {age}, at {school}'
 
describe(age=22, school='SBITE', name='Alice')   # order irrelevant
 
# *args — accept ANY number of positional arguments
def total(*numbers):
    return sum(numbers)
 
print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100
 
# **kwargs — accept ANY number of keyword arguments
def show_info(**details):
    for key, value in details.items():
        print(f'  {key}: {value}')
 
show_info(name='Alice', score=92, city='Kigali')
#   name: Alice
#   score: 92
#   city: Kigali
