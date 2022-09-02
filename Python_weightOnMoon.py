"""
Owen's "Weight on moon calculator"

"""

#ImperialVariables
earthWeight = float(input("Enter weight in pounds: "))
moonWeight = (((earthWeight)/9.81)*1.622)
moonWeightLbs = int(moonWeight // 1)
moonWeightOz = int(((moonWeight % 1) * 16) + 0.5)

#MetricVariables
moonWeightKg = int((moonWeight * 0.45359237) // 1)
moonWeightG = int(((((moonWeight * 0.45359237) % 1)) * 1000) + 0.5)

#Dr. Priem's dumb universe
pythoidWeight = (4 * ((((((earthWeight) ** 2) - 13) / 8) + 22) ** 0.5))
pythoidWeightLbs = int(pythoidWeight // 1)
pythoidWeightOz = int(((pythoidWeight % 1) * 16) + 0.5)

print(earthWeight, "lbs on Earth is equal to", moonWeightLbs, "lbs", moonWeightOz, "oz on the Moon.")
print(earthWeight, "lbs on Earth is equal to", moonWeightKg, "kg", moonWeightG, "g on the Moon")
print(earthWeight, "lbs on Earth is equal to", pythoidWeightLbs, "lbs", pythoidWeightOz, "oz on Pythoid.")
