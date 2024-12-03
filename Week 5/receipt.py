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