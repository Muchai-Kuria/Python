#Funcion 1
def hello(name):
    print("Hello, " + name + "!")

hello("Lee")    

#Function 2
def invoice(name, amount, date):
    print(f"Invoice for {name} for $ {amount:.2f} is due on {date}.")

invoice("James", 100.20," 12/05/2024")

#Function 3 -- Performing function
def greetings(name):
    print(f"Hello {name}")

greetings("Lee")

#Function 4 -- Returning
def say_hello(name):
    return f"Hello {name}"

print(say_hello("Muchai"))

#Keywords
def increment(no, by=2): # 2 is acing as default number.
    return no + by

print(increment(3,1))

# Multiplication
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1,5,10,6))    

#Saving in a dictionary
def save_user(**user):
    print(user)

save_user(ID = 1, Age = 20, Name = "Lee", Email = "leemuchai30@gmail.com" )

