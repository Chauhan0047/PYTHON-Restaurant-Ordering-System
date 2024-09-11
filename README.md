PYTHON Restaurant Ordering System

Overview:
This Python script simulates a simple restaurant ordering system. Customers can view the menu, place orders, and receive the total amount for their orders. The script runs in a loop, allowing multiple orders until the user decides to quit.

Features:
View Menu: Displays a list of available items with their prices.
Place Orders: Allows users to order items from the menu.
Total Calculation: Calculates and displays the total cost of all orders.

Requirements:
Python 3.x

Installation :
Clone the repository: https://github.com/Chauhan0047/PYTHON-Restaurant-Ordering-System.git
 
Navigate to the project directory:
Copy code: cd restaurant-ordering-system

Usage
Run the script: python restaurant_ordering_system.py

Follow the on-screen instructions to place your orders:
View Menu: The script automatically displays the menu when started.
Place Orders: Enter the name of the item you want to order. To stop ordering, type No.
Total Calculation: The total cost of your orders will be displayed when you quit.

Example Usage:
Here's how you might interact with the script

Copy code:
Welcome to PYTHON Restaurant
Our Menu: 
pizza : 50
burger : 40
pasta : 45
salad : 35
coffee : 30

Enter the item you want to order (or 'No' to quit): pizza
You ordered pizza for 50.

Enter the item you want to order (or 'No' to quit): burger
You ordered burger for 40.

Enter the item you want to order (or 'No' to quit): coffee
You ordered coffee for 30.

Enter the item you want to order (or 'No' to quit): No
Thank you for ordering at PYTHON Restaurant. Have a GoodDay!

Total orders: 120

\\
Code Details:
menu: A dictionary containing menu items and their prices.
Main Loop: Continuously prompts the user for orders until 'No' is entered.
Order Validation: Checks if the ordered item is on the menu and updates the total cost.
Order Summary: Displays the total cost after the user exits.

Contributing:
Feel free to open issues or submit pull requests if you have any suggestions or improvements.
