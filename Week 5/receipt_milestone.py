import csv
def main():
  PRODUCT_INDEX = 0
  products_dict = read_dictionary("products.csv", PRODUCT_INDEX)
  print(f"All Products\n{products_dict}")
  print(f"Requested Items")

  with open("request.csv", "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row_list in reader:
      key = row_list[0]
      if key in products_dict:
        product_number = row_list[0]
        product_name = products_dict[product_number][1]
        requests = row_list[1]
        product_price = products_dict[product_number][2]
        print(f"{product_name}: {requests} @ {product_price}")

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

if __name__ == "__main__":
  main()