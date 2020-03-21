chisla = ["10","15","20"]
while True:
	n = input("Отгадайте число: ")
	if n in chisla:
		print("Вы угадали!")
	elif n == "X":
		break
	else:
		print("Провал...")
		