# F-Strings
# Mr. Scott
# Nov 8th, 2023
# Using F-strings to generate strings w/ variable substitutions

#current way we've seen
t = 15
units = "Fahrenheit"
print("The temperature is: " + str(t) + " degrees " + units + ".")

#Using F(ormatted)-Strings instead:
print(f"The temperature is: {t} degrees {units}.")

