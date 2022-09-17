"""
Owen Heuschele
9/16/2022

This code calculates the number of perfect, abundant, and deficient numbers
within a range given an upper bound.
"""

#Takes the upper bound
upperBound = int(input("Enter an upper bound for a check: "))

#Define variables
defCount = 0
perfCount = 0
abunCount = 0

#Checks each number in the range for proper divisors, then determines 
#whether the number is deficient, perfect, or abundant.
for number in range(1, (upperBound + 1)):
	
	#Resets the sum of proper divisors
	propDiv = 0
	
	for value in range(1, number):
		
		#Checks a number in range for proper divisors and adds them to a sum
		if (number % value) == 0:
			propDiv += value
			
	#Checks the sum of proper divisors to determine whether the number is deficient, perfect, or abundant
	if propDiv < number:
		defCount += 1
		
	elif propDiv == number:
		perfCount += 1
		
	elif propDiv > number:
		abunCount += 1
		
#Print the results			
print(f"Between 1 and {upperBound} there are")
print(f"   {defCount} deficient numbers")
print(f"   {perfCount} perfect numbers")
print(f"   {abunCount} abundant numbers")
