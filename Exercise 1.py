'''
Takes an Input
if divisible by 3 return = Fizz
                by 5 return = Buzz
                by both return = FizzBuzz
                other numbers return the number
'''
number = int(input("Enter a Number :"))

def divisible(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")

divisible(number)