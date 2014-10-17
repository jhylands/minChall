#define our list of primes 
primes = (2,)#WARNING LIST MUST BE KEPT IN ASC ORDER!

#get the input from the user 
def get_number():
	number = int(raw_input("What is the number you would like to check for primeness?"))
	return number
#function to check devisibility 
def dvsl(a,b):#if a/b maps to an integer
	return a%b==0
#define fuction to check if the number is prime
def isprime(number):
	global primes
	#loop through known primes
	for prime in primes:
		if dvsl(number,prime):
			return False
#still no factors found:
	#start at the last known prime number and count up (This isn't garateed to find the prime
	n = primes[-1]
	while n<=number**0.5:
		if dvsl(number,n):
			return False
		n+=1
 #still no factors found:
	i = 3
	while i<n ** 0.5:
		#could check that the number wasn't a prime but that would require more procceses than just checking the number twice
		if dvsl(number,i):
			return False
		#increase n
		i+=1
 #still no factors found:
	#it is the reponsibility of the parent function to then add this number to the list of primes
	return True

#function to add prime number to list of known primes 
def add_prime(prime):
	global primes
	n=0
	while prime< primes[n]:
		n+=1
	primes = primes[:n] + (prime,) + primes[n:]

#define a function to call the programs functions 
def check_prime():
	number = get_number()
	if isprime(number):
		add_prime(number)
		print "The number is prime"
	else:
		print "The number is not prime"
#have a function that loops until the use does not wish to check for any more primes
def main():
	more_numbers = True 
	while more_numbers:
		check_prime()
		if raw_input("Do you have more numbers? (y/n)") != "y":
			more_numbers = False

main()
