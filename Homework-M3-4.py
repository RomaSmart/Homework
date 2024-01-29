import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users=None):
    today_date = dtdt.today().date() # беремо сьогоднішню дату
    upcoming_birthdays = [] # створюємо список для результатів

    for user in users: # перебираємо користувачів
        birthdate_str = user["birthday"] # отримуємо дату народження людини у вигляді рядка
        birthdate_str = f"{today_date.year}.{birthdate_str[5:]}" # Замінюємо рік на поточний
        birthdate = dtdt.strptime(birthdate_str, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        days_until_birthday = (birthdate - today_date).days # рахуємо різницю між зараз і днем народження цьогоріч у днях
        weekday = birthdate.isoweekday() # Отримуємо день тижня (1-7)

        if 0 <= days_until_birthday < 7 and weekday < 6:  # якщо день народження протягом 7 днів від сьогодні і в будні (Від Понеділка по П'ятницю)
            upcoming_birthdays.append({'name': user['name'], 'birthday': birthdate.strftime("%Y.%m.%d")})  # Додаємо запис у список.
        # Перевіряємо чи День Народження припадає на вихідні дні:
        elif days_until_birthday == 0 and weekday >= 6:
            next_monday = today_date + dt.timedelta(days=(7 - weekday) + 1)  # Якщо Субота чи Неділя то переносимо на Понеділок
            upcoming_birthdays.append({'name': user['name'], 'birthday': next_monday.strftime("%Y.%m.%d")})
                
    return upcoming_birthdays

    # Список як приклад:
users = [{"name": "John Doe", "birthday": "1985.01.23"},
         {"name": "Jane Smith", "birthday": "1990.01.27"},
         {"name": "Jane Smith", "birthday": "2000.01.29"},
         {"name": "Jane Smith", "birthday": "1998.01.30"}] 

print(get_upcoming_birthdays(users))