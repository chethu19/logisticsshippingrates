#shipping cost calculator

##input [ackage weight and shipping rate
weight=float(input("enter the package weight in the kelograms:"))
rate=float(input("enter teh shipping rate per kilogram:"))

#calculate shipping cost
shipping_cost=weight*rate

#display the result
print(f"shipping cost:{shipping_cost}USD")
