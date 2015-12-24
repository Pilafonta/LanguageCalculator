'''
pilafonta
12/6/15

acts like a normal calculator, but the answers are in German
will add other languages as I learn them (or remember them)

'''

numbers = {0:'', 1:'ein', 2:'zwei', 3:'drei', 4:'vier', 5:'fünf', 6:'sechs', 7:'sieben', 8:'acht',
9:'neun', 10:'zehn', 11:'elf', 12:'zwölf', 20:'zwanzig', 30:'dreißig', 40:'vierzig', 50:'fünfzig',
60:'sechzig', 70:'siebzig', 80:'achtzig', 90:'neunzig', 100:'hundert', 1000:'tausend',
1000000:'million', 1000000000:'milliarde'}

def inp():
	x = input("Please enter a number 1-999: ")
	one = int(x)%10
	ten = (int(x)%100)-one
	hundred = int(int(x)/100)
	if(int(x)<=12):
		print(numbers[int(x)])
	if(int(x)>=13 and int(x)<20):
		print(numbers[one] + numbers[10])
	if(int(x)>=20 and int(x)<=99):
		if(one==0):
			print(numbers[int(x)])
		else:
			print(numbers[one]+"und"+numbers[ten])
	if(int(x)>=100 and int(x)<1000):
		#print(numbers[hundred])
		if(int(x) == 101):
			print(numbers[hundred]+numbers[100]+'eins')
		elif(one>0 and ten==0):
			print(numbers[hundred]+numbers[100]+numbers[one])
		elif(one==0 and ten>0):
			print(numbers[hundred]+numbers[100]+numbers[ten])
		elif(one>0 and ten>0):
			print(numbers[hundred]+numbers[100]+numbers[one]+"und"+numbers[ten])
		else:
			hundred = (int(x)/100)
			print(numbers[hundred]+numbers[100])

	

cont = True
while(cont):
	inp()
	print()
	c = input("Would you like to contine?(y/n) ")
	if(c == 'n'):
		cont = False
