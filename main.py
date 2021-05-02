# Simple Word Comparer

# Variables
value1 = input('Please enter the 1st value -> ')
print()
value2 = input('Please enter the 2nd value -> ')

is_num_value1 = value1.isdigit()
is_num_value2 = value2.isdigit()

print('')

# Logic
if value1 == value2:
	print('The values entered are the same!')
elif is_num_value1 and is_num_value2:
	if int(value1) == int(value2):
		print('The values entered are the same!')
else:
	print('The values entered are not the same!')