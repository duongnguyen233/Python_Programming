# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 1
# Question number: 4
# -------------------------------------------------------*/
adultPrice = 120; teensPrice = 72; childrenPrice = 24.5
firstPerAge = int(input("Enter the 1st person’s age: "))
secondPerAge = int(input("Enter the 2nd person’s age: "))
thirdPerAge = int(input("Enter the 3rd person’s age: "))
firstPerPrice = ""; secondPerPrice = ""; thirdPerPrice = ""
totalPrice = 0
price = 0

if firstPerAge >= 18:
  price = adultPrice
elif firstPerAge <= 12:
  price = childrenPrice
else:
  price = teensPrice
firstPerPrice = "${0:.2f}".format(price)
totalPrice += price

if secondPerAge >= 18:
  price = adultPrice
elif secondPerAge <= 12:
  price = childrenPrice
else:
  price = teensPrice
secondPerPrice = "${0:.2f}".format(price)
totalPrice += price

if thirdPerAge >= 18:
  price = adultPrice
elif thirdPerAge <= 12:
  price = childrenPrice
else:
  price = teensPrice
thirdPerPrice = "${0:.2f}".format(price)
totalPrice += price

print("The cost of your ticket package is:")
print("{0:<10} {1:>10}".format("Age", "Ticket Cost"))
print("{0:<10} {1:>11}".format(firstPerAge, firstPerPrice))
print("{0:<10} {1:>11}".format(secondPerAge, secondPerPrice))
print("{0:<10} {1:>11}".format(thirdPerAge, thirdPerPrice))
print("The total cost is ${0:.2f}".format(totalPrice))