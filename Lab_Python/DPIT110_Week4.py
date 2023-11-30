# print("----Exercise 1:----")
# for i in range (2, 9):
#     print(i, end =" ")


# print("----Exercise 2:----")
# for i in range (1, 10):
#     print("6 x {0:<2} = {1:<2}".format(i, i*6))


# print("----Exercise 3:----")
# number = int(input("Enter a number: "))
# for i in range (1, 10):
#     print("{0:<2} x {1:<2} = {2:<2}".format(number, i, i*number))


# print("----Exercise 4:----")
# for i in range (0, 11):
#     print("{0:<2} + {1:<2} = {2}".format(i, (10 - i), 10))


# print("----Exercise 5:----")
# for i in range (0, 11):
#     endChar = ","
#     if i == 10: endChar = "."
#     print("{0}{1} ".format(i, endChar), end = "")


# print("----Exercise 6:----")
# sum = 0
# for i in range (2, 21):
#     sum += i
# print("The sum of 2 to 20 is " + str(sum))


# print("----Exercise 7:----")
# inputStr = input("Enter a sentence: ")
# for i in range (0, len(inputStr)):
#     print(inputStr[i])


# print("----Exercise 8:----")
# userName = input("Enter username: ")
# password = userName
# password = password.replace("i", "1" )
# password = password.replace("r", "7" ) 
# password = password.replace("z", "2" ) 
# print("Password is " + password)


# print("----Exercise 9:----")
# for i in range (0, 10):
#     action = input("Would you like green eggs and ham? (Y/N): ")
#     if action == "Y" or action == "y":
#         break


# print("----Exercise Additional 1:----")
# inputStr = input("Enter a sentence: ")
# arrStr = inputStr.split()
# for i in range(0, len(arrStr)):
#     print(arrStr[i])


# print("----Exercise Additional 2:----")
col = 7; row = 6
for i in range(0, row):
    for j in range (i, col):
        line = "* " * (i + 1)
        line += "# " * (col - i - 1)
    print(line)

    