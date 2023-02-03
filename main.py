from replit import clear

logo = """     _____________________
	|  _________________  |
	| |              0. | |
	| |_________________| |
	|  ___ ___ ___   ___  |
	| | 7 | 8 | 9 | | + | |
	| |___|___|___| |___| |
	| | 4 | 5 | 6 | | - | |
	| |___|___|___| |___| |
	| | 1 | 2 | 3 | | x | |
	| |___|___|___| |___| |
	| | . | 0 | = | | / | |
	| |___|___|___| |___| |
	|_____________________| """


def addition(num1, num2):
	return num1 + num2


def subtraction(num1, num2):
	return num1 - num2


def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	return num1 / num2


opDict = {"+": addition, "-": subtraction, "*": multiply, "/": divide}


def calculator(dictionary):
	print(logo)
	inputx = float(input("  Enter your first number"))
	keepCalculating = True
	for symbol in opDict:
		print(symbol)
	keepCalculating = True

	while keepCalculating:
		choice = input("Choose a symbol from above")
		inputy = float(input("Enter your second number"))
		usOp = dictionary[choice]
		product = usOp(inputx, inputy)
		print(f"{inputx} {choice} {inputy} = {product}")

		if input(
		  f"Enter y to make another calculation with {product} or type n to start another calculation?: "
		).lower() == "y":
			inputx = product
		else:
			keepCalculating = False
			clear()
			calculator(opDict)


calculator(opDict)
