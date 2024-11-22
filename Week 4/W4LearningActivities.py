# Collections:

# # Lists are collections of items
# names = ['Christopher', 'Susan']
# scores = []
# scores.append(98) # Add new item to the end
# scores.append(99)
# print(names)
# print(scores)
# print(scores[1]) # Collections are zero-indexed

# # Arrays are also collections of items
# from array import array
# scores = array('d')
# scores.append(97)
# scores.append(98)
# print(scores)
# print(scores[1])

# What is the difference?
# Arrays - Numerical data types; must all be the same type
# Lists - Store anything; store any type

# # Common operations
# names = ['Susan', 'Christopher']
# print(len(names)) # Get the number of items
# names.insert(0, 'Bill') # Insert before index 0
# print(names)
# names.sort()
# print(names)

# # Retrieving ranges
# names = ['Susan', 'Christopher', 'Bill', 'Justin']
# presenters = names[1:3] # If remove '1' and leave it as '[:3]', it will return from index 0 through 2
# # Start and end index

# print(names)
# print(presenters)

# # Dictionaries
# person = {'first': 'Christopher'}
# person['last'] = 'Harrison'
# print(person)
# print(person['first'])

# What is the difference?
# Dictionaries - Key/Value pairs; Storage order not guaranteed
# Lists - Zero-based index; Stored order guaranteed

# Loops:

# # Loop through a collection
# for name in ['Christopher', 'Susan']:
#   print(name)

# # Looping a number of times
# for index in range(0, 2): # 0 is the starting number, 2 is the number of items we are going to get
#   print(index)

# # Looping with a condition
# names = ['Christopher', 'Susan']
# index = 0
# while index < len(names):
#   print(names[index])
#   # Change the condition!! to avoid a stack overflow
#   index += 1

# Lists and Repetition:

# Lists:
# # Example 1
# def main():
#   # Create a list that contains five strings.
#   colors = ["yellow", "red", "green", "yellow", "blue"]
#   # Call the built-in len function
#   # and print the length of the list.
#   length = len(colors)
#   print(f"Number of elements: {length}")
#   # Print the element that is stored
#   # at index 2 in the colors list.
#   print(colors[2])
#   # Change the element that is stored at
#   # index 3 from "yellow to "purple".
#   colors[3] = "purple"
#   # Print the entire colors list.
#   print(colors)
# # Call main to start this program,
# if __name__ == "__main__":
#   main()

# # Example 2
# def main():
#   # Create an emmpty list that will hold fabric names.
#   fabrics = []
#   # Add three elements at the end of the fabrics list.
#   fabrics.append("velvet")
#   fabrics.append("denim")
#   fabrics.append("gingham")
#   # Insert an element at the beginning of the fabrics list.
#   fabrics.insert(0, "chiffon")
#   print(fabrics)
#   # Determine if gingham is in the fabrics list.
#   if "gingham" in fabrics:
#     print("gingham is in the list.")
#   else:
#     print("gingham is NOT in the list.")
#   # Get the index where velvet is stored in the fabrics list.
#   i = fabrics.index("velvet")
#   # Replace velvet with taffeta.
#   fabrics[i] = "taffeta"
#   # Remove the last element from the fabrics list.
#   fabrics.pop()
#   # Remove denim from the fabrics list.
#   fabrics.remove("denim")
#   # Get the length of the fabrics list and print it.
#   n = len(fabrics)
#   print(f"The fabrics list contains {n} elements.")
#   print(fabrics)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Repetition:

