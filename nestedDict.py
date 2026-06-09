students = {
    'STU001': {
        'name':   'Alice Doe',
        'school': 'SBITE',
        'grades': {'Data Science': 88, 'ML': 92},
        'active': True
    },
    'STU002': {
        'name':   'Bob Smith',
        'school': 'SNHS',
        'grades': {'Biology': 79, 'Chemistry': 83},
        'active': False
    }
}
 
# Access nested values
print(students['STU001']['name'])              # 'Alice Doe'
print(students['STU001']['grades']['ML'])      # 92
 
# Safe nested access
ml = students.get('STU001',{}).get('grades',{}).get('ML','N/A')
 
# Iterate over all students
for sid, info in students.items():
    print(f"{sid}: {info['name']} — Active: {info['active']}")
