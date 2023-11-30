# print("----Exercise 1:----")
# i = 0
# while i < 10:
#     print(i)
#     i += 1


# print("----Exercise 2:----")
# i = 9
# while i >= 0:
#     print(i)
#     i -= 1


# print("----Exercise 3:----")
# i = 0
# while i < 10:
#     print("{0} x {1} = {2}".format(5, i, 5*i))
#     i += 1


# print("----Exercise 4:----")
# i = 0
# while i <= 10:
#     print("{0} + {1} = {2}".format(i, 10 - i, 10))
#     i += 1


# print("----Exercise 5:----")
# endStr = ","
# i = 0
# while i <= 10:
#     if i%2 == 0:
#         if i == 10: endStr = "."
#         print("{0}{1} ".format(i, endStr), end="")
#     i += 1


# print("----Exercise 6:----")
# startNum = int(input("Enter start number: "))
# endNum = int(input("Enter end number: "))
# print("Equations:")
# i = startNum
# while i <= endNum:
#     print("{0} + {1} = {2}".format(i, i, i+i))
#     i += 1


# print("----Exercise 7:----")
# keepEnter = True
# while keepEnter:
#     strEnter = input("Enter something (or q to quit): ")
#     if strEnter == "q" or strEnter == "quit":
#         keepEnter = False
#         print("Goodbye!")
#     else:
#         print("You have entered: " + strEnter)


# print("----Exercise 8:----")
# enterNum = -1
# while enterNum < 0:
#     enterNum = int(input("Enter a positive integer: "))
# print("You have entered: {0}".format(enterNum))


# print("----Exercise 9:----")
keepEnter = True
while keepEnter:
    optionStr = input("Would you like green eggs and ham? (Y/N): ")
    if optionStr.lower() == "y":
        keepEnter = False
        print("That's a smart choice!")
    elif optionStr.lower() == "n":
        continue
    else:
        print("Invalid input")
