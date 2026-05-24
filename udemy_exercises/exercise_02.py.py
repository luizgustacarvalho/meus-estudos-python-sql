name = input('Type your name: ')
age = input('Type your age: ')

if name and age:
    print(f'Name: {name} | Age: {age}')
    if int(age) >= 18: print('Status: Adult.')
    else: print('Status: Minor.')

    if ' ' in name: print('Has spaces.')
    else: print('No spaces.')

    print(f'Reversed: {name[::-1]}')
    print(f'Total chars: {len(name)}')
    print(f'First: {name[0]} | Last: {name[-1]}')
else:
    print('❌ Error: Empty fields.')