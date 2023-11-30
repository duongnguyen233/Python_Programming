import datetime

# print("----Exercise 1:----")
# print("Hello World!")
# print("Welcome to Python!\n")
# print(1000)
# print(2000)
# print(3000)

# print("----Exercise 2:----\n")
# first_name = "John"
# virus_found = False
# print(type(first_name))
# print(type(virus_found))

# print("----Exercise 3:----\n")
# first_name = "John"
# last_name = "Smith"
# full_name = "My name is " + first_name + last_name
# print(full_name)

# print("----Exercise 4:----\n")
# print('Enter string: ')
# str = input()
# print('Multiplication: ')
# mul = input()
# print(str*int(mul))

# print("----Exercise 5:----\n")
# print('Enter your first name: ')
# firstName = input()
# print('Enter your last  name: ')
# lastName = input()
# print("My name is " + firstName + lastName)

# print("----Exercise 6:----\n")
# # A program to display a favorite number
# # favorite number
# fav_number = 7
# # display favorite number
# print("My favorite number is " + str(fav_number))

# print("----Exercise 7:----\n")
# print('Enter the 1st integer: ')
# num1 = input()
# print('Enter the 2nd integer: ')
# num2 = input()
# print(int(num1) + int(num2))

# print("----Exercise 8:----\n")
# print('Enter the 1st number: ')
# num1 = input()
# print('Enter the 2nd number: ')
# num2 = input()
# print(float(num1) + float(num2))

print("----Exercise 9:----\n")
print("Welcome to Unimovies!")
current_time = datetime.datetime.now()
meridiem = current_time.strftime("%p").lower()
print(current_time.strftime('%A %B %d at %I.%M' + meridiem + ': "Inside Out"'))

# print("----Exercise 10:----\n")
# #Program 1:
# print("dog")
# print("cat")
# print("kangaroo")

# #Program 2:
# print("dog", end="*")
# print("cat", end="*")
# print("kangaroo", end="*")

# #Program 3:
# print("dog", end="XYZ")
# print("cat", end="XYZ")
# print("kangaroo", end="XYZ")

# #Program 4:
# print("dog", end="")
# print("cat", end="")
# print("kangaroo", end="")

# #Program 5:
# print("dog", end=", ")
# print("cat", end=", ")
# print("kangaroo", end=".")
# print(2000)

# # Program 6:
# print("dog", end=", ")
# print("cat", end=", ")
# print("kangaroo", end=".")
# print()
# print(2000)
