def main():
  try:
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # Reverse the order of the elements in fruit.
    fruit_list.reverse()
    # Print the reversed fruit list.
    print(f"reversed: {fruit_list}")
    # Append orange to the list.
    fruit_list.append("orange")
    # Print the updated fruit list.
    print(f"append orange: {fruit_list}")
    # Find where "apple" is located and insert
    # "cherry" before "apple" in the list.
    i = fruit_list.index("apple")
    fruit_list.insert(i, "cherry")
    # Print the updated fruit list.
    print(f"insert cherry: {fruit_list}")
    # Remove "banana" from the list.
    fruit_list.remove("banana")
    # Print the updated fruit list.
    print(f"remove banana: {fruit_list}")
    # Remove the last element from the list.
    last = fruit_list.pop()
    # Print the updated fruit list.
    print(f"pop {last}: {fruit_list}")
    # Sort the list.
    fruit_list.sort()
    # Print the sorted fruit list.
    print(f"sorted: {fruit_list}")
    # Clear the list.
    fruit_list.clear()
    # Print the cleared fruit list.
    print(f"cleared: {fruit_list}")

  except IndexError as index_err:
    print(type(index_err).__name__, index_err, sep=": ")

# Call main to start this program.
if __name__ == "__main__":
  main()