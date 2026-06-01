# =============================================================
# BANK LOAN ANALYSIS SYSTEM
# =============================================================

print("=== Bank Loan Analysis ===")
input_age = input('Enter your age: ')
input_salary = input('Enter your monthly salary: ')

try:
    # Convert inputs to appropriate numerical types
    age = int(input_age)
    salary = float(input_salary)

    # Validation business rules
    is_age_valid = 18 <= age <= 65
    is_salary_valid = salary >= 2500.00

    # Decision matrix for loan approval
    if is_age_valid and is_salary_valid:
        print('\n✅ STATUS: Loan Pre-Approved!')
    else:
        print('\n❌ STATUS: Loan Denied.')
        if not is_age_valid:
            print(f'- Reason: Age must be between 18 and 65 (Current: {age}).')
        if not is_salary_valid:
            print(f'- Reason: Minimum monthly salary required is $ 2,500.00 (Current: $ {salary:.2f}).')

except ValueError:
    # Handle non-numeric inputs gracefully
    print('\n⚠️ ERROR: Please enter valid numbers for age and salary.')