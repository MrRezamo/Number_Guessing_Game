import random


guess = random.randint(0, 100)
user = int(input("Enter your Number : "))
count = 0
while guess != user:
    if guess < user:
        print("Too high")
        count += 1
        print(count)
        user = int(input("Enter your Number : "))
    elif guess > user:
        print("Too low")
        count += 1
        print(count)
        user = int(input("Enter your Number : "))

print(f"Just right in {count + 1} time")