# for loop
# # Example 3
# def main():
#   # Create a list of color names.
#   colors = ["red", "orange", "yellow", "green", "blue"]
#   # Use a for loop to print each element in the list.
#   for color in colors:
#     print(color)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# range function
# # Example 4
# def main():
#   # Count from zero to nine by one.
#   for i in range(10):
#     print(i)
#   print()
#   # Count from five to nine by one.
#   for i in range(5, 10): # '5' is the starting number, '10' - 1 is the number of items we are going to get, so it will go from 5 to 9
#     print(i)
#   print()
#   # Count from zero to eight by two.
#   for i in range(0, 10, 2):
#     print(i)
#   print()
#   # Count from 100 down to 70 by three.
#   for i in range(100, 69, -3): # in this case '69' + 1 to achieve desired number
#     print(i)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # Example 5 | Most programmers prefer to write a loop like the one at lines 6–7 because it is simpler than the one at lines 11–15.
# def main():
#   # Create a list of color names.
#   colors = ["red", "orange", "yellow", "green", "blue"]
#   # Use a for loop to print each element in the list.
#   for color in colors:
#     print(color)
#   print()
#   # Use a different for loop to
#   # print each element in the list.
#   for i in range(len(colors)):
#     # Use the index i to retrieve
#     # an element from the list.
#     color = colors[i]
#     print(color)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# break statement
# # Example 6
# def main():
#   sum = 0
#   # Get ten or fewer numbers from the user and
#   # add them together.
#   for i in range(10):
#     number = float(input("Please enter a number: "))
#     if number == 0:
#       break
#     sum += number
#   # Print the sum of the numbers for the user to see.
#   print(f"Sum: {sum}")
# # Call main to start this program.
# if __name__ == "__main__":  
#   main()

# while loop
# # Example 7
# def main():
#   list1 = ["red", "orange", "yellow", "green", "blue"]
#   list2 = ["red", "orange", "green", "green", "blue"]
#   index = compare_lists(list1, list2)
#   if index == -1:
#     print("The contents of list1 and list2 are equal")
#   else:
#     print(f"list1 and list2 differ at index {index}")
# def compare_lists(list1, list2):
#   """Compare the contents of two lists. If the contents
#   of the two lists are not equal, return the index of
#   the first difference. If the contents of the two lists
#   are equal, return -1.
#   Parameters
#     list1: a list
#     list2: another list
#   Return: an index or -1
#   """
#   # Get the length of the shortest list.
#   length1 = len(list1)
#   length2 = len(list2)
#   limit = min(length1, length2)
#   # Begin at the first index (0) and repeat until the
#   # computer finds two elements that are not equal or
#   # until the computer reaches the end of the shortest
#   # list, whichever comes first.
#   i = 0
#   while i < limit:
#     # Retrieve one element from each list.
#     element1 = list1[i]
#     element2 = list2[i]
#     # If the two elements are not
#     # equal, quit the while loop.
#     if element1 != element2:
#       break
#     # Add one to the index variable.
#     i += 1
#     # If the length of both lists are equal and the
#     # computer verified that all elements are equal,
#     # set i to -1 to indicate that the contents of
#     # the two lists are equal.
#   if length1 == length2 == i:
#     i = -1
#   return i
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Compound Lists:
# # Example 8
# def main():
#   # These are the indexes of each
#   # element in the inner lists.
#   YEAR_PLANTED_INDEX = 0
#   HEIGHT_INDEX = 1
#   GIRTH_INDEX = 2
#   FRUIT_AMOUNT_INDEX = 3
#   # Create a compound list that stores inner lists.
#   apple_tree_data = [
#     # [year_planted, height, girth, fruit_amount]
#     [2012, 2.7, 3.6, 70.5],
#     [2012, 2.4, 3.7, 81.3],
#     [2015, 2.3, 3.6, 62.7],
#     [2016, 2.1, 2.7, 42.1]
#   ]
#   # Retrieve one inner list from the compound list.
#   one_tree = apple_tree_data[2]
#   # Retrieve one value from the inner list.
#   height = one_tree[HEIGHT_INDEX]
#   # Print the tree's height.
#   print(f"height: {height}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # Example 9
# def main():
#   # These are the indexes of each
#   # element in the inner lists.
#   YEAR_PLANTED_INDEX = 0
#   HEIGHT_INDEX = 1
#   GIRTH_INDEX = 2
#   FRUIT_AMOUNT_INDEX = 3
#   # Create a compound list that stores inner lists.
#   apple_tree_data = [
#     # [year_planted, height, girth, fruit_amount]
#     [2012, 2.7, 3.6, 70.5],
#     [2012, 2.4, 3.7, 81.3],
#     [2015, 2.3, 3.6, 62.7],
#     [2016, 2.1, 2.7, 42.1]
#   ]
#   total_fruit_amount = 0
#   # This loop will repeat once for each inner list
#   # in the apple_tree_data compound list.
#   for inner_list in apple_tree_data:
#     # Retrieve the fruit amount from
#     # the current inner list.
#     fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]
#     # print the fruit amount for the current tree.
#     print(fruit_amount)
#     # Add the current fruit amount to the total.
#     total_fruit_amount += fruit_amount
#   # Print the total fruit amount.
#   print(f"Total fruit amount: {total_fruit_amount:.1f}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Values and References:
# # Example 10
# def main():
#   x = 17
#   y = x
#   print(f"Before changing x: x {x} y {y}")
#   x += 1
#   print(f"After changing x: x {x} y {y}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# # Example 11
# def main():
#   lx = [7, -2]
#   ly = lx
#   print(f"Before changing lx: lx {lx} ly {ly}")
#   lx.append(5)
#   print(f"After changing lx: lx {lx} ly {ly}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# From examples 10 and 11, we learn that when a computer executes a Python statement to assign the value of a boolean,
# integer, or float variable to another variable (y = x), the computer copies the value of one variable into the other.
# However, when a computer executes a Python statement to assign the value of a list variable to another variable (ly = lx),
# the computer does not copy the value but instead copies the reference so that both variables refer to the same list in memory.

