# Завдання 2
# Функція яка допоможе генерувати набір унікальних випадкових чисел для лотерей.

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    try:
        # Check for invalid range
        if min < 1 or max > 1000:
            raise ValueError

        # Generate a random list of "quantity" unique numbers between "min" and "max"
        random_numbers = random.sample(range(min, max+1), quantity)

        # Sort the list
        random_numbers.sort()

        return (f"Your lottery numbers: {random_numbers}")
    
    except Exception:
       
       # Return error message in case of wrong entries
       return (f"Somefing went wrong. Please check your entries: {[]}")

# Test the function
print(get_numbers_ticket(1, 1000, 6))
print(get_numbers_ticket(1, 1, 1))
print(get_numbers_ticket(0, 0, 0))
print(get_numbers_ticket(-1, -3, -1))
print(get_numbers_ticket(1001, 1001, 1))
print(get_numbers_ticket(1, 3, 4))
print(get_numbers_ticket(3, 1, 2))
print(get_numbers_ticket("1", "six", 3))
print(get_numbers_ticket(1, 3, "2"))


