# def deposit(amount):
#   # In order for this program to work correctly and
#   # for the bank records to be correct, we must not
#   # allow someone to deposit a zero or negative amount.
#   assert amount > 0
#   ...

# assert temperature < 0
# assert len(given_name) > 0
# assert balance == 0
# assert school_year != "senior"

# def test_min():
#   assert min(7, -3, 0, 2) == -3

# # Example 4
# # The variables e and f can by any floating-
# # point numbers from any calculation.
# e = 7.135
# f = 7.128
# if abs(e-f) < 0.01:
#   print(f"{e} and {f} are close enough so\nwe'll consider them to be equal.")
# else:
#   print(f"{e} and {f} are not close and\ntherefore not equal.")

# def approx(expected_value, rel=None, abs=None, nan_ok=False):

# def test_function():
#   assert actual_value == approx(expected_value)

# # Example 5
# def test_sqrt():
#   assert math.sqrt(5) == approx(2.24, rel=0.01)

# # Example 6
# # Compute the tolerance.
# tolerance = expected_value * rel
# # Use the tolerance to determine if the actual
# # anc expected values are close enough to be
# # considered equal.
# if abs(actual_value - expected_value) < tolerance:
#   return True
# else:
#   return False

# # Example 7
# def test_sqrt():
#   assert math.sqrt(5) == approx(2.24, abs=0.01)

# # weather.py
# def cels_from_fahr(fahr):
#   """Convert a temperature in Farehnheit to
#   Celsius and return the Celsius temporature.
#   """
#   cels = (fahr - 32) * 5 / 9
#   return cels

# # test_weather.py
# from weather import cels_from_fahr
# from pytest import approx
# import pytest
# def test_cels_from_fahr():
#   """Test the cels_from_fahr function by calling it and
#   comparing the values it returns to the expected values.
#   Notice this test function uses pytest.approx to compare
#   floating-point numbers.
#   """
#   assert cels_from_fahr(-25) == approx(-31.66667)
#   assert cels_from_fahr(0) == approx(-17.77778)
#   assert cels_from_fahr(32) == approx(0)
#   assert cels_from_fahr(70) == approx(21.1111)
# # Call the main function that is part of pytest so that the
# # computer will execute the test functions in this file.
# pytest.main(["-v", "--tb=line", "-rN", __file__])

# from file_name import function_1, function_2, ... function_N
# # Start this program by
# # calling the main function.
# main()

# # If this file is executed like this:
# # >python program.py
# # then call the main function. However, if this file is simply
# # imported (e.g. into a test file), then skip the call to main.
# if __name__ == "__main__":
#   main()

# # Example 1
# def main():
#   print("Are you surprised, Clark?)
# # Start this program by
# # calling the main function.
# if__name__ == "__main__":
#   main()

# # Example 2
# def main():
#   print("This program computes and prints the remaining\nbalance for a loan with a fixed annual percentage rate\nand a fixed number of payments per year.")
#   print()
#   print("Please enter the following five values.")
#   principal = float(input("Principal amount: "))
#   annual_rate = float(input("Annual percentage rate: "))
#   years = int(input("Number of years in the life of the loan: "))
#   payments_per_years = int(input("Number of payments per year: "))
#   number_paid = int(input("Number of payments already paid: "))
#   balance = compute_balance(principal, annual_rate, years, payments_per_years, number_paid)
#   print()
#   print(f"Balance remaining: {balance}")

# def compute_balance(princ, ar, years, ppy, ptd):
#   """Compute and return the  balance remaining for a loan."""
#   payment = compute_payment(princ, ar, years, ppy)
#   # Show variable values for debugging
#   print()
#   print(f"compute_balance({princ}, {ar}, {years}, {ppy}, {ptd})")
#   rate = ar / ppy
#   power = (1 + rate) ** ptd
#   # Show variable values for debugging
#   print(f"    payment: {payment}, rate: {rate}, power: {power}")
#   balance = princ * power - payment * (power - 1) / rate
#   # Show variable values for debugging
#   print(f"    balance: {balance:.2f}")
#   return round(balance, 2)

# def compute_payment(princ, ar, years, ppy):
#   """Compute and return the payment per period for a loan."""
#   # Show variable values for debugging
#   print()
#   print(f"compute_payment({princ}, {ar}, {years}, {ppy})")
#   rate = ar / ppy
#   n = years * ppy
#   # Show variable values for debugging
#   print(f"    rate: {rate}, n: {n}")
#   payment = princ * rate / (1 - (1 + rate) ** (-n))
#   # Show variable values for debugging
#   print(f"    payment: {payment:.2f}")
#   return round(payment, 2)

# # Start this program by
# # calling the main function.
# if __name__ == "__main__":
#   main()