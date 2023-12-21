def check(a, b):
    if not (a.isupper() or b.isupper()):
        return -1  
    if a.islower() == b.islower():
        return 1  
    else:
        return 0 

print(check('0', '1'))  
print(check('A', 'C')) 
print(check('b', 'G')) 