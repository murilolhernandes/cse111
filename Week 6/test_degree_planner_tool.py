from degree_planner_tool import dictionaryBuilder, creditsToGraduate, creditsCompleted
import pytest

def test_dictionaryBuilder():
  """Verify that the dictionaryBuilder function works correctly.
  Parameters: the filename of the csv file
  Return: nothing
  """
  csv_file = "test_courses.csv"
  with open(csv_file, "w") as f:
    f.write("Hernandes,Murilo Luiz,2024\n")
    f.write("Course Number,Course Name,Credits,Completion\n")
    f.write("CSE101,Introduction to CSE,3,In Progress\n")
    f.write("CSE202,Data Structures,4,Completed\n")

  course_dict = dictionaryBuilder(csv_file)

  expected_dict = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "Completed"]
  }
  assert course_dict == expected_dict

  # def test_dictionaryBuilder_empty_file():
  csv_file = "empty_courses.csv"
  with open(csv_file, "w") as f:
    f.write("Hernandes,Murilo Luiz,2024\n")
    f.write("Course Number,Course Name,Credits,Completion\n")
    pass

  course_dict = dictionaryBuilder(csv_file)

  expected_dict = {}
  assert course_dict == expected_dict
  # def test_dictionaryBuilder_invalid_file():
  csv_file = "non_existing_courses.csv"
  with pytest.raises(FileNotFoundError):
    dictionaryBuilder(csv_file)

def test_creditsToGraduate(capsys):
  dictionary = {}
  creditsToGraduate(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou need 0 credits to graduate.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "Completed"],
    "REL200C": ["The Eternal Family", "2", "Incomplete"],
    "REL225A": ["Foundations of Restoration", "1", "In Progress"]
  }

  creditsToGraduate(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou need 6 credits to graduate.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "Completed"],
    "REL200C": ["The Eternal Family", "2", "Completed"],
    "REL225A": ["Foundations of Restoration", "1", "Completed"]
  }

  creditsToGraduate(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou need 3 credits to graduate.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "In Progress"],
    "REL200C": ["The Eternal Family", "2", "Incomplete"],
    "REL225A": ["Foundations of Restoration", "1", "Incomplete"]
  }

  creditsToGraduate(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou need 10 credits to graduate.\n"

def test_creditsCompleted(capsys):
  dictionary = {}
  creditsCompleted(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou have completed 0 credits.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "Completed"],
    "REL200C": ["The Eternal Family", "2", "Completed"],
    "REL225A": ["Foundations of Restoration", "1", "Completed"]
  }

  creditsCompleted(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou have completed 7 credits.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "Completed"],
    "CSE202": ["Data Structures", "4", "Completed"],
    "REL200C": ["The Eternal Family", "2", "Completed"],
    "REL225A": ["Foundations of Restoration", "1", "Completed"]
  }

  creditsCompleted(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou have completed 10 credits.\n"

  dictionary = {
    "CSE101": ["Introduction to CSE", "3", "In Progress"],
    "CSE202": ["Data Structures", "4", "Incomplete"],
    "REL200C": ["The Eternal Family", "2", "Incomplete"],
    "REL225A": ["Foundations of Restoration", "1", "In Progress"]
  }

  creditsCompleted(dictionary)
  captured = capsys.readouterr()
  assert captured.out == "\nYou have completed 0 credits.\n"

pytest.main(["-v", "--tb=line", "-rN", __file__])
