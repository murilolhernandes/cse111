# Text Files
# open(filename, mode="rt")
# mode is an optional string that specifies the mode in which the file will be opened. It defaults to "rt" which
# means open for reading in text mode. Other common values are "wt" for writing a text file (truncating the file
# if it already exists), and "at" for appending to the end of a text file.

# # Example 1
# def main():
#   # Read the contents of a text file
#   # named plants.txt into a list.
#   text_list = read_list("plants.txt")
#   # Print the entire list.
#   print(text_list)
# def read_list(filename):
#   """Read the contents of a text file into a list and
#   return the list. Each element in the list will contain
#   one line of text from the text file.
#   Parameter filename: the name of the text file to read
#   Return: a list of strings
#   """
#   # Create an empty list that will store
#   # the lines of text from the file.
#   text_list = []
#   # Open the text file for reading and store a reference
#   # to the opened file in a variable named text_file.
#   with open(filename, "rt") as text_file:
#     # Read the contents of the text
#     # file one line at a time.
#     for line in text_file:
#       # Remove white space, if there is any,
#       # from the beginning and end of the line.
#       clean_line = line.strip()
#       # Append the clean line of text
#       # onto the end of the list.
#       text_list.append(clean_line)
#   # Return the list that contains the lines of text.
#   return text_list
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # CSV Files
# # Example 2
# import csv
# def main():
#   # Open the CSV file for reading and store a reference
#   # to the opened file in a variable named csv_file.
#   with open("hymns.csv", "rt") as csv_file:
#     # Use the csv module to create a reader object
#     # that will read from the opened CSV file.
#     reader = csv.reader(csv_file)
#     # Read the rows in the CSV file one row at a time.
#     # The reader object return each row as a list.
#     for row_list in reader:
#       print(row_list)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()
# When a csv.reader reads a row from a CSV file, the reader returns the row as a list of strings. The output from
# example 2 shows that a csv.reader returns a list of strings. In the output, notice the five lists of strings, (strings
# surrounded by square brackets [ … ]) that were printed by the print statement at line 17. Notice also that the reader
# reads all the rows from a CSV file, including the first row, which contains column headings.

