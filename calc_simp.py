#Function that test if the given string is a common operation.
def calc_test(resp):
	if resp == 'som' or resp == 'sub' or resp == 'mult' or resp == 'div':
		return resp
	else:
		return 'again'
#The beginning of the code. Resp is the variable that get what operation will be done.

resp = calc_test(input('qual operacao ---->'))

while resp == 'again':
	resp = calc_test(input('vamo... operacao ---->'))

num1 = float(input('coloque aqui o primeiro numero ---->'))
num2 = float(input('coloque o segundo ----->'))

if resp == 'som':
	print (num1 + num2)
elif resp == 'sub':
	print (num1 - num2)
elif resp == 'div':
	print (num1 / num2)
else:
	print (num1 * num2)

