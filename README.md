# VIT Guide

A simple **Python-based terminal application** that provides useful VIT Bhopal campus information such as food places, shops, hostel blocks, sports courts, AB1 building information, search, favourites, ordering, and bill calculation.

## 👨‍💻 Project Details

| Detail | Information |
|---|---|
| **Project Name** | VIT Guide |
| **Student** | Abhishek Kumar |
| **Registration No.** | 26BCE10471 |
| **Institute** | VIT Bhopal University |
| **Language** | Python 3 |
| **Interface** | Terminal / Command Line |
| **Project Type** | Academic Mini Project |
| **Academic Year** | 2026–2027 |

## 📌 Project Overview

VIT Guide is designed as a lightweight campus utility program for students.

The application provides a menu-driven interface where users can:

- Explore Special Block places
- View food menus and prices
- Place sample food orders
- Calculate bills automatically
- View boys hostel blocks
- Explore sports courts
- View shop locations
- View shop item prices
- Buy items through a simple order system
- View AB1 building information
- Search for campus places and items
- Add places/courts to favourites
- Remove favourites

The project is intentionally built without a database, web server, API, or external library so that the Python logic remains easy to understand.

## ✨ Features

### 1. Special Block

Contains information about:

- AB Darshan
- Bistro
- Mayuri
- Gym
- Dentist

Users can:

- View menu
- View prices
- Place an order
- Add a place to favourites

### 2. Boys Hostel

Displays available hostel blocks and basic location information.

### 3. Sports Courts

Currently includes:

- Basketball
- Volleyball
- Football
- Badminton
- Tennis

Users can also add a selected court to favourites.

### 4. Shops

Provides:

- Shop locations
- Item prices
- Simple purchasing system

Example items:

- Notebook
- Pen
- Water Bottle
- Biscuits
- Chips
- Cold Drink

### 5. AB1 Building

Displays basic information about:

- Teachers' cabin / proctor
- Cafes

### 6. Search

The search system allows users to search using partial names.

It searches across:

- Special Block places
- Sports courts
- Shops
- Hostel blocks
- Shop items

Search is case-insensitive.

### 7. My Favourites

Users can:

- Add places/courts
- View saved favourites
- Remove a favourite

### 8. Ordering and Billing

The ordering system allows the user to:

1. Select an item
2. Enter quantity
3. Add the item to the order
4. Continue ordering
5. Finish the order
6. View the final bill

The total is calculated using:

```text
Total = Item Price × Quantity
```

## 🛠️ Technologies Used

- Python 3
- Lists
- Dictionaries
- Nested dictionaries
- Functions
- Loops
- Conditional statements
- String methods
- User input
- Basic input validation
- Terminal / Command Prompt

No external Python packages are required.

## 📂 Project Structure

```text
VIT-Guide/
│
├── vit_guide.py
├── README.md
└── VIT_Guide_Project_Report_Abhishek_Kumar.pdf
```

> The Python file name can be changed if required.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed.

Check using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Download / Clone the Project

If the project is hosted on GitHub:

```bash
git clone <repository-url>
```

Then enter the project folder:

```bash
cd VIT-Guide
```

### Step 3: Run the Program

On Windows:

```bash
python vit_guide.py
```

On Linux/macOS:

```bash
python3 vit_guide.py
```

## 🖥️ Example

When the program starts:

```text
========================================
      WELCOME TO VIT GUIDE
========================================
What is your name? Abhishek
Hello Abhishek! Let's start.

----------------------------------------
   MAIN MENU
----------------------------------------
1. Special block
2. Boys hostel
3. Sports courts
4. Shops
5. AB1 building
6. Search
7. My favourites
0. Exit
----------------------------------------
Enter your choice:
```

## 🧠 Python Concepts Demonstrated

### Dictionaries

Used to store structured information such as menus and prices.

```python
special_block = {
    "Bistro": {
        "Burger": 80,
        "Pizza": 120,
        "Cold Coffee": 60
    }
}
```

### Lists

Used for collections such as courts and favourites.

```python
courts = [
    "Basketball",
    "Volleyball",
    "Football",
    "Badminton",
    "Tennis"
]
```

### Functions

The program is divided into multiple functions to make the code modular.

Examples:

```python
def ask_number(message):
def add_favourite(name):
def make_order(heading, menu):
def search_section():
```

### Loops

`while` loops are used to keep menus running until the user chooses to go back or exit.

### Conditions

`if`, `elif`, and `else` statements control user choices.

### String Handling

The search feature uses:

```python
word.lower()
```

to perform case-insensitive searching.

## 🧪 Testing

| Test | Expected Result |
|---|---|
| Enter a valid menu number | Correct section opens |
| Enter letters instead of a number | Program asks for a number |
| Add a favourite | Item is added |
| Add the same favourite again | Duplicate warning appears |
| Search for an existing item | Matching result appears |
| Search for unknown item | "Nothing found" message appears |
| Place an order | Items and total are displayed |
| Remove favourite | Selected favourite is removed |
| Select Exit | Program closes |

## ⚠️ Limitations

This is an academic prototype and not an official VIT campus information system.

Current limitations include:

- Data is hard-coded in Python.
- Favourites are not permanently saved.
- No database is used.
- No student login system.
- No real-time booking system.
- No real-time price or availability updates.
- Terminal interface only.

Campus-specific information should be verified before using the application as an official campus service.

## 🚀 Future Improvements

Possible future versions could include:

- SQLite/MySQL database
- Student login
- Persistent favourites
- Order history
- GUI interface
- Web application
- Admin panel
- Verified campus locations
- Opening/closing timings
- Real-time availability
- Campus map/navigation
- Better error handling
- Unit testing

## 🎯 Learning Outcome

This project helped demonstrate how fundamental Python concepts can be combined to create a complete interactive application.

The main concepts practiced include:

- Variables
- Lists
- Dictionaries
- Nested dictionaries
- Functions
- Loops
- Conditions
- Input validation
- String manipulation
- List operations
- Modular programming
- Basic application design

## 📄 Project Report

A detailed project report is included with the project:

**VIT_Guide_Project_Report_Abhishek_Kumar.pdf**

## 👤 Author

**Abhishek Kumar**  
**Reg. No.: 26BCE10471**  
**VIT Bhopal University**

---

⭐ If this project is useful for learning Python, consider improving it by adding persistent storage, better validation, and a graphical interface.
