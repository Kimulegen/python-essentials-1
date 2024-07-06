def is_year_leap(year):
    if year % 4 == 0:
        if (year / 100) % 2 == 1:
            return False
        else:
            return True
    return False


days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(year, month):
    if year < 1582 or not (1 <= month <= 12):
        return
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_by_month[month - 1]


test_years = [1900, 2000, 2016, 1987, 1900]
test_months = [2, 2, 1, 11, 13]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
