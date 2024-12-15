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
  # loop(main)

def options(dictionary):
  try:
    menu = int(input("\n1. Search for a course\n2. View your current course load\n3. Add a course\n4. Drop a course\n5. View credits to graduate\n6. View credits accomplished\n7. Quit\n\n"))
    if menu == 1:
      searchCourse(dictionary)
    elif menu == 2:
      viewCourseLoad(currentCourseLoad(dictionary))
      options(dictionary)
    elif menu == 3:
      addCourses(dictionary)
      options(dictionary)
    elif menu == 4:
      dropCourse(dictionary)
      options(dictionary)
    # elif menu == 5:
    #   viewCreditsToGraduate(dictionary)
    # elif menu == 6:
    #   viewCreditsAccomplished(dictionary)
    # elif menu == 7:
    #   quit()
    else:
      print("Please enter a valid option.")
  except ValueError as err:
    print(f"Please enter a valid option. {err}")
  except TypeError as err:
    print(f"Please enter a valid option. {err}")

def searchCourse(dictionary):
  search = input("\nWould you like to search by course number or course name? (number or name, or quit): ").lower()
  if search == "number":
    courseNumber = input("Please enter the course number: ").upper()
    if courseNumber in dictionary:
      print(f"Course name: {dictionary[courseNumber][0]}")
      print(f"Course credits: {dictionary[courseNumber][1]}")
      print(f"Course completion: {dictionary[courseNumber][2]}")
    else:
      print("Sorry, we could not find that course number.")
  elif search == "name":
    courseName = input("Please enter the course name: ").lower()
    found = False
    for key, value in dictionary.items():
      if courseName in value[0].lower():
        print(f"Course number: {key}")
        print(f"Course name: {value[0]}")
        print(f"Course credits: {value[1]}")
        print(f"Course completion: {value[2]}\n")
        found = True
    if not found:
      print("Sorry, we could not find that course name.")  
  elif search == "quit":
    options(dictionary)
  else:
    print("\nPlease enter 'number' , 'name' or 'quit to search for a course, or 'quit' to return to the main menu.")
    searchCourse(dictionary)
  more(dictionary, "\nWould you like to search for another course? (yes/no): ", searchCourse)

def more(dictionary, prompt, function):
  cont = input(prompt).lower()
  if cont == "yes":
    function(dictionary)
  elif cont == "no":
    options(dictionary)
  else:
    print("Please enter 'yes' or 'no'.")
    more(dictionary, prompt, function)


# def filter_dictionary(original_dict, user_input):
#   filtered_dict = {key: value for key, value in original_dict.items() if key == user_input and value[2] == "In Progress"}
#   return filtered_dict

def currentCourseLoad(dictionary):
  in_progress_courses = {key: value for key, value in dictionary.items() if value[2] == "In Progress"}
  return in_progress_courses

def viewCourseLoad(courseLoadDictionary):
  print("\nYour current course load is:\n")
  found = False
  for key, value in courseLoadDictionary.items():
    print(f"Course number: {key}")
    print(f"Course name: {value[0]}")
    print(f"Credits: {value[1]}")
    print(f"Status: {value[2]}\n")
    found = True
  if not found: 
    print("\nYour course load is empty.")
  # user_input = input("Please enter a filter value (or 'quit' to exit): ").lower() /// I could use this as filter to search for anything, like courses with a specific completion status, or even by their credits.
  # while user_input != "quit":
  # # user_input = input("Please enter a course number: ").upper()
  #   filtered_dict = {key: value for key, value in filtered_dict.items() if user_input}
  # if filtered_dict:
  #   print(filtered_dict)
  # else:
  #   print("No course found matching the filter criteria.")

def addCourses(dictionary):
  addCourse = input("\nWhich course would you like to add? Please enter by the course number: ").upper()
  found = False
  for key, value in dictionary.items():
    if addCourse == key:
      if value[2] == "Completed":
        print("You cannot add a completed course to your course load.")  
        found = True      
      elif value[2] == "In Progress":
        print("You already have that course in your course load.")
        found = True
      else:
        dictionary[addCourse][2] = "In Progress"
        more(dictionary, "\nWould you like to add another course? (yes/no): ", addCourses)
        found = True
  if not found:   
    print("Sorry, that course is not in your course load.")

def dropCourse(dictionary):
  removeCourse = input("\nWhich course would you like to drop? Please enter by the course number: ").upper()
  found = False
  for key, value in dictionary.items():
    if removeCourse == key and value[2] == "In Progress":
      updateDictionary = input("\nDid you complete the course or are you dropping it? (completed/drop): ").lower()
      if updateDictionary == "completed":
        dictionary[removeCourse][2] = "Completed"
        found = True
      elif updateDictionary == "drop":
        dictionary[removeCourse][2] = "Incomplete"
        found = True
      more(dictionary, "\nWould you like to drop another course? (yes/no): ", dropCourse)
      # found = True
  if not found:
    print("Sorry, that course is not in your course load.")

# def viewCreditsToGraduate():

# def viewCreditsAccomplished()

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
  except Exception as e:
    print(f"An error has occurred: {e}")
  except:
    print("An error has occurred.")

if __name__ == "__main__":
  main()