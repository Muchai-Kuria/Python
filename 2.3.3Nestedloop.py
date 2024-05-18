for y in range(3):
    for x in range(1,10):
        print(x, end=" ")
    print()

#Example 2
rows = int(input("How Many Rows: "))
columns = int(input("How Many Columns: "))
symbol = input("Enter a symbol:")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()    

