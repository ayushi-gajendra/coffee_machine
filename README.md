# ☕ Coffee Machine in Python

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A terminal-based coffee machine simulation that manages resources, takes payments, calculates change, and dispenses coffee — all using Python!

---

## 🔧 Features

- Supports 3 drinks: `espresso`, `latte`, and `cappuccino`
- Tracks ingredients (`water`, `milk`, `coffee`) and money
- Checks resource sufficiency before making coffee
- Accepts coins: quarters, dimes, nickels, and pennies
- Calculates and returns change
- Special commands:
  - `report`: prints current resource and money status
  - `off`: turns off the machine

---

## 🧠 Python Concepts Used

- **Functions**: For checking resources, processing coins, and making coffee
- **Dictionaries**: For menu and resource management
- **Control Flow**: Conditional logic, loops, boolean flags
- **Input Handling**: Accepts and validates user input
- **Global Variables**: For shared state (`profit`, `resources`)

---

## ▶️ How to Run

1. Make sure you have **Python 3.7+** installed.  
2. Clone this repository:  
```
git clone https://github.com/ayushi-gajendra/coffee_machine.git
cd coffee_machine
```
3. Run the program:
```
python main.py
```
---

⚙️ Project Structure
coffee_machine/
├── main.py              # main logic of the simulator
└── README.md            # this documentation
