import os

def main():
	b = int()
	p = int()
	m = int()
	try:
		os.system("cls")
		phrase1 = "The equation is of the form b^p%m"
		phrase2 = "Input your values: "
		print(phrase1)
		print(phrase2, end="")

		b = int(input())
		os.system("cls")
		print("{}\n{}{}{}".format(phrase1, phrase2, b, "^"), end="")

		p = int(input())
		os.system("cls")
		print("{}\n{}{}{}{}{}".format(phrase1, phrase2, b, "^", p, "%"), end="")

		m = int(input())
		
		if b < 0 or p < 0 or m < 0:
			m = int("error") # only positive values are accepted
	except ValueError:
		os.system("cls")
		print("Invalid input.", end="\n\n")
		main()

	binary = binary_expansion(p)
	
	x = 1
	power = b % m
	for i in range(0, len(binary)):
		if binary[i] is 1:
			x = (x * power) % m
		power = (power * power) % m

	print("{}^{}%{}={}".format(b, p, m, x))

def binary_expansion(decimal):
	binary = [ ]
	while decimal > 0: # decimal must already be positive
		if decimal % 2 is 0:
			binary.append(1)
		else:
			binary.append(0)
		decimal //= 2
	return binary

if __name__ == '__main__':
	main()