# # Example 3
# import csv
# # Indexes of some of the columns
# # in the dentists.csv file.
# COMPANY_NAME_INDEX = 0
# NUM_EMPS_INDEX = 3
# NUM_PATIENTS_INDEX = 4
# def main():
#   # Open a file named dentist.csv and store a reference
#   # to the opened file in a variable named dentist_file.
#   with open("dentists.csv", "rt") as dentist_file:
#     # Use the csv module to create a reader
#     # object that will read from the opened file.
#     reader = csv.reader(dentist_file)
#     # The first row of the CSV file contains column
#     # headings and not data about a dental office,
#     # so this statemen skips the first row of the
#     # CSV file.
#     next(reader)
#     running_max = 0
#     most_office = None
#     # Read each row in the CSV file one at a time.
#     # The reader object returns each row as a list.
#     for row_list in reader:
#       # For the current row, retrieve the
#       # values in columns 0, 3, and 4.
#       company = row_list[COMPANY_NAME_INDEX]
#       num_employees = int(row_list[NUM_EMPS_INDEX])
#       num_patients = int(row_list[NUM_PATIENTS_INDEX])
#       # Compute the number of patients per
#       # employee for the current dental office.
#       patients_per_emp = num_patients / num_employees\
#       # If the current dental office has more
#       # patients per employee than the running
#       # maximum, assign running_max and most_office
#       # to be the current dental office.
#       if patients_per_emp > running_max:
#         running_max = patients_per_emp
#         most_office = company
#   # Print the results for the user to see.
#   print(f"{most_office} has {running_max:.1f} patients per employee.")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # Reading a CSV File into a Compound List
# # Example 4
# import csv
# def main():
#   # Read the contents of the dentists.csv file
#   # into a compound list.
#   dentists_list = read_compound_list("dentists.csv")
#   # Print the entire list.
#   print(dentists_list)
# def read_compound_list(filename):
#   """Read the contents of a CSV file into a compound
#   list and return the list. Each element in the
#   compound list will be a small list that contains
#   the values from one row of the CSV file.
#   Parameter filename: the name of the CSV file to read
#   Return: a list of lists that contain strings
#   """
#   # Create an empty list that will
#   # store the data from the CSV file.
#   compound_list = []
#   # Open the CSV file for reading and store a reference
#   # to the opened file in a variable named csv_file.
#   with open(filename, "rt") as csv_file:
#     # Use the csv module to create a reader object
#     # that will read from the opened CSV file.
#     reader = csv.reader(csv_file)
#     # Read the rows in the CSV file one row at a time.
#     # The reader object returns each row as a list.
#     for row_list in reader:
#       # If the current row is not blank,
#       # append it to the compound_list.
#       if len(row_list) != 0:
#         # Append one row from the CSV
#         # file to the compound list.
#         compound_list.append(row_list)
#   # Return the compound list.
#   return compound_list
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # Reading a CSV File into a Compounf Dictionary
# # Example 5
# import csv
# def main():
#   # Index of the phone number column
#   # in the dentists.csv file.
#   PHONE_INDEX = 2
#   # Read the contents of the dentists.csv into a
#   # compound dictionary named dentists_dict. Use
#   # the phone numbers as the keys in the dictionary.
#   dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)
#   # Print the dentists compound dictionary.
#   print(dentists_dict)
# def read_dictionary(filename, key_column_index):
#   """Read the contents of a CSV file into a compound
#   dictionary and return the dictionary.
#   Parameters
#     filename: the name of the CSV file to read.
#     key_column_index: the index of the column
#       to use as the keys in the dictionary.
#   Return: a compound dictionary that contains
#     the contents of the CSV file.
#   """
#   # Create an empty dictionary that will
#   # store the data from the CSV file.
#   dictionary = {}
#   # Open the CSV file for reading and store a reference
#   # to the opened file in a variable named csv_file.
#   with open(filename, "rt") as csv_file:
#     # Use the csv module to create a reader object
#     # that will read from the opened CSV file.
#     reader = csv.reader(csv_file)
#     # The first row of the CSV file contains column
#     # headings and not data, so this statement skips
#     # the first row of the CSV file.
#     next(reader)
#     # Read the rows in the CSV file one row at a time.
#     # The reader object returns each row as a list.
#     for row_list in reader:
#       # If the currrent row is not blank, add the
#       # data from the current to the dictionary.
#       if len(row_list) != 0:
#         # From the current row, retrieve the data
#         # from the column that contains the key.
#         key = row_list[key_column_index]
#         # Store the data from the current
#         # row into the dictionary.
#         dictionary[key] = row_list
#   # Return the dictionary.
#   return dictionary
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Handling Exceptions

# x = 42
# y = 0

# print()
# try:
#   print(x / y)
# except ZeroDivisionError as e:
#   print("Not allowed to divide by zero")
# else:
#   print("Something else went wrong")
# finally:
#   print("This is our cleanup code")
# print()

# # Example 1
# try:
# # Write normal code here. This block must include
# # code that falls into two groups:
# # 1. Code that my cause an exception to be raised
# # 2. Code that depends on the results of the code
# # in the first group
# except ZeroDivisionError as zero_div_err:
# # Code that the computer executes if the code in the try
# # block caused a function to raise a ZeroDivisionError.
# except ValueError as val_err:
# # Code that the computer executes if the code in the try
# # block caused a function to raise a ValueError.
# except (TypeError, KeyError, IndexError) as error:
# # Code that the computer executes if the code in the try
# # block caused a function to raise a TypeError,
# # KeyError, or IndexError.
# except Exception as excep:
# # Code that the computer executes if the code in the try
# # block caused a function to raise any exception that
# # was not handled by one of the previous except blocks.
# except:
# # Code that the computer executes if the code in the try
# # block caused a function to raise anything that
# # was not handled by one of the previous except blocks.
# else:
# # Code that the computer executes after the code in the
# # try block if the code in the try block
# # did not cause any function to raise an exception.
# finally:
# # Code that the computer executes after all the other
# # code in try, except, and else blocks regardless of
# # whether an exception was raised or not.

# As shown in example 1 above, when we want to write code that will handle exceptions, we first write a try block,
# and we put into that try block the normal code that might cause an exception. Then we write except blocks to
# handle the exceptions. Each except block may handle one type of exception like the code at line 227:

