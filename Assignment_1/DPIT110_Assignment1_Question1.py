# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 1
# Question number: 1
# -------------------------------------------------------*/
steps = input("Enter the number of steps from the start to the finish: ")
print("Here is your journey:")
print("start", end="")
for i in range(int(steps)):
    print("->", end="")
print("finish")