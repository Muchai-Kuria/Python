#Logical and = both conditions have to be true
x = 10 
y = 20
z = 30

if x>y and x>z:
    print("X is greater than y and Z")
else:
    print("X is not greater than Y or Z")

#Logical or = any of the condition have to be true

if  x<y or x<z:
    print("X is lesser than either of Y or Z")
else:
    print("X is neither lesser than Y nor Z")  

#Logical NOT = returns true is the condition is false and viceversa

if not(x>y or x>z):
    print("Neither X is greater than Y nor Z")
else:
    print("X is larger than Y and Z")
