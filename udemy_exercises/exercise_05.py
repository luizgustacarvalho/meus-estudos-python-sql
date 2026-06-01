# =============================================================
# SECTION 1: STRING AND NAME LENGTH ANALYSIS
# =============================================================
name = input('Enter your name: ').strip()

# Calculate length excluding internal spaces
name_length = len(name.replace(' ', ''))

if name_length > 0:
    print(f'Welcome, {name}!')
    if name_length <= 4:
        print('Your name is short.')
    elif 5 <= name_length <= 6:
        print('Your name is normal-sized.')
    else:
        print('Your name is very long.')
else:
    print('Error: Name cannot be empty.')

# =============================================================
# SECTION 2: PARITY CHECK (EVEN OR ODD)
# =============================================================
number_input = input('Enter an integer: ')

# Check if the input consists of digits only
if number_input.isdigit():
    number = int(number_input)
    result = "even" if number % 2 == 0 else "odd"
    print(f'The number {number} is {result}.')
else:
    print('Error: Please enter a valid integer.')

# =============================================================
# SECTION 3: TIME-BASED GREETING SYSTEM
# =============================================================
hour_input = input('Current hour (0-23): ')

try:
    hour = int(hour_input)

    # Check bounds and determine the correct greeting
    if 0 <= hour <= 11:
        print("Good morning!")
    elif 12 <= hour <= 17:
        print("Good afternoon!")
    elif 18 <= hour <= 23:
        print("Good evening!")
    else:
        print("Error: Hour must be between 0 and 23.")

except ValueError:
    # Handle non-integer inputs for the hour field
    print("Error: Invalid hour format. Please enter numbers only.")