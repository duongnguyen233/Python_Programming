
# print("----Exercise 1:----")
# # ask user to choose a language
# print("Choose a language: (I)talian (W)elsh (Z)ulu")
# language_option = input("Enter language selection: ")
# # display Hello World, How are you, in different languages
# if (language_option == "I"):
#   print("Ciao mondo.")
# elif (language_option == "W"):
#   print("Helo Byd.")
# elif (language_option == "Z"):
#   print("Sawubona Mhlaba.")
# else:
#   print("Hello World.")


# print("----Exercise 2:----")
# numProducts = int(input("Enter the quantity: "))
# price = 0; postage = 0
# if numProducts <= 50:
#     price = 3
#     postage = 10
# else:
#     price = 2
# totalCost = numProducts*price + postage
# print("Total cost: ${0}".format(totalCost))


# print("----Exercise 3:----")
# numProducts = int(input("Enter the quantity: "))
# shipMethod = input("Shipping method (s/r/e): ")
# price = 0; postage = 0
# if numProducts <= 50:
#     price = 3
#     if shipMethod == "s":
#         postage = 10
#     elif shipMethod == "r":
#         postage = 15
#     else:
#         postage = 120
# else:
#     price = 2
#     if shipMethod == "s":
#         postage = 0
#     elif shipMethod == "r":
#         postage = 15
#     else:
#         postage = 120
# totalCost = numProducts*price + postage
# print("Total cost: ${0}".format(totalCost))


# print("----Exercise 4:----")
# mark = int(input("Please enter mark: "))
# grade = ""
# if mark >= 80:
#     grade = "A"
# elif mark >= 60:
#     grade = "B"
# elif mark >= 40:
#     grade = "C"
# else:
#     grade = "D"
# print("Mark {0}, Grade {1}".format(mark, grade))


# print("----Exercise 5:----")
firstNum = int(input("Enter the 1st integer: "))
secondNum = int(input("Enter the 2nd integer: "))
thirdNum = int(input("Enter the 3rd integer: "))

highest = max(firstNum, secondNum, thirdNum)
print("Max of {0}, {1}, {2} is {3}".format(firstNum, secondNum, thirdNum, highest))