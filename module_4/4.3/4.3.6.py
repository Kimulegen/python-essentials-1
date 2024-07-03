days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def is_year_leap(year):
    if year % 4 == 0:
        if (year / 100) % 2 == 1:
            return False
        else:
            return True
    return False


def days_in_month(year, month):
    if year < 0 or not (1 <= month <= 12):
        return
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_by_month[month - 1]


def day_of_year(year, month, day):
    if year < 0 or not (1 <= month <= 12) or not (1 <= day <= 31):
        return

    # THE REST OF THE FUNCTION


print(day_of_year(1789, 7, 21))
