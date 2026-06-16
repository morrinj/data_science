age = 22
income = 50000
has_id = True

# compound condition
eligible = age >= 18 and income >= 30000 and has_id
print(eligible)  # True

#short-circuit evaluation
def risky():raise Expection('called!')
print(False and risky())

#'or' stops at first True
print(True or risky())

#practical: provide a default value
name = "or 'Anonymous'"
print(name)

#operator precedence : not > and > or 
print (True or False and False )
print((True or False) and False)

    