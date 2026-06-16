def print_hello():
    print('Hello')
 
result = print_hello()   # prints Hello
print(result)            # None
 
# Return multiple values — returned as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)
 
lo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f'Min: {lo}, Max: {hi}')   # Min: 1, Max: 9
 
# Early return — exit the function before reaching the end
def safe_divide(a, b):
    if b == 0:
        return None   # early return avoids ZeroDivisionError
    return a / b
 
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None
