# Using Objects

# Programming Paradigms

# Procedural Programming
# # Example 1
# def main():
#   numbers = [87, 95, 72, 92, 95, 88, 84]
#   total = 0
#   for x in numbers:
#     total += x
#     average = total / len(numbers)
#   print(f"average: {average:.2f}")
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Declarative Programming
# # Example 2
# # SELECT AVG(numbers) FROM table;
# # AVG(numbers)
# # -------------
# # 87.57142857142857

# Functional Programming
# # Example 3
# from functools import reduce
# def main():
#   numbers = [87, 95, 72, 92, 95, 88, 84]
#   func_add = lambda a, b: a + b
#   total = reduce(func_add, numbers)
#   average = total / len(numbers)
#   print(f"average: {average:.2f}")
# # Call main to start the program.
# if __name__ == "__main__":
#   main()
# # Notice how example 3 uses three functions: a lambda function, the reduce function, and the len function. Notice
# # also that the lambda function is passed into the reduce function. Passing a function into a function is one of the
# # marks of functional programming.

# Object-Oriented Programming
# # Example 4
# def main():
#   numbers = [87, 95, 72, 92, 95, 88, 84]
#   numbers.append(78)
#   numbers.append(72)
#   print(numbers)
# # Call main to start the program.
# if __name__ == "__main__":
#   main()
# # There are several types of commands that are commonly found in object-oriented programs. These types of
# # commands are so common, that a programmer must be able to recognize and write them. Three of these types of
# # commands are:
# from datetime import datetime
# # 1. Creating objects, for example:
# obj = datetime.now()
# # 2. Accessing the attributes of an object using the dot operator (.), for example:
# year = obj.year
# # 3. Calling the methods of an object using the dot operator (.), for example:
# new_obj = obj.replace(year=2035)
# day_of_week = obj.weekday()
# print(new_obj, day_of_week)

# Python Lists Are Objects

# # Example 5
# def main():
#   # Create an empty list that will hold fabric names.
#   fabrics = []
#   # Add three elements at the end of the fabrics list.
#   fabrics.append("velvet")
#   fabrics.append("denim")
#   fabrics.append("gingham")
#   # Insert an element at the beginning of the fabrics list.
#   fabrics.insert(0, "chiffon")
#   print(fabrics)
#   # Get the index where velvet is stored in the fabrics list.
#   i = fabrics.index("velvet")
#   # Replace velvet with taffeta.
#   fabrics[i] = "taffeta"
#   print(fabrics)
#   # Remove the last element from the fabrics list.
#   fabrics.pop()
#   # Remove denim from the fabrics list.
#   fabrics.remove("denim")
#   print(fabrics)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

# Python Dictionaries Are Objects

# # Example 6
# def main():
#   # Create a dictionary with student IDs as
#   # the keys and student names as the values.
#   students = {
#     "42-039-4736": "Clint Huish",
#     "61-315-0160": "Amelia Davis",
#     "10-450-1203": "Ana Soares",
#     "75-421-2310": "Abdul Ali",
#     "07-103-5621": "Amelia Davis",
#     "81-298-9238": "Sama Patel"
#   }
#   # Get a student Id from the user.
#   id = input("Enter a student ID: ")
#   # Lookup the student ID in the dictionary and
#   # retrieve the corresponding student name.
#   name = students.get(id)
#   if name:
#     # Print the student name.
#     print(name)
#     # Remove the student that the user
#     # specified from the dictionary.
#     students.pop(id)
#   else:
#     print("No such student")
#   print()
#   # Use a for loop to print each key value pair
#   # in the dictionary. Of courese, the code in
#   # the body of a loop can do much more with
#   # each key value pair than simply print it.
#   for key, value in students.items():
#     print(key, value)
# # Call main to start this program.
# if __name__ == "__main__":
#   main()

