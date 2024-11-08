# Define the main function.
def main():
  # Get the start odomoter value from the user.
  start = float(input("Enter the start odometer reading (miles): "))
  # Get the end odometer value from the user.
  end = float(input("Enter the end odometer reading (miles): "))
  # Get the fuel consumed value from the user.
  fuel = float(input("Enter the fuel consumed (gallons): "))
  # Call the miles_per_gallon function and store
  # its return value in a variable to use later.
  mpg = miles_per_gallon(start, end, fuel)
  # Call the lp100k_from_mpg function and store
  # its return value in a variable to use later.
  lp100k = lp100k_from_mpg(mpg)
  # Print the efficiency of the car in miles.
  print(f"{mpg:.1f} miles per gallon")
  # Print the efficiency of the car in kilometers.
  print(f"{lp100k:.2f} liters per 100 kilometers")

# Define the miles_per_gallon function.
def miles_per_gallon(start, end, fuel):
  # Compute the miles per gallon.
  mpg = abs(end - start) / fuel
  return mpg

def lp100k_from_mpg(mpg):
  # Compute the kilometers per liter.
  lp100k = 235.215 / mpg
  return lp100k

# Start program.
main()