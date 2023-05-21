# Ideally, 'total_items' and 'id' should be saved in a database or a file so that we don't lose our existing data every time
# we exit the app. But for now, we'll just keep them in memory
total_items = []  # stores the list of all the items user's added
id = 0  # each item will have a unique id

# The default sales tax is for Ontario, if you are outside of the province,
# simple change the value to the sales tax of your location  (value is in percentage)
SALES_TAX = 13


# Removes the tax from the final price of a product
def remove_tax(price, tax_included):
    if tax_included:
        return round(price - (price * SALES_TAX / 100), 2)
    return price


# Adds an item to the list
def add_item(name, detailed_name, price, tax_included, place):
    global id

    item = {
        # each product will have a unique id. This will be used for deleting the items
        'id': id,
        # the general name of the product, like bread, banana, toothpaste, pop, dog food...
        'name': name.title().strip(),
        # the detailed name of the product, like Wonder Bread Sliced White Bread, 675g
        'detailed_name': detailed_name.strip(),
        # the price of the product before tax
        'price': remove_tax(price, tax_included),
        # the place the product is being sold in, like Metro, Food Basics, Walmart, Amazon, or even the name of a restaurant
        'place': place
    }

    total_items.append(item)
    id += 1


# Deletes an item from the list based on the id specified
def delete_item(id):
    # item is removed from the list based on its index
    for index, item in enumerate(total_items):
        if item.id == id:
            del total_items[index]
            break


# List all the items with their id for deletion
def list_items_for_deletion():
    for item in total_items:
        print(
            f'{item["id"]}. {item["name"]} - {item["detailed_name"]} - ${item["price"]} - {item["place"]}')


# Prints the items in a formatted way categorized by name
def list_items():
    print("\n---------------------")
    print("List of all products (all prices before tax): \n\n")
    categorized_items = dict()

    # put the items into a dictionary categorized by the name, so the keys of the dict will be the names
    for item in total_items:
        if item["name"] not in categorized_items:
            categorized_items[item["name"]] = []
        categorized_items[item["name"]].append(item)

    # key is the name, and value is a list of items with that name
    for key, value in categorized_items.items():
        print(f"{key}: ")
        for item in value:
            print(
                f'\t {item["place"]} sells "{item["detailed_name"]}" for ${item["price"]}.')
        print("\n")
    print("---------------------\n")


# Will list all the items of one product type only (only based on name)
def list_items_of_product(name):
    print("\n---------------------")
    print(f"List of all {name} products (all prices before tax): \n")

    list_of_items_of_product = [
        item for item in total_items if item["name"] == name]

    for item in list_of_items_of_product:
        print(
            f'{item["place"]} sells "{item["detailed_name"]}" for ${item["price"]}.')

    print("---------------------")


# Adding some pseudo data...
# Please comment or remove these lines out if you want to start fresh
add_item("Bread", "Wonder Bread 600 g", 3.99, False, "Metro")
add_item("Bread", "Enriched Bread 625 g", 6.87, True, "Metro")
add_item("banana", "Premium Banana Product of Ontario 2 lb",
         1.2, False, "Food Basics")
add_item("Banana", "Green Banana 2 lb", 1, False, "Food Basics")
add_item("Dog food", "CESAR Classic Loaf in Sauce Wet Dog Food Beef Selects Variety Pack, 24x100g Trays",
         26.47, False, "Amazon")
add_item("DOG fooD", "Hill's Science Diet Adult Healthy Mobility Large Breed Dry Dog Food, Chicken Meal, Brown Rice & Barley Recipe, 30 lb Bag", 92.14, False, "Amazon")


print("--------------------------------------------")
print("Welcome to Shopping Management!")
print("--------------------------------------------")


# Display the menu of the application
def display_menu():
    print("\nMenu:")
    print("[1] Add an item")
    print("[2] Remove an item")
    print("[3] List all items")
    print("[4] List items of a product")
    print("[5] Exit")
    print("Please specify an option:", end=" ")


display_menu()
option = int(input())

# As long as user doesn't specify the option as five, we'll keep going
while (option != 5):
    # adding an item...
    if (option == 1):
        print("Please specify the general name of the product:", end=" ")
        name = input()

        print("Please specify the detailed name of the product:", end=" ")
        detailed_name = input()

        print("Please specify the price of the product:", end=" ")
        price = float(input())

        print("Is the price before tax (Y)? [Y/N]:", end=" ")
        is_before_tax = input()
        tax_included = False

        if is_before_tax.lower() == "n":
            tax_included = True

        print("Please specify the place that sells this product:", end=" ")
        place = input()

        add_item(name, detailed_name, price, tax_included, place)
        print("--- The product was added successfully! ---")

    # removing an item...
    if (option == 2):
        list_items_for_deletion()
        print("Please specify the id of the product you want to delete:", end=" ")
        id = int(input())
        delete_item(id)
        print(f"--- Product with the id {id} was successfully removed! ---")

    # listing all the items...
    if (option == 3):
        list_items()

    # listing all the items of a particular product...
    if (option == 4):
        print("Please specify the product name:", end=" ")
        name = input()
        list_items_of_product(name.title().strip())

    display_menu()
    option = int(input())
