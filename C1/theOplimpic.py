#get the number as imput from the user
def get_number():
	number = int(raw_input("Please enter the number in which you which to find the product of it's unique prime factors"))
	return number	

def get_prime_factors(number):
	factors = ()
	n = 2
	working_value = number
	for n in xrange(2,number):
		while working_value % n == 0:
			working_value = working_value/n	
			factors = factors + (n,)
		if working_value<n:
			#this will be the case at some point unless the number is prime
			return factors
	return factors
#fucntion to find the product of a list of numbers 
def product(alist):
	the_product = 1
	for element in alist:
		the_product = the_product * element
	return the_product

def main():
	number = get_number()
	#get prime factors and use set to find the unique ones 
	prime_factors = get_prime_factors(number)
	print prime_factors
	prime_factors = list(set(prime_factors))
	#find the product 
	product_primes = product(prime_factors)
	#return the result
	print "The product of the unique prime factors is " , product_primes

main()


#The lowest number that devides into "number" will be prime