# except ZeroDivisionError as zero_div_err:

# Or each except block may handle several types of exceptions, like the code at line 233:

# except (TypeError, KeyError, IndexError) as error:

# Or one except block may handle all possible types of exceptions, like the code at line 237:

# except Exception as excep:

# Or a bare except block may handle anything that can be raised, including SystemExit, KeyboardInterrupt and
# GeneratorExit, like the code at line 241:

# except:

# # TypeError
# # Example 2
# def main():
#   try:
#     text = input("Please enter a number: ")
#     integer = round(text)
#     print(integer)
#   except TypeError as type_err:
#     print(type_err)

# if __name__ == "__main__":
#   main()

# The computer raises a TypeError when the code that calls a function passes an argument with the wrong data
# type. The code in example 2 attempts to pass a string to the round function. This causes the computer to raise a
# TypeError because the round function cannot round a string to an integer. It can round only a number to an
# integer. The output below example 2 shows that the computer raised a TypeError.

# # ValueError
# # Example 3
# def main():
#   try:
#     number = float(input("Please enter a number: "))
#     print(number)
#   except ValueError as val_err:
#     print(val_err)

# if __name__ == "__main__":
#   main()

# The computer raises a ValueError when the code that calls a function passes an argument with the correct data
# type but with an invalid value. A common event that causes the computer to raise a ValueError is when the int
# function or float function tries to convert a string to a number but the string contains characters that are not
# digits. The code in example 3 and its output show a ValueError.

# # ZeroDivisionError
# # Example 4
# def main():
#   try:
#     players = int(input("Enter the number of players: "))
#     teams = int(input("Enter the number of teams: "))
#     players_per_team = players / teams
#     print(f"Each team should have {players_per_team} players")
#   except ZeroDivisionError as zero_div_err:
#     print(zero_div_err)

# if __name__ == "__main__":
#   main()

# The computer raises a ZeroDivisionError when a program attempts to divide a number by zero (0) as shown in
# example 4 and its output.

# # IndexError
# # Example 5
# def main():
#   try:
#     # Create a list that contains three family names.
#     surnames = ["Smith", "Lopez", "Marsh"]
#     # Attempt to change the surname at index 3. Because
#     # there are only three names in the surnames list and
#     # therefore the last index is 2, this statement will
#     # fail and cause the computer to raise an IndexError.
#     surnames[3] = "Olsen"
#   except IndexError as index_err:
#     print(index_err)

# if __name__ == "__main__":
#   main()

# Recall from week 4 that each element in a list is stored at a unique index and that an index is always an integer. If
# we write code that tries to use an index that doesn’t exist in a list, when the computer executes that code, the 
# omputer will raise an IndexError. The program in example 5 creates a list that contains three surnames. Then the
# program attempts to change the surname at index 3. Of course, the list contains only three elements, and the index
# of the last element is 2, so the statement fails and causes the computer to raise an IndexError.

# The program in example 6 is similar to example 5, and both programs cause the computer to raise an IndexError.
# The program in example 6 creates a list that contains three surnames. Then the program attempts to print the
# surname at index 3. Of course, this statement fails because the list contains only three elements, and the index of
# the last element is 2.

# # Example 6
# def main():
#   try:
#     # Create a list that contains three family names.
#     surnames = ["Smith", "Lopez", "Marsh"]
#     # Attempt to change the surname at index 3. Because
#     # there are only three names in the surnames list and
#     # therefore the last index is 2, this statement will
#     # fail and cause the computer to raise an IndexError.
#     print(surnames[3])
#   except IndexError as index_err:
#     print(index_err)

# if __name__ == "__main__":
#   main()

# KeyError
# Example 7
# def main():
#   try:
#     # Create a dictionary with student IDs as
#     # the keys and student names as the values.
#     students = {
#     "42-039-4736": "Clint Huish",
#     "61-315-0160": "Amelia Davis",
#     "10-450-1203": "Ana Soares",
#     "75-421-2310": "Abdul Ali",
#     "07-103-5621": "Amelia Davis"
#     }
#     # Attempt to find the key "50-420-1021",
#     # which is not in the dictionary. This will
#     # cause the computer to raise a KeyError.
#     name = students["50-420-1021"]
#     print(name)
#   except KeyError as key_err:
#     print(type(key_err).__name__, key_err)

