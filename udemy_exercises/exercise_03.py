"""
Python Utility Script: Name Analysis, Parity Check, and Time-based Greeting.
Developed as part of the backend learning track.
"""

# --- Section 1: Name Analysis ---
name = input('Type your name: ').strip()
# Count letters only (ignoring spaces)
name_length = len(name.replace(' ', ''))

if name_length > 0:
    print(f'Welcome, {name}!')
    if name_length <= 4:
        print('Status: You have a short name.')
    elif 5 <= name_length <= 6:
        print('Status: You have a normal-sized name.')
    else:
        print('Status: You have a very long name.')
else:
    print('Error: Name field cannot be empty.')

print('-' * 20)

# --- Section 2: Parity Check (Even/Odd) ---
entry_num = input('Enter an integer: ')

if entry_num.isdigit():
    number = int(entry_num)
    # Using ternary operator for clean code
    result = "even" if number % 2 == 0 else "odd"
    print(f'The number {number} is {result}.')
else:
    print('Error: Invalid integer.')

print('-' * 20)

# --- Section 3: Time-based Greeting ---
entry_hour = input('Current time (0-23): ')

try:
    hour = int(entry_hour)
    if 0 <= hour <= 11:
        print("Good morning!")
    elif 12 <= hour <= 17:
        print("Good afternoon!")
    elif 18 <= hour <= 23:
        print("Good evening!")
    else:
        print("Error: Hour must be between 0 and 23.")
except ValueError:
    print("Error: Please enter integers only for the time.")