# print("----Exercise 1:----")
# print("Input arguments: 3 input arguments")
# num1 = int(input("number 1: "))
# num2 = int(input("number 2: "))
# num3 = int(input("number 3: "))

# def multiply_3_numbers(num1, num2, num3) -> int:
#     return num1 * num2 * num3

# print("multiply 3 numbers result: {0}".format(multiply_3_numbers(num1, num2, num3)))



# print("----Exercise 2:----")
# grade = int(input("mark: "))
# def calculate_grade(grade) -> str:
#     gradeStr = ""
#     if grade <= 39:
#         gradeStr = "D"
#     elif grade <= 59:
#         gradeStr = "C"
#     elif grade <= 79:
#         gradeStr = "B"
#     else:
#         gradeStr = "A"
#     return gradeStr
# print("Student have mark {0} is rank {1}".format(grade, calculate_grade(grade)))



# print("----Exercise 3:----")
# firstName = input("Input first name: ")
# lastName = input("Input last name: ")

# def say_hi(firstName, lastName):
#     print("Hi {0} {1}".format(firstName, lastName))

# say_hi(firstName, lastName)



# print("----Exercise 4:----")
# strInput = input("word: ")
# multiply = int(input("multiplicity: "))
# def expand(str, multiply):
#     retStr = ""
#     for i in range(len(str)):
#         retStr += str[i] * multiply
#     return retStr
# print(expand(strInput, multiply))



# print("----Exercise 5:----")
# strInput = input("Enter a string: ")
# def transform_character(letter):
#     retStr =""
#     for i in range(len(letter)):
#         if letter[i] == "i":
#             retStr += "I"
#         elif letter[i] == "r":
#             retStr += "R"
#         elif letter[i] == "s":
#             retStr += "S"
#         elif letter[i] == "z":
#             retStr += "Z"
#         else:
#             retStr += letter[i]
#     return retStr
# print("Convert string is: {0}".format(transform_character(strInput)))



# print("----Exercise 6:----")
# userName = input("Enter username : ")
# def generate_password(userName):
#     password =""
#     for i in range(len(userName)):
#         if userName[i].lower() == "i":
#             password += "1"
#         elif userName[i].lower() == "r":
#             password += "7"
#         elif userName[i].lower() == "s":
#             password += "5"
#         elif userName[i].lower() == "z":
#             password += "2"
#         else:
#             password += userName[i]
#     return password
# print("Password is: {0}".format(generate_password(userName)))



# print("----Exercise 7:----")
num = int(input("Input a number: "))
def factorial(number) -> int:
    resultNum = 0
    if number == 1:
        resultNum = 1
        print("1 x ", end="")
    else:
        resultNum = number * factorial(number - 1)
        if number == num:
            print("{0} = ".format(number), end="")
        else:
            print("{0} x ".format(number), end="")
    if number == num:
        print("{0}".format(resultNum))
    return resultNum
print("Result factorial of {0} is {1}".format(num, factorial(num)))