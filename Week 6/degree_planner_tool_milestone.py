import csv

def dictionaryBuilder(file):
  courseDict = {}
  with open(file, "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    next(reader)
    for row in reader:
      courseDict[row[0]] = row[1:]
  return courseDict

def executeProgram(dictionary):
  print("\nWelcome to the Degree Planner Tool!\n")
  print("What would you like to do?")
  print("\nYour options are:")
  options(dictionary)
  loop(main)

def options(dictionary):
  try:
    options = int(input("\n1. Search for a course\n2. View your current course load\n3. Add a course\n4. Drop a course\n5. View credits to graduate\n6. View credits accomplished\n7. Quit\n\n"))
    if options == 1:
      searchCourse(dictionary)
    # elif options == 2:
    #   viewCourseLoad(dictionary)
    # elif options == 3:
    #   addCourse(dictionary)
    # elif options == 4:
    #   dropCourse(dictionary)
    # elif options == 5:
    #   viewCreditsToGraduate(dictionary)
    # elif options == 6:
    #   viewCreditsAccomplished(dictionary)
    # elif options == 7:
    #   quit()
    else:
      print("Please enter a valid option.")
  except ValueError:
    print("Please enter a valid option.")
  except TypeError:
    print("Please enter a valid option.")

def searchCourse(dictionary):
  search = input("\nWould you like to search by course number or course name? (number or name): ").lower()
  if search == "number":
    courseNumber = input("Please enter the course number: ").upper()
    if courseNumber in dictionary:
      print(f"Course name:{dictionary[courseNumber][0]}")
      print(f"Course credits:{dictionary[courseNumber][1]}")
      print(f"Course completion:{dictionary[courseNumber][2]}")
      # loop()
    else:
      print("Sorry, we could not find that course number.")
  elif search == "name":
    courseName = input("Please enter the course name: ").lower()
    if courseName in dictionary.lower():
      print(f"Course number:{dictionary[courseName][0]}")
      print(f"Course credits:{dictionary[courseName][1]}")
      print(f"Course completion:{dictionary[courseName][2]}")
    else:
      print("Sorry, we could not find that course name.")
  else:
    print("\nPlease enter 'number' or 'name' to search for a course.")
    searchCourse(dictionary)
  cont = input("\nWould you like to search for another course? (yes/no): ").lower()
  if cont == "yes":
    searchCourse(dictionary)  # call searchCourse again if user wants to search for another course
  elif cont == "no":
    options(dictionary)
  else:
    print("Please enter 'yes' or 'no'.")
    searchCourse(dictionary)


# def viewCourseLoad():

# def addCourse():

# def dropCourse():

# def viewCreditsToGraduate():

# def viewCreditsAccomplished():

def loop(function):
  answer == 0
  while answer == 0:
    again = input("\nDo you want to do something else? (y/n) ").lower()
    if again == "y":
      # loop main()
      print()
      function()
      answer = 1
    elif again == "n":
      # end program
      print("Goodbye!")
      answer = 1
    else:
      print("Please enter 'y' or 'n'.")
      answer = 0
  # elif answer == 1:
  #   while answer == 1:
  #     print("\nPlease enter a valid option.")
  #     message = input(errorMessage).lower()
  #     if message == "number":
  #       # loop main()
  #       # print()
  #       function()
  #       answer = -1
  #     elif message == "name":
  #       function()
  #       answer = -1
  #     else:
  #       # print(errorMessage)
  #       answer = 1

def main():
  try:
    executeProgram(dictionaryBuilder("degreeAudit.csv"))
    # print(courseDict)
  except FileNotFoundError as not_found_err:
    print(f"Error: missing file\n{not_found_err}")
  except PermissionError as perm_err:
    print(f"{perm_err}")
  except:
    print("An error has occurred.")

if __name__ == "__main__":
  main()