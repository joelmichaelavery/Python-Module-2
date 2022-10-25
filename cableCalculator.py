#Module 2 Assignment
#Joel Avery 10/22/2022
#CSD 205


#This program will welcome the customer, gather the customers name, 
# see how many feet of fiberoptic cable the customer will want installed.
# Then the program will figure out the amount of the total cost at 0.87 dollars
# per foot. It will calculate this amount and output the total to the customer
# showing their name. 

#Outputs welcome message to customer
print('''Welcome and thank you for choosing our program to calculate the cost 
of the installation of fiber optic cable. We will need your company name
and the amount of cable that you will need installed in feet. Have a great 
day!\n''')

#Ask for input on what the company name is 
company_name = input("Please enter your company's name: ")

#Ask for input on how many feet the customer would like and store
cable_in_feet = input("Please enter how many feet of cable you want to install: ")

#declare price_per_foot variable and set to 0.87
price_per_foot = 0.87

#declare variable total_cost and set to price_per_foot * cable_in_feet
total_cost = price_per_foot * float(cable_in_feet)

#output company name and total cost
print(f'''Hello, {company_name.title()}, your total cost is ${total_cost} 
for {cable_in_feet} feet of cable, thank you and have a great day!''')

