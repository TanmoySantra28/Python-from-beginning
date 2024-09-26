#After spending if remaining money is more than 500, then you can buy the product. Otherwise not.
budget = 1600
price = int(input("Enter the price of the product = "))
if (budget-price) > 500:
    print("You can buy it")
else:
    print("Too costly, don't buy it")