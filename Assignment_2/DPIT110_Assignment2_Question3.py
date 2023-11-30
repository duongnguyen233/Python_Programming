# ------------------------------------------------------
# My name: Tuan Duong Nguyen
# My subject code: DPIT110
# My student number: 8147231
# My email address: tdn763@uowmail.edu.au
# Assignment number: 2
# Question number: 3
# -------------------------------------------------------*/
wordInput = input("Enter a word: ")

print("Your word in uppercase: {0}".format(wordInput.upper()))
print("Your word in lowercase: {0}".format(wordInput.lower()))

wordSeparated = ""
for i in range (len(wordInput)):
    space = " "
    if i == len(wordInput):
        space = "" # last character do not have a space
    wordSeparated += wordInput[i] + space
print("Your word space separated: {0}".format(wordSeparated))
    