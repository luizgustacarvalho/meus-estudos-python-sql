"""
Loan Approval System
Validates age and income requirements for financial services.
"""

print("=== Bank Loan Analysis ===")

entry_age = input('Enter your age: ')
entry_salary = input('Enter your monthly salary: ')

try:
    age = int(entry_age)
    salary = float(entry_salary)

    # Business Rules (Flags)
    age_ok = 18 <= age <= 65
    salary_ok = salary >= 2500

    if age_ok and salary_ok:
        print('\n✅ STATUS: Loan Pre-Approved!')
    else:
        print('\n❌ STATUS: Loan Denied.')
        if not age_ok:
            print(f'- Requirement fail: Age must be between 18 and 65 (Current: {age}).')
        if not salary_ok:
            print(f'- Requirement fail: Minimum salary is R$ 2.500,00 (Current: R$ {salary:.2f}).')

except ValueError:
    print('\n⚠️ ERROR: Please enter valid numbers for age and salary.')