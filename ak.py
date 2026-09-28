special_block = {
    "AB Dakshin": {"Thali": 90, "Paratha": 40, "Tea": 15},
    "Bistro": {"Burger": 80, "Pizza": 120, "Cold Coffee": 60},
    "Mayuri": {"Sandwich": 50, "Maggi": 40, "Juice": 30},
    "Gym": {"Protein Shake": 100, "Water Bottle": 20},
    "Dentist": {"Checkup": 200, "Cleaning": 500},
}
special_info = {
    "AB Darshan": "Price and menu",
    "Bistro": "Price, menu and booking", 
    "Mayuri": "Price and menu",
    "Gym": "Menu only",
    "Dentist": "Check timings at the counter",
}
boys_hostel = {
    "Block 1": "Near the main gate",
    "Block 2": "Near the sports courts",
}
courts = ["Basketball", "Volleyball", "Football", "Badminton", "Tennis"]
shops = {
    "Mayuri": ["Block 1", "Block 2"],
    "Safal": ["Block 1", "Block 2"],
}
shop_items = {
    "Notebook": 60,
    "Pen": 10,
    "Water Bottle": 20,
    "Biscuits": 10,
    "Chips": 20,
    "Cold Drink": 40,
}

ab1_info = {
    "Teachers cabin": "AB Proctor",
    "Cafes": ["Mayuri", "Under Betty"],
}

favourites = []
def title(text):
    print()
    print("-" * 40)
    print("   " + text)
    print("-" * 40)
def ask_number(message):
    # keeps asking until the user types a number
    while True:
        answer = input(message)
        if answer.isdigit():
            return int(answer)
        print("Please type a number only.")
def pause():
    input("\nPress Enter to continue...")


def show_list(items):
    number = 1
    for item in items:
        print(number, ".", item)
        number = number + 1
def add_favourite(name):
    if name in favourites:
        print(name, "is already in favourites.")
    else:
        favourites.append(name)
        print(name, "added to favourites!")
def make_order(heading, menu):
    title(heading)
    items = list(menu.keys())
    total = 0
    bill = []

    while True:
        number = 1
        for item in items:
            print(number, ".", item, "- Rs", menu[item])
            number = number + 1
        print("0 . Finish")

        choice = ask_number("Choose item number: ")

        if choice == 0:
            break
        elif 1 <= choice <= len(items):
            name = items[choice - 1]
            quantity = ask_number("How many? ")
            total = total + menu[name] * quantity
            bill.append(name + " x" + str(quantity))
            print("Added", name, "x", quantity)
        else:
            print("Wrong number.")

    title("YOUR BILL")
    if len(bill) == 0:
        print("You did not choose anything.")
    else:
        for b in bill:
            print(b)
        print()
        print("Total = Rs", total)
    pause()


def show_menu(place):
    title(place + " MENU")
    menu = special_block[place]
    for item in menu:
        print("-", item, ": Rs", menu[item])
    print()
    print("Info:", special_info[place])
    pause()
def place_options(place):
    while True:
        title(place)
        print("1. Show menu")
        print("2. Order food")
        print("3. Add to favourites")
        print("4. Back")

        choice = ask_number("Enter choice: ")

        if choice == 1:
            show_menu(place)
        elif choice == 2:
            make_order("ORDER FROM " + place.upper(), special_block[place])
        elif choice == 3:
            add_favourite(place)
        elif choice == 4:
            break
        else:
            print("Wrong choice.")
def special_block_section():
    while True:
        title("SPECIAL BLOCK")
        places = list(special_block.keys())
        show_list(places)
        print(len(places) + 1, ". Back")

        choice = ask_number("Choose a place: ")

        if 1 <= choice <= len(places):
            place_options(places[choice - 1])
        elif choice == len(places) + 1:
            break
        else:
            print("Wrong number.")
def hostel_section():
    title("BOYS HOSTEL")
    for block in boys_hostel:
        print(block, "->", boys_hostel[block])
    print()
    print("Facilities: Gym, Sports courts")
    pause()
def courts_section():
    while True:
        title("SPORTS COURTS")
        show_list(courts)
        print(len(courts) + 1, ". Back")

        choice = ask_number("Choose a court: ")

        if 1 <= choice <= len(courts):
            court = courts[choice - 1]
            print("\nYou selected", court, "court.")
            answer = input("Add to favourites? (yes/no): ")
            if answer.lower() == "yes":
                add_favourite(court + " court")
        elif choice == len(courts) + 1:
            break
        else:
            print("Wrong number.")

def shops_section():
    while True:
        title("SHOPS")
        print("1. Shop locations")
        print("2. Items and prices")
        print("3. Buy items")
        print("4. Back")

        choice = ask_number("Enter choice: ")

        if choice == 1:
            for shop in shops:
                print(shop, "is in:", ", ".join(shops[shop]))
            pause()
        elif choice == 2:
            for item in shop_items:
                print("-", item, ": Rs", shop_items[item])
            pause()
        elif choice == 3:
            make_order("BUY ITEMS", shop_items)
        elif choice == 4:
            break
        else:
            print("Wrong choice.")

def ab1_section():
    title("AB1 BUILDING")
    print("Teachers cabin ->", ab1_info["Teachers cabin"])
    print("Cafes:")
    for cafe in ab1_info["Cafes"]:
        print("  -", cafe)
    pause()
def search_section():
    title("SEARCH")
    word = input("Type a name to search: ").lower()
    found = False

    for place in special_block:
        if word in place.lower():
            print("Special Block:", place)
            found = True

    for court in courts:
        if word in court.lower():
            print("Court:", court)
            found = True

    for shop in shops:
        if word in shop.lower():
            print("Shop:", shop)
            found = True

    for block in boys_hostel:
        if word in block.lower():
            print("Boys Hostel:", block)
            found = True

    for item in shop_items:
        if word in item.lower():
            print("Shop item:", item)
            found = True

    if found == False:
        print("Nothing found for", word)
    pause()
def favourites_section():
    title("MY FAVOURITES")
    if len(favourites) == 0:
        print("No favourites yet.")
    else:
        show_list(favourites)
        answer = input("\nRemove one? (yes/no): ")
        if answer.lower() == "yes":
            num = ask_number("Enter number to remove: ")
            if 1 <= num <= len(favourites):
                removed = favourites.pop(num - 1)
                print(removed, "removed.")
            else:
                print("Wrong number.")
    pause()

def main():
    print("=" * 40)
    print("      WELCOME TO VIT GUIDE")
    print("=" * 40)
    name = input("What is your name? ")
    print("Hello", name + "! Let's start.")

    while True:
        title("MAIN MENU")
        print("1. Special block")
        print("2. Boys hostel")
        print("3. Sports courts")
        print("4. Shops")
        print("5. AB1 building")
        print("6. Search")
        print("7. My favourites")
        print("0. Exit")

        choice = ask_number("Enter your choice: ")

        if choice == 1:
            special_block_section()
        elif choice == 2:
            hostel_section()
        elif choice == 3:
            courts_section()
        elif choice == 4:
            shops_section()
        elif choice == 5:
            ab1_section()
        elif choice == 6:
            search_section()
        elif choice == 7:
            favourites_section()
        elif choice == 0:
            print("\nThanks for using VIT Guide,", name + "!")
            break
        else:
            print("Wrong choice, try again.")
main()
