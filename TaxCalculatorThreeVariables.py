"""
Owen Heuschele
9/9/2022

This program calculates taxes from three variables
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2022: $"))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")

#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")

depDeduct = int(input("Enter the number of dependents: "))

#Tax calculation if single
if(maritalStatus == "s"):
	
	if(earnedIncome >= 539901):
		taxOwed += (10275 * 0.1)
		taxOwed += ((41775 - 10275) * 0.12)
		taxOwed += ((89075 - 41775) * 0.22)
		taxOwed += ((170050 - 89075) * 0.24)
		taxOwed += ((215950 - 170050) * 0.32)
		taxOwed += ((539900 - 215950) * 0.35)
		earnedIncome -= 539900
		taxOwed += (earnedIncome * 0.37)
		
	elif(earnedIncome >= 215951):
		taxOwed += (10275 * 0.1)
		taxOwed += ((41775 - 10275) * 0.12)
		taxOwed += ((89075 - 41775) * 0.22)
		taxOwed += ((170050 - 89075) * 0.24)
		taxOwed += ((215950 - 170050) * 0.32)
		earnedIncome -= 215950
		taxOwed += (earnedIncome * 0.35)
		
	elif(earnedIncome >= 170051):
		taxOwed += (10275 * 0.1)
		taxOwed += ((41775 - 10275) * 0.12)
		taxOwed += ((89075 - 41775) * 0.22)
		taxOwed += ((170050 - 89075) * 0.24)
		earnedIncome -= 170050
		taxOwed += (earnedIncome * 0.32)
	
	elif(earnedIncome >= 89076):
		taxOwed += (10275 * 0.1)
		taxOwed += ((41775 - 10275) * 0.12)
		taxOwed += ((89075 - 41775) * 0.22)
		earnedIncome -= 89075
		taxOwed += (earnedIncome * 0.24)
		
	elif(earnedIncome >= 41776):
		taxOwed += (10275 * 0.1)
		taxOwed += ((41775 - 10275) * 0.12)
		earnedIncome -= 41775
		taxOwed += (earnedIncome * 0.22)
		
	elif(earnedIncome >= 10276):
		taxOwed += (10275 * 0.1) 
		earnedIncome -= 10275
		taxOwed += (earnedIncome * 0.12)
		
	else:
		taxOwed = (earnedIncome * 0.1)

#Tax calculation if married		
elif(maritalStatus == "m"):
	
	if(earnedIncome >= 647851):
		taxOwed += (20550 * 0.1)
		taxOwed += ((83550 - 20550) * 0.12)
		taxOwed += ((178150 - 83550) * 0.22)
		taxOwed += ((340100 - 178150) * 0.24)
		taxOwed += ((431900 - 340100) * 0.32)
		taxOwed += ((647850 - 431900) * 0.35)
		earnedIncome -= 647850
		taxOwed += (earnedIncome * 0.37)
		
	elif(earnedIncome >= 431901):
		taxOwed += (20550 * 0.1)
		taxOwed += ((83550 - 20550) * 0.12)
		taxOwed += ((178150 - 83550) * 0.22)
		taxOwed += ((340100 - 178150) * 0.24)
		taxOwed += ((431900 - 340100) * 0.32)
		earnedIncome -= 431900
		taxOwed += (earnedIncome * 0.35)
		
	elif(earnedIncome >= 340101):
		taxOwed += (20550 * 0.1)
		taxOwed += ((83550 - 20550) * 0.12)
		taxOwed += ((178150 - 83550) * 0.22)
		taxOwed += ((340100 - 178150) * 0.24)
		earnedIncome -= 340100
		taxOwed += (earnedIncome * 0.32)
	
	elif(earnedIncome >= 178151):
		taxOwed += (20550 * 0.1)
		taxOwed += ((83550 - 20550) * 0.12)
		taxOwed += ((178150 - 83550) * 0.22)
		earnedIncome -= 178150
		taxOwed += (earnedIncome * 0.24)
		
	elif(earnedIncome >= 83551):
		taxOwed += (20550 * 0.1)
		taxOwed += ((83550 - 20550) * 0.12)
		earnedIncome -= 83550
		taxOwed += (earnedIncome * 0.22)
		
	elif(earnedIncome >= 20551):
		taxOwed += (20550 * 0.1)
		earnedIncome -= 20550
		taxOwed += (earnedIncome * 0.12)
		
	else:
		taxOwed = (earnedIncome * 0.1)

#Tax deduction from dependents
taxOwed -= (depDeduct * 4450)

print(f"This year you owe ${round(taxOwed, 2)} in taxes.")
