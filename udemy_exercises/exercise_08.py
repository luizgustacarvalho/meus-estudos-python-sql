# =============================================================
# CLOSURE AND DELAYED FUNCTION EXECUTION CHALLENGE
# =============================================================

def sum_numbers(x, y):
    """Returns the sum of two numbers."""
    return x + y


def multiply_numbers(x, y):
    """Returns the product of two numbers."""
    return x * y


def execute_delayed(function_to_run, *args):
    """
    Creates a closure that freezes the initial arguments (*args)
    and delays the execution until the next arguments are provided.
    """
    def delayed_execution(*next_args):
        # Combines the initial arguments with the new ones and executes
        return function_to_run(*args, *next_args)

    return delayed_execution


# =============================================================
# FUNCTION GENERATION AND TESTING
# =============================================================

# Creating specialized functions with frozen initial states
add_five = execute_delayed(sum_numbers, 5)
multiply_by_ten = execute_delayed(multiply_numbers, 10)

# Executing the deferred functions with the remaining arguments
print(add_five(10))          # Expected Output: 15 (5 + 10)
print(multiply_by_ten(5))    # Expected Output: 50 (10 * 5)