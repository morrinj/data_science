student = {'name': 'Alice', 'age': 22, 'gpa': 3.8}
 
# READ — access by key
print(student['name'])    # 'Alice'
 
# KeyError if key doesn't exist:
# student['email']  →  KeyError: 'email'
 
# Safe access with get() — returns None (or a default) if missing
print(student.get('email'))            # None
print(student.get('email', 'N/A'))    # 'N/A'
 
# CREATE / UPDATE — add or change a key
student['email'] = 'alice@uni.ac.rw'  # add new key
student['age']   = 23                 # update existing key
 
# Update multiple keys at once
student.update({'age': 24, 'gpa': 3.9})
 
# DELETE
del student['email']
gpa = student.pop('gpa')   # removes and returns the value
 
# Check key existence
print('name' in student)   # True
print('gpa' in student)    # False (we just removed it)
