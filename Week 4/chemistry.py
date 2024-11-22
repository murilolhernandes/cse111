"""
Welcome to Week 04, Project 04: Chemistry: Calculating Molar Mass.
We were asked to make a program that will calculate the molar mass of a substance
from the periodic table. We were asked to make functions that will ask the user for a molecular formula and 
a mass sample in grams, and then calculate, return, and print the following results:
The total molar mass, and the number of moles in the sample.

"""

# ///

# Additions for this assignment: I followed the Exceeding the Requirements steps in the assingment by making two extra functions:
# get_formula_name which will return the name of the compound chosen by the user, if it is a known compound,
# if not it will return "unknown compound". For this function to work I had to add a known_molecules_dict provided by the assignment.
# Then I added an option for the user to continue the program by prompting them if they want to calculate another molar mass, and if they do 
# the program will prompt them for the information. The whole program will continue to loop until the user chooses to quit the program.
# The last thing I added was an introduction of the program to the grader (just above) and then to the user (just bellow)
# explaining what we were asked to do and to the user how to use the program and what the user should expect from the program.

# ///

"""
Hello there, scientist! Welcome to the Mole Mass Calculator!
We made a program that calculate the mole mass of a molecular formula to help you in your lab experiments!
All we need is for you to enter the information required like the chemical formula of the sample, and the mass of the sample.
We will display the compound name, if it is a known one, then the total molar mass and the number of moles in the sample!
By default, the program will prompt you to enter the information only once, but if you want to do more calculations. Feel free to continue
for as long as you want. Although, if you don't want to, just say "n" and the program will end.
Enjoy the program!
"""

from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

known_molecules_dict = {
"Al2O3": "aluminum oxide",
"CH3OH": "methanol",
"C2H6O": "ethanol",
"C2H5OH": "ethanol",
"C3H8O": "isopropyl alcohol",
"C3H8": "propane",
"C4H10": "butane",
"C6H6": "benzene",
"C6H14": "hexane",
"C8H18": "octane",
"CH3(CH2)6CH3": "octane",
"C13H18O2": "ibuprofen",
"C13H16N2O2": "melatonin",
"Fe2O3": "iron oxide",
"FeS2": "iron pyrite",
"H2O": "water"
}

def make_periodic_table():
  periodic_table_dict = {
    # symbol: [name, atomic_mass]
    "Ac":	["Actinium",	227],
    "Ag":	["Silver",	107.8682],
    "Al":	["Aluminum",	26.9815386],
    "Ar":	["Argon",	39.948],
    "As":	["Arsenic",	74.9216],
    "At":	["Astatine",	210],
    "Au":	["Gold",	196.966569],
    "B":	["Boron",	10.811],
    "Ba":	["Barium",	137.327],
    "Be":	["Beryllium",	9.012182],
    "Bi":	["Bismuth",	208.9804],
    "Br":	["Bromine",	79.904],
    "C":	["Carbon",	12.0107],
    "Ca":	["Calcium",	40.078],
    "Cd":	["Cadmium",	112.411],
    "Ce":	["Cerium",	140.116],
    "Cl":	["Chlorine",	35.453],
    "Co":	["Cobalt",	58.933195],
    "Cr":	["Chromium",	51.9961],
    "Cs":	["Cesium",	132.9054519],
    "Cu":	["Copper",	63.546],
    "Dy":	["Dysprosium",	162.5],
    "Er":	["Erbium",	167.259],
    "Eu":	["Europium",	151.964],
    "F":	["Fluorine",	18.9984032],
    "Fe":	["Iron",	55.845],
    "Fr":	["Francium",	223],
    "Ga":	["Gallium",	69.723],
    "Gd":	["Gadolinium",	157.25],
    "Ge":	["Germanium",	72.64],
    "H":	["Hydrogen",	1.00794],
    "He":	["Helium",	4.002602],
    "Hf":	["Hafnium",	178.49],
    "Hg":	["Mercury",	200.59],
    "Ho":	["Holmium",	164.93032],
    "I":	["Iodine",	126.90447],
    "In":	["Indium",	114.818],
    "Ir":	["Iridium",	192.217],
    "K":	["Potassium",	39.0983],
    "Kr":	["Krypton",	83.798],
    "La":	["Lanthanum",	138.90547],
    "Li":	["Lithium",	6.941],
    "Lu":	["Lutetium",	174.9668],
    "Mg":	["Magnesium",	24.305],
    "Mn":	["Manganese",	54.938045],
    "Mo":	["Molybdenum",	95.96],
    "N":	["Nitrogen",	14.0067],
    "Na":	["Sodium",	22.98976928],
    "Nb":	["Niobium",	92.90638],
    "Nd":	["Neodymium",	144.242],
    "Ne":	["Neon",	20.1797],
    "Ni":	["Nickel",	58.6934],
    "Np":	["Neptunium",	237],
    "O":	["Oxygen",	15.9994],
    "Os":	["Osmium",	190.23],
    "P":	["Phosphorus",	30.973762],
    "Pa":	["Protactinium",	231.03588],
    "Pb":	["Lead",	207.2],
    "Pd":	["Palladium",	106.42],
    "Pm":	["Promethium",	145],
    "Po":	["Polonium",	209],
    "Pr":	["Praseodymium",	140.90765],
    "Pt":	["Platinum",	195.084],
    "Pu":	["Plutonium",	244],
    "Ra":	["Radium",	226],
    "Rb":	["Rubidium",	85.4678],
    "Re":	["Rhenium",	186.207],
    "Rh":	["Rhodium",	102.9055],
    "Rn":	["Radon",	222],
    "Ru":	["Ruthenium",	101.07],
    "S":	["Sulfur",	32.065],
    "Sb":	["Antimony",	121.76],
    "Sc":	["Scandium",	44.955912],
    "Se":	["Selenium",	78.96],
    "Si":	["Silicon",	28.0855],
    "Sm":	["Samarium",	150.36],
    "Sn":	["Tin",	118.71],
    "Sr":	["Strontium",	87.62],
    "Ta":	["Tantalum",	180.94788],
    "Tb":	["Terbium",	158.92535],
    "Tc":	["Technetium",	98],
    "Te":	["Tellurium",	127.6],
    "Th":	["Thorium",	232.03806],
    "Ti":	["Titanium",	47.867],
    "Tl":	["Thallium",	204.3833],
    "Tm":	["Thulium",	168.93421],
    "U":	["Uranium",	238.02891],
    "V":	["Vanadium",	50.9415],
    "W":	["Tungsten",	183.84],
    "Xe":	["Xenon",	131.293],
    "Y":	["Yttrium",	88.90585],
    "Yb":	["Ytterbium",	173.054],
    "Zn":	["Zinc",	65.38],
    "Zr":	["Zirconium",	91.224]
  }
  return periodic_table_dict

