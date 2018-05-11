

while 1:

	try:
		 x = input('Enter a number: ')
	except:
		break
	

	kertoma = 0
	for i in range(1, x+1):
		kertoma += i
	
	print kertoma
