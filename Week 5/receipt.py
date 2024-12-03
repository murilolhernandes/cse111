"""
Welcome to Week 05, Project 05: Grocery Store: Reading CSV files and printing receipts.
We were asked to make a program that will read two csv files and print a receipt
for a grocery store. We were asked to make functions that will compile online requests (contained in the CSV files)
and print a receipt for the user, or rather the employee of the grocery store.
"""

# ///

# Additions for this assignment: I followed the Exceeding the Requirements steps in the assingment by making one extra function
# with two of the suggested requirements: dates() which will print the friendly reminder for the new year's sale and 
# the return by date. Then I added an option for the employee to print an extra receipt for the costumer.  
# The last thing I added was an introduction of the program to the grader (just above) and then to the user (just bellow)
# explaining what we were asked to do and to the user how to use the program and what the user should expect from the program.

# ///

"""
Hello, Inkom Emporium! Welcome to the receipt generator program!
We've created a program that generates receipts for your online grocery store orders!
We will do all the hard work from transferring the items in each order to the receipt so you can focus on the fun part,
getting your constumer's groceries ready.
We will display the items ordered, the subtotal, the sales tax, and the total! We even added a reminder for the new year's sale
and the return by date. Don't worry it's all automated, so it will update itself every time you an order is placed!
By default, the program will prompt you if the costumer wants a copy of the receipt, if they do, simply say "y", otherwise "n".
Enjoy the program!
"""

import csv
from datetime import datetime, timedelta
def main():
  try:
    read_list("request.csv", read_dictionary("products.csv", 0))
    dates()
    if copy():
      read_list("request.csv", read_dictionary("products.csv", 0))
  except FileNotFoundError as not_found_err:
    print(f"Error: missing file\n{not_found_err}")
  except PermissionError as perm_err:
    print(f"{perm_err}")
  except:
    print("An error has occurred.")

def read_list(filename, dictionary):
  items = 0
  subtotal = 0
  print("\nInkom Emporium\n")
  print("Ordered Items:")
  with open(filename, "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row_list in reader:
      try:
        key = row_list[0]
        items += int(row_list[1])
        product_number = row_list[0]
        product_name = dictionary[product_number][1]
        product_price = dictionary[product_number][2]
        requests = row_list[1]
        subtotal += float(requests) * float(product_price)
        taxes = 0.06 * subtotal
        total = subtotal + taxes
        print(f"{product_name}: {requests} @ {product_price}")
      except KeyError:
        items -= int(row_list[1])
        print(f"Error: unknown product ID ({key}) in the {filename} file.")
    print(f"\nNumber of Items: {items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {taxes:.2f}")
    print(f"Total: {total:.2f}")
  print("\nThank you for shopping at Inkom Emporium.")
  current_date = datetime.now()
  print(f"{current_date:%c}\n")

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
      to use as the keys in the dictionary.
  Return: a compound dictionary that contains
    the contents of the CSV file.
  """
  dictionary = {}
  with open(filename, "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row_list in reader:
      if len(row_list) != 0:
        key = row_list[key_column_index]
        dictionary[key] = row_list
  return dictionary

def dates(today=datetime.today().date()):
  new_year = datetime(today.year + 1, 1, 1).date()
  days_before_sale = (new_year - today).days
  print(f"Friendly reminder:\nNew Year's Sale is starting in {days_before_sale} days.")
  return_by_date = datetime.combine(today, datetime.min.time()) + timedelta(days=30)
  return_by_date = return_by_date.replace(hour=21, minute=0, second=0)
  print(f"Return by: {return_by_date.strftime('%m/%d/%Y %I:%M %p')}")

def copy():
  while True:
    copy = input("Does the costumer want a copy of the receipt? (y/n) ").lower()
    if copy == "y":
      return True
    elif copy == "n":
      return False
    else:
      print("Please enter y or n.")

if __name__ == "__main__":
  main()