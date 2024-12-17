import csv
import sys
import os

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

def options(dictionary):
  try:
    menu = int(input("\n1. Search for a course\n2. View your current course load\n3. Add a course\n4. Drop a course\n5. View credits to graduate\n6. View credits completed\n7. Quit\n\n"))
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
    elif menu == 5:
      creditsToGraduate(dictionary)
      options(dictionary)
    elif menu == 6:
      creditsCompleted(dictionary)
      options(dictionary)
    elif menu == 7:
      print("\nThank you for using the Degree Planner Tool!\nHappy learning!")
      os._exit(0)
    else:
      print("\nPlease enter a valid option.")
      options(dictionary)
  except ValueError as err:
    print(f"\nPlease enter a valid option. {err}")
    options(dictionary)
  except:
    print(f"\nPlease enter a valid option.")
    options(dictionary)

def searchCourse(dictionary):
  search = input("\nWould you like to search by course number or course name? (number or name, or quit): ").lower()
  if search == "number":
    courseNumber = input("Please enter the course number: ").upper()
    if courseNumber in dictionary:
      print(f"\nCourse name: {dictionary[courseNumber][0]}")
      print(f"Course credits: {dictionary[courseNumber][1]}")
      print(f"Course Status: {dictionary[courseNumber][2]}")
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
        print(f"Course Status: {value[2]}\n")
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

def currentCourseLoad(dictionary):
  in_progress_courses = {key: value for key, value in dictionary.items() if value[2] == "In Progress"}
  return in_progress_courses

def viewCourseLoad(courseLoadDictionary):
  credits = 0
  print("\nYour current course load is:\n")
  found = False
  for key, value in courseLoadDictionary.items():
    print(f"Course number: {key}")
    print(f"Course name: {value[0]}")
    print(f"Credits: {value[1]}")
    print(f"Status: {value[2]}\n")
    credits += int(value[1])
    found = True
  if not found: 
    print("\nYour course load is empty.")
  print(f"Total credits this block: {credits}")

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
        print("Course added to your course load.")
        more(dictionary, "\nWould you like to add another course? (yes/no): ", addCourses)
        found = True
  if not found:   
    print("Sorry, that course is not in your catalog.")

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
      print("Course removed to your course load.")
      more(dictionary, "\nWould you like to drop another course? (yes/no): ", dropCourse)
  if not found:
    print("Sorry, that course is not in your course load.")

def creditsToGraduate(dictionary):
  credits = 0
  for key, value in dictionary.items():
    if value[2] != "Completed":
      credits += int(value[1])
  print(f"\nYou need {credits} credits to graduate.")

def creditsCompleted(dictionary):
  credits = 0
  for key, value in dictionary.items():
    if value[2] == "Completed":
      credits += int(value[1])
  print(f"\nYou have completed {credits} credits.")

def loop(function):
  answer == 0
  while answer == 0:
    again = input("\nDo you want to do something else? (y/n) ").lower()
    if again == "y":
      print()
      function()
      answer = 1
    elif again == "n":
      print("Goodbye!")
      answer = 1
    else:
      print("Please enter 'y' or 'n'.")
      answer = 0

def quit():
  print("\nThank you for using the Degree Planner Tool!\nHappy learning!")
  sys.exit()

def main():
  try:
    executeProgram(dictionaryBuilder("degreeAudit.csv"))
  except FileNotFoundError as not_found_err:
    print(f"Error: missing file\n{not_found_err}")
  except PermissionError as perm_err:
    print(f"{perm_err}")
  except SystemExit:
    pass
  except Exception as e:
    print(f"An error has occurred: {e}")
  except:
    print("An error has occurred.")

if __name__ == "__main__":
  main()