# if __name__ == "__main__":
#   main()

# As shown in example 7, if we write code that attempts to find a key in a dictionary and that key doesn’t exist in
# the dictionary, then the computer will raise a KeyError.

# Of course, it is very unlikely that a programmer would write a program that tries to find a hard-coded key that is not
# in a dictionary. However, it is common for a user to enter a key that is not in a dictionary. This is why the programs in
# examples 1 and 4 in the prepare content for lesson 8 include an if statement above the line of code that searches
#   the dictionary, like this:

# # Get a student ID from the user.
# id = input("Enter a student ID: ")
# # Check if the student ID is in the dictionary.
# if id in students:
#   # Find the student ID in the dictionary and
#   # retrieve the corresponding student name.
#   name = students[id]
#   # Print the student's name.
#   print(name)
# else:
#   print("No such student")

# # FileNotFoundError
# # Example 8
# def main():
#   try:
#     with open("products.vcs", "rt") as products_file:
#       for row in products_file:
#         print(row)
#   except FileNotFoundError as not_found_err:
#     print(not_found_err)

# if __name__ == "__main__":
#   main()

# If we write a call to the open function that attempts to open a file for reading and that file doesn’t exist, the
#   computer will raise a FileNotFoundError. Example 8 contains code where such an error might occur.

# # PermissionError
# # Example 9
# def main():
#   try:
#     with open("contacts.csv", "rt") as contacts_file:
#       for row in contacts_file:
#         print(row)
#   except PermissionError as perm_err:
#     print(perm_err)

# if __name__ == "__main__":
#   main()

# # Desired output should be: [Errno 13] Permission denied: 'contacts.csv'

# Nearly all computer operating systems, such as Microsoft Windows, Mac OS X, and Linux, allow multiple people to
# use a single computer. Because people need to store private data in files on a computer, the operating systems
# implement file access permission rules. These rules help to prevent unauthorized access to files.

# If we write a call to the open function that attempts to open a file and the person executing our program doesn’t
# have permission to access the file, the computer will raise a PermissionError. Example 9 contains code where such
# an error might occur.

# # Arithmetic
# # Example 10
# """
# The owner of Sam's Sandwich Shop requested this program,
# which computes the number of sandwiches per employee
# that his employees made in his restaurant in one day.
# """
# def main():
#   try:
#     # Get the number of sandwiches made today and the
#     # number of employees who worked today from the user.
#     sandwiches = int(input("Number of sandwiches made today: "))
#     employees = int(input("Number of employees who worked today: "))
#     # Compute the number of sandwiches per employee
#     # that were made today in the restaurant.
#     sands_per_emp = sandwiches / employees
#     # Print the results for the user to see.
#     print(f"{sands_per_emp:.1f} sandwiches per employee")
#   except ValueError as val_err:
#     print(f"Error: {val_err}")
#     print("You entered text that is not an integer. Please")
#     print("run the program again and enter an integer.")
#   except ZeroDivisionError as zero_div_err:
#     print(f"Error: {zero_div_err}")
#     print("You entered 0 for the number of employees.")
#     print("Please run the program again and enter an integer")
#     print("larger than 0 for the number of employees.")

# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Example 10 contains a complete program with except blocks to handle two types of exceptions: ValueError and
#   ZeroDivisionError.

