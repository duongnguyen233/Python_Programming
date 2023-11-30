# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 2
# Question number: 4
# -------------------------------------------------------*/
import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

def addNum(num1, num2) -> int:
    return num1 + num2
def subtractNum(num1, num2) -> int:
    return num1 - num2
def multiplyNum(num1, num2) -> int:
    return num1 * num2
def divideNum(num1, num2) -> float:
    return num1 / num2

print("The first number is {0}".format(number1))
print("The second number is {0}".format(number2))
print("{0} + {1} = {2}".format(number1, number2, addNum(number1, number2)))
print("{0} - {1} = {2}".format(number1, number2, subtractNum(number1, number2)))
print("{0} * {1} = {2}".format(number1, number2, multiplyNum(number1, number2)))
print("{0} / {1} = {2}".format(number1, number2, divideNum(number1, number2)))