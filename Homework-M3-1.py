from datetime import datetime
def get_days_from_today(date):
    try:
        enter_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        days_between = (current_date - enter_date).days
        return days_between
    except ValueError:
        return "Wrong date format. Please use 'YYYY-MM-DD'."
current_date = datetime.today().strftime("%Y-%m-%d")
result = get_days_from_today("2021-10-09")
print(f"If today is {current_date}, then between them left: {result} days")