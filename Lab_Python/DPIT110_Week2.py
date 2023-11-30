import datetime

# print("----Exercise 1:----")
# subject_code = "CSCI111"
# subject_mark = 80
# subject_grade = "D"

# result = "Subject result: " 
# + str(subject_code)
# + " mark " + str(subject_mark) 
# + " grade " + subject_grade 

# print(result)


# print("----Exercise 2:----\n")
# print("Welcome to Unimovies!")
# current_time = datetime.datetime.now()
# meridiem = current_time.strftime("%p").lower()
# print(current_time.strftime("%A %B %d at %I.%M" + meridiem + ": \"Inside Out\""))


# print("----Exercise 3:----\n")
# firstName = input("Enter first name: ")
# lastName = input("Enter last name: ")
# age = input("Enter age: ")
# gpaScore = input("Enter GPA score: ")

# print("Name: " + firstName + " " + lastName)
# print(firstName + " " + lastName + " is " + age + " years old")
# print("GPA score {0:.2f}".format(float(gpaScore)))

# print("----Exercise 4:----\n")
# print("Alkali metals:\n\n")
# print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Element", "Symbol", "Atomic number", "Atomic weight"))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Lithium", "Li", 3, 6.94))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Sodium", "Na", 11, 22.99))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Potassium", "K", 19, 39.098))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Rubidium", "Rb", 37, 85.468))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Caesium", "Cs", 55, 132.905))
# print("{0:<15}{1:<10}{2:^25}{3:>15.4f}".format("Francium", "Fr", 87, 223))

# print("----Exercise 5:----\n")
# firstName = input("Enter first name: ")
# lastName = input("Enter last name: ")
# age = input("Enter age: ")
# gpaScore = input("Enter GPA score: ")

# fullName = firstName + " " + lastName
# print("{0:<15} {1:>25}".format("Name:", fullName))
# print("{0:<15} {1:>25}".format("Age:", age))
# print("{0:<15} {1:>25.2f}".format("GPA score:", float(gpaScore)))


# print("----Exercise 6:----\n")
number = int(input("Enter the total of seconds: "))
minutes = number//60
seconds = number%60
print("{0} seconds corresponds to {1} minutes and {2} seconds".format(number, minutes, seconds))