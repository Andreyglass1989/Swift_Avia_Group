none_zero = 0
zero = 0
for item in labels:
	if item == 0:
		zero += 1
		print(zero)
	else:
		none_zero += 1
		print(none_zero)

print(zero, none_zero )