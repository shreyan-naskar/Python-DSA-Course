
#Function to calculate x raised to the power y
def Power( x , y ) :

	if (y == 0) :
		return 1

	else :

		ans = x**y 
		return ans


#Function to convert Binary to Decimal
def BinaryToDecimal( n ) :

	ans = 0
	x   = 1
	m = int(n)

	while m > 0 :
		b   =  m%10
		ans += b*x
		x   =  x*2
		m   =  m//10

	return ans


#Function to convert Octal to Decimal
def OctalToDecimal( n ) :

	ans = 0
	x   = 1
	m = int(n)

	while m > 0 :
		b   =  m%10
		ans += b*x
		x   =  x*8
		m   =  m//10

	return ans


#Function to convert Hexadecimal to Decimal
def HexadecimalToDecimal( n ):

	ans = 0
	x   = 1
	s = len( n )
	
	for i in range( s-1 , -1 , -1 ) :
		if n[i] >= '0' and n[i] <= '9' :
			ans += x*(int(n[i]))

		elif n[i] >= 'A' and n[i] <= 'F' :
			ans += x*(ord(n[i]) - ord('A') + 10)

		x = x*16

	return ans


#Function to convert Decimal to Binary
def DecimalToBinary( n ) :

	x   = 10
	ans = 0

	while (x <= n) :
		x = x*2 

	x = x//2

	while (x > 0) :
		lastDigit = n/x 
		n = n - lastDigit*x
		x = x//2
		ans = ans*10 + lastDigit

	return ans


#Function to convert Decimal to Octal
def DecimalToOctal( n ) :
	
	ans   = 0
	count = 0

	while (n > 0) :
		lastDigit =  n%8
		ans       += lastDigit*(10**(count))
		n         =  n//8

		count     += 1

	return ans


#Function to convert Decimal to Hexadecimal
def DecimaltoHexadecimal( n ) :

	ans = ''

	while (n > 0) :
		lastDigit = n%16
		if (lastDigit >= 0 and lastDigit <=9 ) :
			ans = ans + str(lastDigit)

		elif (lastDigit >= 10 and lastDigit <= 15) :
			a = chr(ord('A') + (lastDigit-10))
			ans = ans + a

		n = n//16

	return ans[::-1]

