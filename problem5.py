count = int(input("How many numbers? "))

first = 0
second = 1

print("Fibonacci sequence:")

for i in range(count):
    print(first)
    next_number = first + second
    first = second
    second = next_number
