import random
from fractions import Fraction

print("Welcome to the Fractions Game!")
print()
print("-" * 30)
print("Choose your operation:")
print("1 - Multiplication")
print("2 - Addition")
print("3 - Subtraction")
print("4 - Division")
operation = int(input("Operation:"))
print("-" * 30)
print()
print("Choose a level:")
print("1 - Easy")
print("2 - Difficult")
# ask for level
level = int(input("Level: "))
print("-" * 30)
print()

limit = 10
# the difficult level;
if level == 2:
	limit = 100

count = 0

while count < 5:
	print()
	count = count + 1

	first_n = random.randrange(0, limit)
	first_d = random.randrange(1, limit)
	first = Fraction(first_n, first_d)

	sec_n = random.randrange(0, limit)
	sec_d = random.randrange(1, limit)
	second = Fraction(sec_n, sec_d)

	while second.denominator == 1:
		sec_n = random.randrange(0, limit)
		sec_d = random.randrange(1, limit)
		second = Fraction(sec_n, sec_d)

	# if the user chooses multiplication
	if operation == 1:
		print(f"Calculate {first} x {second}")
		correct = first * second
	# if the user chooses addition
	if operation == 2:
		print(f"Calculate {first} + {second}")
		correct = first + second
		# if the user chooses subtraction
	if operation == 3:
		print(f"Calculate {first} - {second}")
		correct = first - second
		# if the user chooses division
	if operation == 4:
		print(f"Calculate {first} ÷ {second}")
		correct = first / second

	given = Fraction(input(f"Your Answer: "))

	if given == correct:
		print(f"{given} is the correct answer!")
	else:
		print(f"You're wrong. The correct answer is {correct}")
		print("Game Over!")
		exit()

print("You Win! You're good at this!")