# Pass by Value and Pass by Reference:
# # Example 12
# def main():
#   print("main()")
#   x = 5
#   lx = [7, -2]
#   print(f"Before calling modify_args(): x {x} lx {lx}")
#   # Pass one integer and one list
#   # to the modify_args function.
#   modify_args(x, lx)
#   print(f"After calling modify_args(): x {x} lx {lx}")
# def modify_args(n, alist):
#   """Demonstrate that the computer passes a value
#   for integers and passes a reference for lists.
#   Parameters
#     n: A number
#     alist: A list
#   Return: nothing
#   """
#   print("   modify_args(n, alist)")
#   print(f"   Before changing n and alist: n {n} alist {alist}")
#   n += 1
#   alist.append(4)
#   print(f"   After changing n and alist: n {n} alist {alist}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# From the output of example 12, we see that modifying an integer parameter changes the integer within the called
# function only. However, modifying a list parameter changes the list within the called function and within the
# calling function. Why? Because when a computer passes a boolean, integer, or float variable to a function, the
# computer copies the value of that variable into the parameter of the called function. Copying the value of an
# argument into a parameter is known as pass by value. However, when a computer passes a list variable to a
# function, the computer copies the reference so that the original variable and the parameter both refer to the same
# list in memory. Copying the reference of an argument into a parameter is known as pass by reference.

# Rationale for Pass by Reference:
# Why are booleans and numbers passed to a function by value and lists are passed to a function by reference? To
# understand the answer to this question, consider the work a computer would have to do if lists were passed by value.

# When a computer passes a number (or boolean) variable to a function, the number is passed by value which
# means the computer copies the value of the number variable into the parameter of the called function. This works
# well for numbers because each number variable occupies a small amount of the computer’s memory. Making a
# copy of a number is fast, and the copy uses a small amount of memory.

# However, a list may contain millions of elements and therefore occupy a large amount of the computer’s memory.
# If lists were passed by value to a function, the computer would have to make a copy of a list each time it is passed
# to a function. If a list is large, copying the list takes a relatively long time and uses a lot of the computer’s memory
# for the copy. Therefore, to make programs fast and use less memory, lists (and other large data types) are passed to
# a function by reference.

# Dictionaries:

