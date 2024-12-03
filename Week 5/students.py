import csv

def main():
  try:
    student_dict = read_dictionary("students.csv", 0)
    studentID = input("Please enter an I-Number (xxxxxxxxx): ").replace("-", "")
    student_name = student_dict[studentID][1]
    print(f"Name: {student_name}")
  except FileNotFoundError as not_found_err:
    print(f"{not_found_err}")
  except PermissionError as perm_err:
    print(f"{perm_err}")
  except KeyError:
    print("No such student.")
  except:
    print("An error has occurred.")

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
  with open(filename, "rt") as students_file:
    reader = csv.reader(students_file)
    next(reader)
    for row_list in reader:
      key = row_list[key_column_index]
      dictionary[key] = row_list
  return dictionary

if __name__ == "__main__":
  main()