#1
for x in range(1,11):
    print(x)

#2
for x in reversed(range(1,5)):
    print(x)

#3
for x in range(1,11,3):#steps
    print(x)

#4
for x in range(1,11):#skipping a number
    if x == 3:
        continue
    else:
        print(x)