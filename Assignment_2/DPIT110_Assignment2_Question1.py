# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 2
# Question number: 1
# -------------------------------------------------------*/
number = int(input("Enter an integer: "))
print("Here is your output:")
for i in range(0, number):
    for j in range(number, i, -1):
        print("{0}".format(j), end = "")
    print("")