menu = {
  'pizza': 50,
  'burger': 40,
  'pasta': 45,
  'salad': 35,
  'coffee': 30
}

print("Welcome to PYTHON Restaurant")
print("Our Menu: \npizza : 50\nburger : 40\npasta : 45\nsalad : 35\coffee : 30")

total_orders = 0

while True:
    
  order = input("Enter the item you want to order (or 'No' to quit): ")
  if order.lower() == 'no':
        print("Thank you for ordering at PYTHON Restaurant. Have a GoodDay!")
        break

  if order in menu:
        total_orders += menu[order]
        print(f"You ordered {order} for {menu[order]}.")
  else:
       print(f"Sorry, we don't have {order} in our menu.")
       
print(f"\nTotal orders: {total_orders}")