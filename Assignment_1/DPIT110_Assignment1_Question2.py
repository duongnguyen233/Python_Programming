# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 1
# Question number: 2
# -------------------------------------------------------*/
applePrice = 1.1; bananaPrice = 0.8; orangePrice = 1.5
numApple = int(input("Enter the number of apples: "))
numBanana = int(input("Enter the number of bananas: "))
numOrange = int(input("Enter the number of oranges: "))
cost = numApple*applePrice + numBanana*bananaPrice + numOrange*orangePrice

print("You have purchased: apples {0}, bananas {1} and oranges {2}.".format(numApple, numBanana, numOrange))
print("The cost is ${0:.2f}.".format(cost))