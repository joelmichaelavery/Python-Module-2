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
cable_in_feet = int(input("Please enter how many feet of cable you want to install: "))

#if statement to determine price per foot if more than 100 ft byt less than 250
if cable_in_feet > 101 and cable_in_feet < 251:
    price_per_foot = 0.80

#elif statement to determine price per foot at 0.70 per ft if 250 - 500 ft
elif cable_in_feet > 250 and cable_in_feet < 501:
    price_per_foot = 0.70

#elif statement to determine price per foot at 0.5 per ft if over 500ft install. 
elif cable_in_feet > 500:
    price_per_foot = 0.50

#else statement to say if none of the above cases are true, then 0.87 per ft. 
else: 
    price_per_foot = 0.87


#declare variable total_cost and set to price_per_foot * cable_in_feet
total_cost = price_per_foot * float(cable_in_feet)
total_cost = "{:.2f}".format(total_cost) #sets the total cost to two decimals

#output company name and total cost
print(f'''Hello, {company_name.title()}, your total cost is ${total_cost} 
for {cable_in_feet} feet of cable, thank you and have a great day!''')

