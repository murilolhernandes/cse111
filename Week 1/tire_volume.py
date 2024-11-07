"""
Welcome to Week 01, Project 01: Tire Volume Calculator.
We were asked to make a program that will calculate the user's input and output the result in a file containing the data they provided.
We ask the user to enter the width of the tire in mm, the aspect ratio of the tire, and the diameter of the wheel in inches, 
then we calculate the volume of the tire with the formula: volume = math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000.
We will display it to the user then ask them if they would like to buy tires with the same size.
"""

# ///

# Additions for this assignment: I followed the Exceeding the Requirements steps in the assingment by adding the possibility for the user
# to choose to buy a tire with the size they provided and if they say yes, I added 5 options for the user to choose from.
# I added the option to choose between all season and winter tires. Then I displayed the best tire for the size provided for either all season or winter tires. I also added the question for the user to insert
# phone number and I also appended that to the file called volumes.txt.
# I also added an option to continue the program by prompting the user if they want to enter another tire volume.
# then the whole program will continue to loop until the user chooses to quit the program.
# The last thing I added was an introduction of the program to the grader (just above) and then to the user (just bellow) explaining
# what we were asked to do and to the user how to use the program and what the user should expect from the program.

# ///

"""
Hello there! Welcome to the Tire Volume Calculator!
We will be calculating the volume of a tire then appending the data to a file. This file is currently empty but will be
filled with data you provide and the calculation of the volume.
We will prompt you to enter the width of the tire in mm, the aspect ratio of the tire, and the diameter of the wheel in inches.
We will calculate the volume of the tire with a formula then display it to you.
We will prompt you if you want to buy tires with the same size, if you do, we will prompt you to enter your phone number
then what type of tires you would like to buy! Once you choose, we will display the best tire for the size provided for either
all season or winter tires.
Enjoy the program!
"""

import math
from datetime import datetime

gameOn = True
while gameOn:
  gameOn = True
  if gameOn != False:
    width = int(input("Enter the width of the tire in mm (ex. 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex. 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex. 15): "))
    volume = math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
    volume = round(volume, 2)
    current_date_and_time = datetime.now().strftime("%Y-%m-%d")
    print(f"The approximate volume is {volume:.2f} liters")
    option0 = input("\nWould you like to buy tires with the same size? (y/n): ").lower()
    if option0 == "y":
      phoneNumber = input("\nEnter your phone number: ")
      if width == 215 and aspect_ratio == 55 and diameter == 17:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option1 = "Firestone All Season 215/55R17 Touring"
          tire = option1
        elif typeOfTire == "winter":
          option1 = "Firestone Winterforce 2 215/55R17 Winter"
          tire = option1
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")
      elif width == 245 and aspect_ratio == 45 and diameter == 19:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option2 = "Firestone Firehawk AS V2 245/45R19 Performance"
          tire = option2
        elif typeOfTire == "winter":
          option2 = "Vredestein Wintrac Pro 245/45R19 Performance Winter"
          tire = option2
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")    
      elif width == 235 and aspect_ratio == 60 and diameter == 18:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option3 = "Firestone All Season 235/60R18 Touring"
          tire = option3
        elif typeOfTire == "winter":
          option3 = "Firestone Weathergrip 235/60R18 Touring"
          tire = option3
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")
      elif width == 225 and aspect_ratio == 65 and diameter == 17:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option4 = "Firest All Season 225/65R17 Touring"
          tire = option4
        elif typeOfTire == "winter":
          option4 = "Firestone Weathergrip 225/65R17 Touring"
          tire = option4
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")
      elif width == 205 and aspect_ratio == 60 and diameter == 15:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option5 = "Sentury Tire 205/60R15 Touring All Season"
          tire = option5
        elif typeOfTire == "winter":
          option5 = "Cooper Tires Evolution Winter Studded 205/60R15 Winter"
          tire = option5
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")
      elif width == 185 and aspect_ratio == 50 and diameter == 14:
        typeOfTire = input("Would you like to buy All Season tires or Winter tires? ").lower()
        if typeOfTire == "all season":
          option6 = "We are sorry to inform you that we currently do not any tires for this size at the moment."
          tire = option6
        elif typeOfTire == "winter":
          option6 = "We are sorry to inform you that we currently do not any tires for this size at the moment."
          tire = option6
        else:
          print("\nWe currently we don't have that tire type in stock. We only have All Season and Winter tires at the moment.")
      else:
        option7 = print("\nWe currently we don't have that tire size in stock. Please try another size.")
      print(f"This is the best tire you can buy for the size provided: {tire}")
    # open file called volumes.txt
    with open("volumes.txt", "at") as file:
      # write current_date_and_time and volume to volumes.txt
      file.write(f"{str(current_date_and_time)}, {str(width)}, {str(aspect_ratio)}, {str(diameter)}, {str(volume)}, {phoneNumber}\n")
      # print(f"{str(current_date_and_time)}, {str(width)}, {str(aspect_ratio)}, {str(diameter)}, {str(volume)}\n", file=file)
    again = input("\nWould you like to enter another tire volume? (y/n): ").lower()
    if again == "y":
      gameOn = True
    else:
      print("Goodbye!")
      gameOn = False
  else:
    break