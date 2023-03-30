Number Guessing Game
This is a simple number guessing game in which the computer generates a random number between 0 and 100, and the user has to guess that number. The program will give feedback to the user after each guess, indicating whether the user's guess is too high or too low.

How to Play
The program will generate a random number between 0 and 100.
The user will be prompted to enter their guess.
The program will check if the guess is too high or too low and provide feedback to the user accordingly.
The user will continue guessing until they guess the correct number.
Once the user guesses the correct number, the program will output the number of guesses it took for the user to get the correct answer.
Code Explanation
import random : Imports the random module to generate a random number.
guess = random.randint(0, 100) : Generates a random number between 0 and 100.
user = int(input("Enter your Number : ")) : Prompts the user to enter their guess and stores it as an integer in the variable user.
count = 0 : Initializes the count variable to keep track of the number of guesses.
while guess != user: : Enters a loop that continues until the user guesses the correct number.
if guess < user: : Checks if the user's guess is too high.
print("Too high") : Outputs "Too high" to provide feedback to the user.
count += 1 : Increments the count variable by 1 to keep track of the number of guesses.
user = int(input("Enter your Number : ")) : Prompts the user to enter another guess and stores it as an integer in the variable user.
elif guess > user: : Checks if the user's guess is too low.
print("Too low") : Outputs "Too low" to provide feedback to the user.
count += 1 : Increments the count variable by 1 to keep track of the number of guesses.
user = int(input("Enter your Number : ")) : Prompts the user to enter another guess and stores it as an integer in the variable user.
print(f"Just right in {count + 1} time") : Outputs the number of guesses it took the user to get the correct answer.