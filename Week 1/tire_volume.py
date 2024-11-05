import math
from datetime import datetime


width = float(input("Enter the width of the tire in mm (ex. 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex. 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex. 15): "))

volume = math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
volume = round(volume, 2)
current_date_and_time = datetime.now().strftime("%Y-%m-%d")
# current_date_and_time = current_date_and_time.strftime("%Y-%m-%d")

# open file called volumes.txt
with open("volumes.txt", "a") as file:
  # write current_date_and_time and volume to volumes.txt
  file.write("Hello, world!" + "\n")
  file.write(str(current_date_and_time) + "\n")
  file.write(str(width) + "\n")
  file.write(str(aspect_ratio) + "\n")
  file.write(str(diameter) + "\n")
  file.write(str(volume))


print(f"The approximate volume is {volume:.2f} liters")