"""
Welcome to Week 03, Project 03: Testing and Fixing Functions: Water-Pressure Calculator.
We were asked to make a program that will calculate the water pressure at a house.
We were guided to make functions that will calculate the water pressure at a house, with the answers from the user.
Then we were asked to make test functions to test the functions we previously made.
Finally, we display the answer at the end of the program in kPa (kilopascals).
"""

# ///

# Additions for this assignment: I followed the Exceeding the Requirements steps in the assingment by making two extra functions:
# convert_kPa_to_psi (on this document) and test_convert_kPa_to_psi (on the test_water_flow.py document).
# I also turned the valus of the earth's gravity into a constant (EARTH_ACCELERATION_OF_GRAVITY), the water density (WATER_DENSITY), 
# and the water viscosity (WATER_DYNAMIC_VISCOSITY).
# I also added an option for the user to continue the program by prompting the user if they want to run the program again, and if they do 
# the program will start over. The whole program will continue to loop until the user chooses to quit the program.
# The last thing I added was an introduction of the program to the grader (just above) and then to the user (just bellow)
# explaining what we were asked to do and to the user how to use the program and what the user should expect from the program.

# ///

"""
Hello there, engineer! Welcome to the Water-Pressure Calculator!
We made a program that calculate the water pressure at house to make your life easier!
All we need if for you to enter the information required like the height of the tower, the height of the tank,
and the diameter of the pipe. The you just have to sit back and relax, while the program does all the hard work for you!
We will display the water pressure at the house in kPa (kilopascals) and in psi (pounds per square inch). =
By default, the program will prompt you to enter the information only once, but if you want to do more calculations. Feel free to continue
for as long as you want. Although, if you don't want to, just say "no" and the program will end.
Enjoy the program!
"""

def water_column_height(tower_height, tank_height):
  height = tower_height + (3 * tank_height / 4)
  return height

def pressure_gain_from_water_height(height):
  P = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
  return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  P = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2 / (2000 * pipe_diameter)
  return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  P = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
  return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
  R = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY
  return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
  k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
  P = -k * WATER_DENSITY * fluid_velocity**2 / 2000
  return P

def convert_kPa_to_psi(pressure):
  psi = pressure * 0.145038
  return psi

# def question():
#   question1 = input("Would you like to run the program again? (yes/no) ").lower()
#   return question1

def again():
  answer = 0
  while answer == 0:
    question1 = input("Would you like to run the program again? (yes/no) ").lower()

    if question1 == "yes":
      main()
      answer = 1
    elif question1 == "no":
      print("Thank you for using the program.")
      answer = 1
    else:
      print("Invalid input. Please type 'yes' or 'no'.")
      answer = 0
    
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
  tower_height = float(input("Height of water tower (meters): "))
  tank_height = float(input("Height of water tank walls (meters): "))
  length1 = float(input("Length of supply pipe from tank to lot (meters): "))
  quantity_angles = int(input("Number of 90° angles in supply pipe: "))
  length2 = float(input("Length of pipe from supply to house (meters): "))
  water_height = water_column_height(tower_height, tank_height)
  pressure = pressure_gain_from_water_height(water_height)
  diameter = PVC_SCHED80_INNER_DIAMETER
  friction = PVC_SCHED80_FRICTION_FACTOR
  velocity = SUPPLY_VELOCITY
  reynolds = reynolds_number(diameter, velocity)
  loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
  pressure += loss
  loss = pressure_loss_from_fittings(velocity, quantity_angles)
  pressure += loss
  loss = pressure_loss_from_pipe_reduction(diameter,
          velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
  pressure += loss
  diameter = HDPE_SDR11_INNER_DIAMETER
  friction = HDPE_SDR11_FRICTION_FACTOR
  velocity = HOUSEHOLD_VELOCITY
  loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
  pressure += loss
  psi = convert_kPa_to_psi(pressure)
  print(f"Pressure at house: {pressure:.1f} kilopascals, or {psi:.1f} pounds per square inch.")
  again()

if __name__ == "__main__":
  main()