# Dictionaries
# # Example 1
# def main():
#   # Create a dictionary with student IDs as
#   # the keys and student names as the values.
#   students_dict = {
#     "42-039-4736": "Clint Huish",
#     "61-315-0160": "Amelia Davis",
#     "10-450-1203": "Ana Soares",
#     "75-421-2310": "Abdul Ali",
#     "07-103-5621": "Amelia Davis"
#   }
#   # Add an item to the dictionary.
#   students_dict["81-298-9238"] = "Sama Patel"
#   # Remove an item from the dictionary.
#   students_dict.pop("61-315-0160")
#   # Get the number of items in the dictionary.
#   length = len(students_dict)
#   print(f"length: {length}")
#   # Print the entire dictionary.
#   print(students_dict)
#   print()
#   # Get a student ID from the user.
#   id = input("Enter a student ID: ")
#   # Check if the student ID is in the dictionary.
#   if id in students_dict:
#     # Find the student ID in the dictionary and
#     # retrieve the corresponding student name.
#     name = students_dict[id]
#     # Print the student's name.
#     print(name)
#   else:
#     print("No such student")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Compound Values
# # Example 2
# def main():
#   # Create a dictionary with student IDs as the keys
#   # and student data stored in a list as the values.
#   students_dict = {
#     # student_ID: [given_name, surname, email_address, credits]
#     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0]
#   }
  # A simple value is a value that doesn’t contain parts, such as an integer. A compound value is a value that has parts,
  # such as a list. In example 1 above, the students dictionary has simple keys and values. Each key is a single string, and
  # each value is a single string. It is possible to store compound values in a dictionary. Example 2 shows a students
  # dictionary where each value is a Python list. Because each list contains multiple parts, we say that the dictionary
  # stores compound values.

# Finding One Item
# # Example 3
# def main():
#   # Create a dictionary with student IDs as the keys
#   # and student data stored in a list as the values.
#   students_dict = {
#     # student_ID: [given_name, surname, email_address, credits]
#     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0]
#   }
#   # Get a student ID from the user.
#   id = input("Enter a student ID: ")
#   # This is a difficult and slow way to find an item in a
#   # dictionary. Don't write code like this to find an item
#   # in a dictionary!
#   # For each item in the dictionay, check if
#   # its key is the same as the variable id.
#   student = None
#   for key, value in students_dict.items(): # Bad example!
#     if key == id:                          # Don't use a loop
#       student = value                      # like this to find an
#       break                                # item in a dictionary.

# Correct way to find an item in a dictionary
# # Example 4
# def main():
#   # Create a dictionary with student IDs as the keys
#   # and student data stored in a list as the values.
#   students_dict = {
#     # student_ID: [given_name, surname, email_address, credits]
#     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0]
#   }
#   # These are the indexes of the elements in the value lists.
#   GIVEN_NAME_INDEX = 0
#   SURNAME_INDEX = 1
#   EMAIL_INDEX = 2
#   CREDITS_INDEX = 3
#   # Get a student ID from the user.
#   id = input("Enter a student ID: ")
#   # Check if the student ID is in the dictionary.
#   if id in students_dict:
#     # Find the student ID in the dictionary and
#     # retrieve the corresponding value, which is a list.
#     value = students_dict[id]
#     # Retrieve the student's given name (first name) and
#     # surname (last name or family name) from the list.
#     given_name = value[GIVEN_NAME_INDEX]
#     surname = value[SURNAME_INDEX]
#     # Print the student's name.
#     print(f"{given_name} {surname}")
#   else:
#     print("No such student")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Processing All Items
# # Example 5
# def main():
#   # Create a dictionary with student IDs as the keys
#   # and student data stored in a list as the values.
#   students_dict = {
#     # student_ID: [given_name, surname, email_address, credits]
#     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
#     "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
#   }
#   # These are the indexes of the elements in the value lists.
#   GIVEN_NAME_INDEX = 0
#   SURNAME_INDEX = 1
#   EMAIL_INDEX = 2
#   CREDITS_INDEX = 3
#   total = 0
#   # For each item in the list add the number
#   # of credits that the students has earned.
#   for item in students_dict.items():
#     key = item[0]
#     value = item[1]
#     # Retrieve the number of credits from the value list.
#     credits = value[CREDITS_INDEX]
#     # Add the number of credits to the total.
#     total += credits
#   print(f"Total credits earned by all students: {total}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Unpacking - combining lines 527-529 into one line only (see line 561)
# # Example 6
# def main():
#   # Create a dictionary with student IDs as the keys
#   # and student data stored in a list as the values.
#   students_dict = {
#     # student_ID: [given_name, surname, email_address, credits]
#     "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#     "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
#     "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
#     "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#     "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
#     "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
#   }
#   # These are the indexes of the elements in the value lists.
#   GIVEN_NAME_INDEX = 0
#   SURNAME_INDEX = 1
#   EMAIL_INDEX = 2
#   CREDITS_INDEX = 3
#   total = 0
#   # For each item in the list add the number
#   # of credits that the students has earned.
#   for key, value in students_dict.items():
#     # Retrieve the number of credits from the value list.
#     credits = value[CREDITS_INDEX]
#     # Add the number of credits to the total.
#     total += credits
#   print(f"Total credits earned by all students: {total}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Dictionaries Are Similar to Lists

