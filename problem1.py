age = int(input("Enter your age: "))

if age <= 12:
    price = 8
elif age >= 65:
    price = 10
else:
    price = 15

print(f"Your ticket price is {price}$")
