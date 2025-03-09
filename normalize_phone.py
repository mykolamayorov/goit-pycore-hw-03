# Завдання 3
# Функція що нормалізує телефонні номери до стандартного формату +380XXXXXXXXX.

import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234+5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123+32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number: str) -> str:

    # Remove all non-digit
    phone_number = re.sub(r"\D", '', phone_number)

    # Add "+" to the number
    phone_number = '+' + phone_number

    # Check if number starts with "+3", if not then update number
    match1 = re.search(r"^\+3", phone_number)
    if match1 == None:
        phone_number = phone_number[:1] + "3" + phone_number[1:]

    # Check if number starts with "+38", if not then update number
    match2 = re.search(r"^\+38", phone_number)
    if match2 == None:
        phone_number = phone_number[:2] + "8" + phone_number[2:]

    # Check if number starts with "+380", if not then update number
    match3 = re.search(r"^\+380", phone_number)
    if match3 == None:
        phone_number = phone_number[:3] + "0" + phone_number[3:]
    
    # Return sanitized number
    return phone_number

# Function test
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)