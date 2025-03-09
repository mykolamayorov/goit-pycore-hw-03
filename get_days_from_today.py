# Завдання 1
# Функція яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime

def get_days_from_today(date: str) -> int:   
    try:
        # Convert date entry into string
        date = str(date)
    
        # Convert date string into datetime object, Get given date
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Get current date
        current_date = datetime.today().date()

        # Calculate date delta
        date_delta = current_date - given_date

        # Return date delta in days
        return date_delta.days
        
    except ValueError:

        # Return error message in case of wrong format entry
        return "Wrong Date format entry. Please use the following date format 'YYYY-MM-DD'."

# Test the function
print(get_days_from_today('2024-03-07'))
print(get_days_from_today('2026-03-07'))
print(get_days_from_today('ab23-*3--7'))
print(get_days_from_today(2025.2/3))
print(get_days_from_today(True))