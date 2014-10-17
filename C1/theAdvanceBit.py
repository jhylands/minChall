#function to get the number 
def get_number():
	number = int(raw_input("Please enter the number you want to chech for primeness"))
	return number

#function to get if a number is prime 
def isprime(number):
	#check devisers from 1
	n = 2
	while n<=number ** 0.5:
		if number % n == 0:
			#the number is not prime retun False and use the return to break out of the function 
			return False
		#incraese the divider
		n +=1
	#no factors have been found the number must be prime
	return True

def main():
	number = get_number()
	if isprime(number):
		print "The number is prime"
	else:
		print "The number is not prime"

main()
