# Завдання 4
# Функція яка допоможе визначати, кого з колег потрібно привітати з днем народження.
# Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.13"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jan Mitch", "birthday": "1979.03.09"}
]

def get_upcoming_birthdays(users: list) -> list:
    # Get today's date
    current_date = datetime.today().date()

    # List to store upcoming birthdays
    congratulation_list = []

    for user in users:
        # Change day string into date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Get the birthday date for this year 
        birthday_this_year = birthday.replace(year=current_date.year)

        # Check if the birthday has already passed this year, move to the next year
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        # Calculate the difference between the birthday and today's date
        days_to_birthday = (birthday_this_year - current_date).days

        # If the birthday is within the next 7 days
        if 0 <= days_to_birthday < 7:

            # Check if the birthday falls on a weekend (Saturday or Sunday)
            if birthday_this_year.weekday() >= 5:
                days_to_birthday += (7 - birthday_this_year.weekday())

            # Create congratulation list
            congratulation_date = current_date + timedelta(days=days_to_birthday)
            congratulation_list.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return congratulation_list

# Test function
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)