def get_formula_name(formula, known_molecules_dict):
  """Try to find formula in the known_molecules_dict.
  If formula is in the known_molecules_dict, return
  the name of the chemical formula; otherwise return
  "unknown compound".
  Parameters
    formula is a string that contains a chemical formula
    known_molecules_dict is a dictionary that contains
    known chemical formulas and their names
  Return: the name of a chemical formula
  """
  # # I first tried this and it worked well, however, I had to add the else statement
  # # so I decided to search the internet for another solution
  # if formula in known_molecules_dict:
  #   value = known_molecules_dict[formula]
  # else:
  #   value = "unknown compound"
  # return value
  # # The ".get()" method searches the dictionary and returns a value from the dictionary
  # # all in one line of code.
  return known_molecules_dict.get(formula, "unknown compound")

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
  """Compute and return the total molar mass of all the
  elements listed in symbol_quantity_list.
  Parameters
    symbol_quantity_list is a compound list returned
      from the parse_formula function. Each small
      list in symbol_quantity_list has this form:
      ["symbol", quantity].
    periodic_table_dict is the compound dictionary
      returned from make_periodic_table.
  Return: the total molar mass of all the elements in
    symbol_quantity_list.
  For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
  this function will calculate and return
  atomic_mass("H") * 2 + atomic_mass("O") * 1
  1.00794 * 2 + 15.9994 * 1
  18.01528
  """
  total_molar_mass = 0
  # Do the following for each inner list in the
  # compound symbol_quantity_list:
  for inner_list in symbol_quantity_list:
    # Separate the inner list into symbol and quantity.
    symbol = inner_list[SYMBOL_INDEX]
    quantity = inner_list[QUANTITY_INDEX]
    # Get the atomic mass for the symbol from the dictionary.
    atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
    # Multiply the atomic mass by the quantity.
    molar_mass = atomic_mass * quantity
    # Add the product into the total molar mass.
    total_molar_mass += molar_mass
  # Return the total molar mass.
  return total_molar_mass

def again():
  answer = 0
  while answer == 0:
    question1 = input("Would you like to calculate another molar mass? (y/n) ").lower()
    if question1 == "y":
      main()
      answer = 1
    elif question1 == "n":
      print("Thank you for using the molar mass calculator.")
      answer = 1
    else:
      print("Invalid input. Please type 'y' or 'n'.")
      answer = 0

def main():
  # Get the chemical formula for a molecule from the user.
  formula = input("Enter the molecular formula of the sample: ").upper()
  # Get the mass of a chemical sample in grams from the user.
  mass_sample = float(input("Enter the mass in grams of the sample: "))
  # Call the make_periodic_table function and store the returned list in a variable.
  periodic_table_dict = make_periodic_table()
  # Call the parse_formula function to convert the
  # chemical formula given by the user to a compound
  # list that stores element symbols and quantity
  # of atoms of each element in the molecule.
  symbol_quantity_list = parse_formula(formula, periodic_table_dict)
  # Call the compute_molar_mass function to compute the
  # molar mass of the molecule from the compound list.
  molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
  # Compute the number of moles in the sample.
  number_of_moles = mass_sample / molar_mass
  # Print the name of the compound.
  compound_name = get_formula_name(formula, known_molecules_dict)
  print(f"The compound chosen is: {compound_name}")
  # Print the molar mass.
  print(f"{molar_mass:.5f} grams/mole")
  # Print the number of moles
  print(f"{number_of_moles:.5f} moles")
  again()


# Call the main function.
if __name__ == "__main__":
  main()