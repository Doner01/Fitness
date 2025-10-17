print("--- Triangle Pattern Printer ---")

height = int(input("Enter the desired height of the triangle: "))

for num in range(1, height+1):
    print("*"*num, end="")
    print()