# # Different
# # Create a list of cities.
# cities_list = ["Delhi", "Lagos", "Dallas"]
# # Create a dictionary of people.
# people_dict = {
#   "P203": "Ignacio Torres",
#   "P445": "Whitney Nelson",
#   "P128": "Yasmin Li"
# }

# # Different
# # Add two cities to the cities list.
# cities_list.insert(1, "Paris")
# cities_list.append("Tokyo")
# # Add two people to the people dictionary.
# people_dict["P205"] = "Liam Myers"
# people_dict["P317"] = "Davina Patel"
	
# # Similar
# if "Paris" in cities_list:
# print("Paris is in the list of cities.")
# if "P203" in people_dict:
# print("P203 is in the dictionary of people.")


# # Different
# # Find Dallas in the cities list.
# index = cities_list.index("Dallas")
# # Find person P128 in the people dictionary.
# person_name = people_dict["P128"]

# # Similar
# # Retrieve the element stored at
# # index 2 in the cities list.
# city_name = cities_list[2]
# # Find person P128 in the people dictionary
# # and retrieve the corresponding value.
# person_name = people_dict["P128"]

# # Similar
# # Change the city name at index 2 to London.
# cities_list[2] = "London"
# # Change the name of person P205 to Finn Meyers.
# people_dict["P205"] = "Finn Myers"

# # Similar
# # Process all the elements in the cities list.
# for city_name in cities_list:
#     print(city_name)
# # Process all the items in the people dictionary.
# for person_key, person_name in people_dict.items():
#     print(person_name)

# # Same
# # Remove the element at index 3
# # from the cities list.
# cities_list.pop(3)
# # Remove the key "P203" and its
# # value from the people dictionary.
# people_dict.pop("P203")

# # Same
	
# # Call the draw_chart function and pass
# # the citites list to that function.
# draw_chart(cities_list)
# # Call the hire_people function and pass
# # the people dictionary to that function.
# hire_people(people_dict)

# Converting between Lists and Dictionaries
# # Example 7
# def main():
#   # Create a list that contains five student numbers.
#   numbers_list = ["42-039-4736", "61-315-0160", 
#     "10-450-1203", "75-421-2310", "07-103-5621"]
#   # Create a list that contains five student names.
#   name_list = ["Clint Huish", "Amelia Davis", "Ana Soares",  "Abdul Ali", "Amelia Davis"]
#   # Convert the numbers and names lists into a dictionary.
#   student_dict = dict(zip(numbers_list, name_list))
#   # Print the entire student dictionary.
#   print(f"Dictionary: {student_dict}")
#   print()
#   # Convert the student dictionary into
#   # two lists and named keys and values.
#   keys = list(student_dict.keys())
#   values = list(student_dict.values())
#   # Print both lists.
#   print(f"Keys: {keys}")
#   print()
#   print(f"Values: {values}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()