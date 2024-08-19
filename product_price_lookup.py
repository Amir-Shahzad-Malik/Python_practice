# Dictionary to store product names and their prices
product_prices = {
    'Marzipan': '200 GM Rs. 590.00',
    'Honey Nougat': '385 GM Rs. 1125.00',
    'Cake Rusk': '500 GM Rs. 505.00',
    'Mini Cup': 'Each Rs. 490.00',
    'Chicken Patties': 'Each Rs. 180.00',
    'Vegetable Patties': 'Each Rs. 170.00',
    'Vegetable Cheese Pasty': 'Each Rs. 260.00',
    'Cheese and Onion Pasty': 'Each Rs. 260.00',
    'All Sorts Puff': 'KG Rs. 2090.00',
    'French Heart Puff': 'KG Rs. 2090.00',
    'Roasted Almond Dry Cake': '1/2 KG Rs. 1390.00',
    'Almond Macaroon Dry Cake': '1/2 KG Rs. 1390.00',
    'Pecan Caramel Dry Cake': '1/2 KG Rs. 1420.00',
    'Plain Cake Small': '250 Grams Rs. 505.00',
    'Old English Dry Cake': '1/2 KG Rs. 970.00',
    'Country Side Dry Cake': '1/2 KG Rs. 1345.00',
    'Chocolate Hard Icing Butter Cream Cake': '1/2 KG Rs. 1295.00',
    'Vanilla Hard Icing Butter Cream Cake': '1/2 KG Rs. 1295.00',
    'Strawberry Hard Icing Butter Cream Cake': '1/2 KG Rs. 1295.00',
    'Lemon Tart Butter Cream Cake': '1/2 KG Rs. 1295.00',
    'Pineapple Fresh Cream Cake': '1/2 KG Rs. 1180.00',
    'Black Forest Fresh Cream Cake': '1/2 KG Rs. 1180.00',
    'Pineapple Cherry Fresh Cream Cake': '1/2 KG Rs. 1235.00',
    'Chocolate Chip Fresh Cream Cake': '1/2 KG Rs. 1235.00',
    'Coffee Chocolate Fresh Cream Cake': '1/2 KG Rs. 1200.00',
    'Black Cherry Fresh Cream Cake': '1 KG Rs. 2030.00',
    'Ferrero Rocher Fresh Cream Cake': '1/2 KG Rs. 950.00',
    'Butter Bread Large': 'Each Rs. 260.00',
    'Milk Bread Small': 'Each Rs. 130.00',
    'Plain Bread Large': 'Each Rs. 240.00',
    'Plain Bread Small': 'Each Rs. 125.00',
    'Sweet Rusk Round': 'KG Rs. 1080.00',
    'Sweet Rusk Flat': 'KG Rs. 1080.00',
    'Fruit Bun': 'Each Rs. 90.00',
    'Butter Bun': 'Each Rs. 90.00',
    'Plain Bun Bread': 'Each Rs. 140.00',
    'Chicken Roll': 'Each Rs. 245.00',
    'Vegetable Roll': 'Each Rs. 195.00',
    'Shashlik Stick': 'Each Rs. 335.00',
    'Drum Stick': 'Each Rs. 185.00'
}

def get_price(product_name):
    """Function to get the price of a product"""
    return product_prices.get(product_name, "Product not found")

# Main program loop
while True:
    # Input from user
    product_name = input("Enter the product name (or type 'exit' to quit): ").strip()
    if product_name.lower() == 'exit':
        break
    # Get and display the price
    price = get_price(product_name)
    print(f"Price of '{product_name}': {price}")
