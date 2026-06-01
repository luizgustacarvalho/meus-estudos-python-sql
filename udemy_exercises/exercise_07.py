# =============================================================
# 1. DATA DEFINITIONS AND IMPORTS (PEP 8 Standard)
# =============================================================
import copy

# Original product catalog (remains immutable)
products = [
    {'name': 'Macarrão', 'preco': 10.00},
    {'name': 'Feijão', 'preco': 22.32},
    {'name': 'Arroz', 'preco': 10.11},
    {'name': 'Macaxeira', 'preco': 105.87},
    {'name': 'Batata Doce', 'preco': 69.90},
]

empty_prices_list = []  # Kept for compatibility with original structure
price_multiplier = 1.1

# =============================================================
# 2. INTERACTIVE SALES INTERFACE (Robust Error Handling)
# =============================================================
while True:
    user_input = input("""
Please choose a product:
1- Macarrão (Type 0)
2- Feijão (Type 1)
3- Arroz (Type 2)
4- Macaxeira (Type 3)
5- Batata Doce (Type 4) >> """)

    try:
        product_index = int(user_input)

        # Validation: Check if the index is out of bounds
        if product_index < 0 or product_index > 4:
            print(f'ERROR: The option {product_index} does not correspond to any registered product.')

            try_again = input('Would you like to try again? [Y/N]: ').strip().upper()
            if try_again == 'Y':
                continue
            else:
                print('Closing the sales system.')
                break

                # Process valid product selections dynamically
        if product_index == 0:
            current_price = products[0]['preco']
            updated_price = current_price * price_multiplier
            print(f'Original product price: $ {current_price:.2f}')
            print(f'New price with 10% increase: $ {updated_price:.2f}')

        elif product_index == 1:
            current_price = products[1]['preco']
            updated_price = current_price * price_multiplier
            print(f'Original product price: $ {current_price:.2f}')
            print(f'New price with 10% increase: $ {updated_price:.2f}')

        elif product_index == 2:
            current_price = products[2]['preco']
            updated_price = current_price * price_multiplier
            print(f'Original product price: $ {current_price:.2f}')
            print(f'New price with 10% increase: $ {updated_price:.2f}')

        elif product_index == 3:
            current_price = products[3]['preco']
            updated_price = current_price * price_multiplier
            print(f'Original product price: $ {current_price:.2f}')
            print(f'New price with 10% increase: $ {updated_price:.2f}')

        elif product_index == 4:
            current_price = products[4]['preco']
            updated_price = current_price * price_multiplier
            print(f'Original product price: $ {current_price:.2f}')
            print(f'New price with 10% increase: $ {updated_price:.2f}')

        # Break the loop on successful execution
        break

    except ValueError:
        print('ERROR: Invalid input. Please enter integers only.')

        try_again = input('Would you like to try again? [Y/N]: ').strip().upper()
        if try_again == 'Y':
            continue
        else:
            print('Closing the sales system.')
            break

# =============================================================
# 3. COURSE CHALLENGE RESOLUTION (Data Processing)
# =============================================================
# Requirement 1: Generate new_products with a 10% price increase via deep copy
new_products = copy.deepcopy(products)

for product in new_products:
    product['preco'] *= price_multiplier
    product['preco'] = round(product['preco'], 2)

# Requirement 2: Sort products by name in descending order (Z-A)
products_sorted_by_name = copy.deepcopy(new_products)
products_sorted_by_name = sorted(
    products_sorted_by_name,
    key=lambda item: item['name'],
    reverse=True
)

# Requirement 3: Sort products by price in ascending order (Low to High)
products_sorted_by_price = copy.deepcopy(new_products)
products_sorted_by_price = sorted(
    products_sorted_by_price,
    key=lambda item: item['preco']
)

# =============================================================
# 4. DATA DISPLAY (Challenge Verification)
# =============================================================
print('\n' + '=' * 50)
print('PROCESSED CHALLENGE DATA:')
print('=' * 50)

print('1. ORIGINAL PRODUCTS (Intact):')
print(*products, sep='\n')
print('-' * 50)

print('2. NEW PRODUCTS (Price + 10%):')
print(*new_products, sep='\n')
print('-' * 50)

print('3. PRODUCTS SORTED BY NAME (Descending):')
print(*products_sorted_by_name, sep='\n')
print('-' * 50)

print('4. PRODUCTS SORTED BY PRICE (Ascending):')
print(*products_sorted_by_price, sep='\n')