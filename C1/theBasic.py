#define list of known prime numbers
primes = (2,3,5,7)

#check if the numbers are prime 
def is_prime(number):
	#start by assuming the number is not prime 
	bool_is_prime = True
	#loop through the known primes
	for prime in primes:
		if number % prime == 0 and number!=prime:
			#the number is not prime
			bool_is_prime = False
	return bool_is_prime

#function to ask the user for a number
def get_number():
	number = int(raw_input("Please enter a number to check if it is prime"))
	return number 

#main function to run the program 
def main():
	number = get_number()
	if is_prime(number):
		print "It's Prime"
	else:
		print "It's not prime"

main()
