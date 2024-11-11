# import datetime

# # print timestamps to see how long sections of code take to run

# first_name = "Susan"
# print("task completed")
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#   print(x)
# print("task completed")
# print(datetime.datetime.now())
# print()

# from datetime import datetime

# # Function to print current date and time
# def print_time(task_name):
#   print(task_name)
#   print(datetime.now())
#   print()

# # print timestamps to see how long sections of code take to run

# first_name = "Susan"
# print_time('printed first name')

# for x in range(0,10):
#   print(x)
# print_time("completed for loop")

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# first_name_initial = first_name[0:1]

# middle_name = input("Enter your middle name: ")
# middle_name_initial = middle_name[0:1]

# last_name = input("Enter your last name: ")
# last_name_initial = last_name[0:1]

# print(f"Your initials are: {first_name_initial}{middle_name_initial}{last_name_initial}")


# # This funciton will return the first initial of a name
# def get_initial(name):
#   initial = name[0:1].upper()
#   return initial

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# first_name_initial = get_initial(first_name)
# middle_name = input("Enter your middle name: ")
# middle_name_initial = get_initial(middle_name)

# last_name = input("Enter your last name: ")
# last_name_initial = get_initial(last_name)

# print(f"Your initials are: {first_name_initial}{middle_name_initial}{last_name_initial}")


# This funciton will return the first initial of a name
# def get_initial(name):
#   initial = name[0:1].upper()
#   return initial

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# middle_name = input("Enter your middle name: ")
# last_name = input("Enter your last name: ")

# print(f"Your initials are: {get_initial(first_name)}{get_initial(middle_name)}{get_initial(last_name)}")


# # This function will take a name and return the first letter of the name
# def get_initial(name, force_uppercase):
#   if force_uppercase:
#     initial = name[0:1].upper()
#   else:
#     initial = name[0:1]
#   return initial

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# first_name_initial = get_initial(first_name, False)

# print(f"Your initial is: {first_name_initial}")


# # This function will take a name and return the first letter of the name
# def get_initial(name, force_uppercase=True):
#   if force_uppercase:
#     initial = name[0:1].upper()
#   else:
#     initial = name[0:1]
#   return initial

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# first_name_initial = get_initial(first_name)

# print(f"Your initial is: {first_name_initial}")


# # This function will take a name and return the first letter of the name
# def get_initial(name, force_uppercase=True):
#   if force_uppercase:
#     initial = name[0:1].upper()
#   else:
#     initial = name[0:1]
#   return initial

# # Ask for someones name and return the initials
# first_name =  input("Enter your first name: ")
# first_name_initial = get_initial(force_uppercase=False, name=first_name)

# print(f"Your initial is: {first_name_initial}")


# def function_name(param1, param2, ... paramN):
#   """documentation string"""
#   statement1
#   statement2
#   ⋮
#   statementN
#   return value

# variable_name = function_name(arg1, arg2, ... argN)


# # Example 1
# import math
# # Define a function named print_cilinder_volume.
# def print_cilinder_volume():
#   """Compute and print the volume of a cylinder.
#   Parameter: none
#   Return: nothing
#   """
#   # Get the radius and height from the user.
#   radius = float(input("Enter the radius of a cylinder: "))
#   height = float(input("Enter the height of a cylinder: "))
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")

# print_cilinder_volume()


# # Example 2
# import math
# # Define a function named print_cilinder_volume.
# def print_cilinder_volume(radius, height):
#   """Compute and print the volume of a cylinder.
#   Parameters
#   radius: the radius of the cylinder
#   height: the height of the cylinder
#   Return: nothing
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")

# print_cilinder_volume(2.5, 4.1)


# # Example 3
# import math
# # Define a function named print_cilinder_volume.
# def compute_cylinder_volume(radius, height):
#   """Compute and print the volume of a cylinder.
#   Parameters
#   radius: the radius of the cylinder
#   height: the height of the cylinder
#   Return: nothing
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Return the volume of the cylinder so that the
#   # volume can be used somewhere else in the program.
#   return volume

# volume = compute_cylinder_volume(2.5, 4.1)


# # Example 4
# import math
# # Get the radius and height from the user.
# radius = float(input("Enter the radius of a cylinder: "))
# height = float(input("Enter the height of a cylinder: "))
# # Compute the volume of the cylinder.
# volume = math.pi * radius**2 * height
# # Print the volume of the cylinder.
# print(f"Volume: {volume:.2f}")


# # Example 5
# import math
# # Define a function named main.
# def main():
#   # Get the radius and height from the user.
#   radius = float(input("Enter the radius of a cylinder: "))
#   height = float(input("Enter the height of a cylinder: "))
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")
# # Start this program by
# # calling the main function.
# main()


# # Example 6
# import math
# # Define the main function.
# def main():
#   # Get the radius and height from the user.
#   radius = float(input("Enter the radius of a cylinder: "))
#   height = float(input("Enter the height of a cylinder: "))
#   # Call the compute_cylinder_volume function and store
#   # its return value in a variable to use later.
#   volume = compute_cylinder_volume(radius, height)
#   # Print the volume of the cylinder.
#   print(f"Volume: {volume:.2f}")
# # Define the compute_cylinder_volume function.
# def compute_cylinder_volume(radius, height):
#   """Compute the volume of the cylinder.
#   Parameters
#   radius: the radius of the cylinder
#   height: the height of the cylinder
#   Return: the volume of the cylinder
#   """
#   # Compute the volume of the cylinder.
#   volume = math.pi * radius**2 * height
#   # Return the volume of the cylinder so that the
#   # volume can be used somwhere else in the program.
#   # The returned result will be available wherever
#   # this function was called.
#   return volume
# # Start this program by
# # calling the main function.
# main()

# # g is a global variable because it
# # is defined outside of all functions.
# g = 25
# def main():
#   # x is a local variable because
#   # it is defined inside a function.
#   x = 1

# nShapes = 0
# def square_area(length):
#   area = length * length
#   return area
# def rectangle_area(width, length):
#   area = width * length
#   return area

# # Example 3 -- Common Mistake
# import math
# def main():
#   radius = float(input("Enter the radius of a circle: "))
#   area = circle_area()
#   print(f"area: {area:.1f}")
# def circle_area():
#   # Mistake! There is no variable named radius
#   # defined inside this function, so the variable
#   # radius cannot be used in this function.
#   area = math.pi * radius * radius
#   return area

# main()

# # Example 4
# import math
# def main():
#   radius = float(input("Enter the radius of a circle: "))
#   area = circle_area(radius)
#   print(f"area: {area:.1f}")
# def circle_area(radius):
#   area = math.pi * radius * radius
#   return area
# main()

# # Example 5
# import math
# def main():
#   # Call the arc_length function with only one argument
#   # even though the arc_length function has two parameters.
#   len1 = arc_length(4.7)
#   print(f"len1: {len1:.1f}")
#   # Call the arc_length function again but
#   # this time with two arguments.
#   len2 = arc_length(4.7, 270)
#   print(f"len2: {len2:.1f}")
#   # Define a function with two parameter. The
#   # second parameter has a default value of 360.
# def arc_length(radius, degrees=360):
#   """Compute and return the length of an arc of a circle"""
#   circumference = 2 * math.pi * radius
#   length = circumference * degrees / 360
#   return length
# main()