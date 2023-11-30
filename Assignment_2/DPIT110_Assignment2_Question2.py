# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 2
# Question number: 2
# -------------------------------------------------------*/
keepEnter = True
totalNum = 0
while keepEnter:
    number = int(input("Enter a number (-1 to quit): "))
    if number == -1:
        print("Your total is {0}.".format(totalNum))
        keepEnter = False
    else:
        totalNum += number