#Shaan Sullivan
#This program adds up digits and finds the sum.

#asks for input
calc = str(input("Enter a group of numbers with no spaces: "))

#Initialize Variables
index = 0
add = 0
total = 0

#Create a for loop to calculate the sum of the digits
for index in range(len(calc)):
    if calc.isdigit():
        add = calc[index]
        total += int(add)
        index += 1

#print the sum
print("The sum of these digits is", total)
