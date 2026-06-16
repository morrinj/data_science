def greet():
    print('Hello, Data Science!')
    greet()
# function with parameters
def greet_person(name):
    print(f'Hello, {name}!')
greet_person('Alice')
greet_person('Bob')
