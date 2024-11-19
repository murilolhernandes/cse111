from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
  assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
  assert extract_city("872 Anne Street, Rexburg, ID 83440") == "Rexburg"
  assert extract_city("3324 Brinley Peak Ln, Riverton, UT 84065") == "Riverton"
  assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"

def test_extract_state():
  assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
  assert extract_state("872 Anne Street, Rexburg, ID 83440") == "ID"
  assert extract_state("3324 Brinley Peak Ln, Riverton, UT 84065") == "UT"
  assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"

def test_extract_zipcode():
  assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
  assert extract_zipcode("872 Anne Street, Rexburg, ID 83440") == "83440"
  assert extract_zipcode("3324 Brinley Peak Ln, Riverton, UT 84065") == "84065"
  assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])