def greet():
    print('Hello, Data Science!')
 
greet()   # call the function '+' Hello, Data Science!
 
# Function with parameters
def greet_person(name):
    print(f'Hello, {name}!')
 
greet_person('Alice')   # Hello, Alice!
greet_person('Bob')     # Hello, Bob!
 
# Function with return value
def square(n):
    return n ** 2
 
result = square(7)
print(result)   # 49
 
# Function with multiple parameters
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)
 
print(calculate_bmi(70, 1.75))   # 22.9
