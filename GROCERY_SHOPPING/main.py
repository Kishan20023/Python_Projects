#importing modules

import grocery

#Giving initial instructions.

print("Welcome to our store!\n")

#Giving menu details to the customer

print("Please see our menu to order the items. \n")
print("milk: 25\negg:5\nbutter: 40\ncoffee powder: 60\ntea bags:52\nbread: 30\nfruit jam: 36 \nsugar: 45\nsalt: 20\ncurd: 15\nnoodles packet: 12\nbiscuits: 10\nchocolates: 20\ncheese: 33\nketchup: 28")


# Program for finding the total amount

n=int(input("Enter the number of items:"))
total amount=0

while(n>0):

	item=input("Enter the item wanted : ")
	if grocery.shopping (item)==0: 
		print("Sorry! It is unavailable in our store.")

	else:
		print(item," : ",grocery.shopping (item))
		total_amount+=grocery.shopping (item)

print("The amount to be paid = ", total amount)

# Returning change to the customer

received_amount=int(input("Enter the amount received from the customer : "))
print("The amount to be returned to the customer received_amount-total_amount)

#Thanking the customer

print("Thank you for visiting us!\nPlease come again!")

