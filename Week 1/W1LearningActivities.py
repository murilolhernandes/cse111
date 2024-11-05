# # Example 1
# # Create variables of different data types and then
# # print the variable names, data types, and values.
# a = "Her name is "  # string
# b = "Isabella"      # string
# c = a + b           # string plus string makes string
# print(f"a: {type(a)} {a}")
# print(f"b: {type(b)} {b}")
# print(f"c: {type(c)} {c}")
# print()
# d = False  # boolean
# e = True   # boolean
# print(f"d: {type(d)} {d}")
# print(f"e: {type(e)} {e}")
# print()
# f = 15     # int
# g = 7.62   # float
# h = f + g  # int plus float makes float
# print(f"f: {type(f)} {f}")
# print(f"g: {type(g)} {g}")
# print(f"h: {type(h)} {h}")
# print()
# i = "True"   # string because of the surrounding quotes
# j = "2.718"  # string because of the surrounding quotes
# print(f"i: {type(i)} {i}")
# print(f"j: {type(j)} {j}")

# # Example 2
# # The input function always returns a string.
# k = input("Please enter a number: ")        # string
# m = input("Please enter another number: ")  # string
# n = k + m          # string plus string makes string
# print(f"k: {type(k)} {k}")
# print(f"m: {type(m)} {m}")
# print(f"n: {type(n)} {n}")
# print()
# # The int and float functions convert a string to a number.
# p = int(input("Please enter a number: "))          # int
# q = float(input("Please enter another number: "))  # float
# r = p + q                     # int plus float makes float
# print(f"p: {type(p)} {p}")
# print(f"q: {type(q)} {q}")
# print(f"r: {type(r)} {r}")

# # Example 3
# # Given the distance that a cable will span and the distance
# # it will sag or dip in the middle, this program computes the
# # length of the cable.
# # Get user input and convert it from
# # strings to floating point numbers.
# span = float(input("Distance the cable must span in meters: "))
# dip = float(input("Distance the cable will sag in meters: "))
# # Use the numbers to compute the cable length.
# length = span + (8 * dip**2) / (3 * span)
# # Print the cable length in the
# # console window for the user to see.
# print(f"Length of cable in meters: {length:.2f}")

# # Example 4
# # Compute the total price of a pizza.
# # The base price of a large pizza is $10.95
# price = 10.95
# # Ask the user for the number of toppings.
# number_of_toppings = int(input("How many toppings? "))
# # Compute the cost of the toppings.
# price_per_topping = 1.45
# toppings_cost = number_of_toppings * price_per_topping
# # Add the cost of the toppings to the price of the pizza.
# price = price + toppings_cost
# # Print the price for the user to see.
# print(f"Price: ${price:.2f}")

# # Example 5
# # Compute the total price of a pizza.
# # The base price of a large pizza is $10.95
# price = 10.95
# # Ask the user for the number of toppings.
# number_of_toppings = int(input("How many toppings? "))
# # Compute the cost of the toppings.
# price_per_topping = 1.45
# toppings_cost = number_of_toppings * price_per_topping
# # Add the cost of the toppings to the price of the pizza.
# price += toppings_cost
# # Print the price for the user to see.
# print(f"Price: ${price:.2f}")

# # Example 6
# # Get an account balance as a number from the user.
# balance = float(input("Enter the account balance: "))
# # If the balance is greater than 500, then
# # compute and add interest to the balance.
# if balance > 500:
#     interest = balance * 0.03
#     balance += interest
# # Print the balance.
# print(f"balance: {balance:.2f}")

# # Example 7
# # Get the cost of an item from the user.
# cost = float(input("Please enter the cost: "))
# # Determine a discount rate based on the cost.
# if cost < 100:
#     rate = 0.10
# elif cost < 250:
#     rate = 0.15
# elif cost < 400:
#     rate = 0.18
# else:
#     rate = 0.20
# # Compute the discount amount
# # and the discounted cost.
# discount = cost * rate
# cost -= discount
# # Print the discounted cost for the user to see.
# print(f"After the discount, you will pay {cost:.2f}")

# # Example 6
# # Get a string of text from the user.
# text1 = input("Enter a motivational quote: ")
# # Call the built-in len function to get
# # the number of characters in the text.
# length = len(text1)
# # Call the string upper method to convert
# # the quote to upper case characters.
# text2 = text1.upper()
# # Call the built-in print function to print
# # the length of the text and the text in all
# # upper case for the user to see.
# print(length, text2)

# # Example 7
# import math
# # Get a number from the user.
# number = float(input("Enter a number: "))
# # Call the math.sqrt function and
# # immediately print its return value.
# print( math.sqrt(number) )
# # Call the math.sqrt function again and
# # use its return value in an if statement.
# if math.sqrt(number) < 100:
#     print(f"The square root is less than 100.")
# elif math.sqrt(number) > 100:
#     print(f"The square root is more than 100.")
# else:
#     print(f"The square root is exactly 100.")

# # Example 8
# import math
# # Get a number from the user.
# number = float(input("Enter a number: "))
# # Call the math.sqrt function and store its
# # return value in a variable to use later.
# root = math.sqrt(number)
# print(f"The square root is {root:.2f}")
# if root < 100:
#     print(f"The square root is less than 100.")
# elif root > 100:
#     print(f"The square root is more than 100.")
# else:
#     print(f"The square root is exactly 100.")

lname = input("What is your last name? ")
fname = input("What is your first name? ")
major = input("What is your major? ")

print(fname, lname, major, sep=" |")