# # Reading from a File
# # Example 11
# import csv
# DATE_INDEX = 0
# START_MILES_INDEX = 1
# END_MILES_INDEX = 2
# GALLONS_INDEX = 3
# def main():
#   try:
#     # Open the fuel_usage.csv file.
#     filename = "fuel_usage.csv"
#     with open(filename, "rt") as usage_file:
#       # Use the standard csv module to get
#       # a reader object for the CSV file.
#       reader = csv.reader(usage_file)
#       # The first line of the CSV file contains
#       # headings and not fuel usage data, so this
#       # statement skips the first line of the file.
#       next(reader)
#       # Print headers for the three columns.
#       print("Date,Start,End,Gallons,Miles/Gallon")
#       # Process each row in the CSV file.
#       for row_list in reader:
#         # From the current row of the CSV file, get
#         # the date, the starting and ending odometer
#         # readings, and the number of gallons used.
#         date = row_list[DATE_INDEX]
#         start_miles = float(row_list[START_MILES_INDEX])
#         end_miles = float(row_list[END_MILES_INDEX])
#         gallons = float(row_list[GALLONS_INDEX])
#         # Call the miles_per_gallon function.
#         mpg = miles_per_gallon(start_miles, end_miles, gallons)
#         # Display the results for one row.
#         mpg = round(mpg, 1)
#         print(date, start_miles, end_miles, gallons, mpg, sep=",")
#   except FileNotFoundError as not_found_err:
#     print(f"Error: cannot open {filename} because it doesn't exist.")
#   except PermissionError as perm_err:
#     print(f"Error: cannot read from {filename} because you don't have permission.")
#   except ZeroDivisionError as zero_div_err:
#     print(f"Error: {filename} contains a zero in the gallons column.")

# def miles_per_gallon(start_miles, end_miles, gallons):
#   """Compute and return the average number of miles
#   that a vehicle traveled per gallon of fuel.
#   Parameter
#   start_miles: starting odometer reading in miles.
#   end_miles: ending odometer reading in miles.
#   gallons: amount of fuel used in U.S. gallons.
#   Return: miles per gallon
#   """
#   mpg = abs(end_miles - start_miles) / gallons
#   return mpg

# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# The program in example 11 below handles exceptions that might occur when the program opens and reads from a
# file. This program contains only one try block, which begins at line 8 and includes all the regular code in the main
# function. This one try block has three except blocks at lines 522, 524, and 526 that handle FileNotFoundError,
# PermissionError, and ZeroDivisionError.

# # Validating User Input
# # Example 12
# def main():
#   gender = input("Enter your gender (M or F): ")
#   weight = get_float("Enter your weight in kg: ", 20, 500)
#   height = get_float("Enter your height in cm: ", 60, 250)
#   age = get_float("Enter your age in years: ", 10, 120)
#   bmr = basal_metabolic_rate(gender, weight, height, age)
#   print(f"Your basal metabolic rate is {bmr} calories per day.")

# def get_float(prompt, lower_bound, upper_bound):
#   """Get a number from the user, validate that the user
#   entered a number and not some other text, validate that
#   the number is between a lower ans upper bound, and then
#   return the number. If the user enter an invalid number,
#   this function will prompt the user repeatedly until the
#   user enters a valid number.
#   Parameters
#   prompt: A string to display to the user.
#   lower_bound: The smallest number that the user may enter.
#   upper_bound: The largest number that the user may enter.
#   Return: The number entered by the user.
#   """
#   while True:
#     try:
#       text = input(prompt)
#       number = float(text)
#       if number < lower_bound:
#         print(f"{number} is too small.")
#         print("Please enter another number.")
#       elif number > upper_bound:
#         print(f"{number} is too large.")
#         print("Please enter another number.")
#       else:
#         # If the computer gets to this line of code,
#         # the user entered a valid number between
#         # lower_bound and upper_bound, so exit the loop.
#         break
#     except ValueError as val_err:
#       # The user entered at least one character that is
#       # not part of a floating point number, so print a
#       # message asking the user to enter a number.
#       print(f"{text} is not a number.")
#       print("Please enter a number.")
#   return number

# def basal_metabolic_rate(gender, weight, height, age):
#   """Calculate and return a person's basal metabolic rate
#   in calories per day. Weight must be in kilograms, height
#   must be in centimeters, and age must be in years.
#   """
#   if gender.upper() == "F":
#     bmr = 447.593 + 9.247 * weight / + 3.098 * height - 4.330 * age
#   else:
#     bmr = 88.362 + 13.397 * weight / + 4.799 * height - 5.677 * age
#   return bmr

# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# To validate user input means to check user input to ensure it is in the correct format before using that input. The
# program in example 12 validates user input by handling exceptions. Notice in the get_float function, there is a try
# block at line 574. The try block is part of a loop that validates user input in the get_float function. Notice at line 588
# that the except block handles ValueError which is the type of exception that the float function raises when it
# tries to convert text to a number but the text contains characters that are not numeric.