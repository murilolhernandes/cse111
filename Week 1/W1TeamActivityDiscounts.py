from datetime import datetime


is_game = True
while is_game:
  price = float(input("Please enter the price? $"))
  if price != 0:
    quantity = int(input("Please enter the quantity? "))
    subtotal = price
    weekday = datetime.now().weekday()
    # weekday = 1
    if subtotal >= 50 and (weekday == 1 or weekday == 2):
      discount = subtotal * 0.1
      print(f"Discount amount: ${discount:.2f}")
      subtotal -= discount
      tax = subtotal * 0.06
      print(f"Sales tax amount: ${tax:.2f}")
      total = subtotal + tax
      print(f"Total: ${total:.2f}")
    elif subtotal < 50 and (weekday == 1 or weekday == 2):
      tax = subtotal * 0.06
      no_discount = 50 - subtotal
      print(f"You need this much to qualify for a 10% discount: ${no_discount:.2f}")
      print(f"Sales tax amount: ${tax:.2f}")
      total = subtotal + tax
      print(f"Total: ${total:.2f}")
    else:
      tax = subtotal * 0.06
      print(f"Sales tax amount: ${tax:.2f}")
      total = subtotal + tax
      print(f"Total: ${total:.2f}")
  else:
    is_game = False

