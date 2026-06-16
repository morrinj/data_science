x = 'global'
 
def outer():
    x = 'enclosing'
 
    def inner():
        x = 'local'
        print(x)    # 'local'  — uses innermost x
 
    inner()
    print(x)    # 'enclosing'
 
outer()
print(x)    # 'global'
 
# global keyword — modify a global variable inside a function
count = 0
def increment():
    global count
    count += 1
 
increment(); increment()
print(count)   # 2
