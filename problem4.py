first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

for num in range(1, 100):
    if num % first_number == 0 and num % second_number == 0:
        print("FizzBuzz")
    elif num % first_number == 0:
        print("Fizz")
    elif num % second_number == 0:
        print("Buzz")
    else:
        print(num)
