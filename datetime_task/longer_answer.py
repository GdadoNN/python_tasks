import datetime as dt

# Globals
INVALID_INPUT = -1


def check_leap_year(year):
    # All the years that are perfectly divisible by 4 are called Leap years except the century years.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # because is a leap year February month has 29 days.
        print(year, " is a leap year")
        leap_year = True
    else:
        # not leap year means February has only 28 days.
        print(year, " is not a leap year")
        leap_year = False
    return leap_year


def how_many_days_in_month(date):
    days_in_month = INVALID_INPUT
    month = date.strftime("%B")
    February = 'February'
    long_months = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    short_months = ['April', 'June', 'September', 'November']
    if month in long_months:
        days_in_month = 31
    elif month in short_months:
        days_in_month = 30
    elif month == February:
        leap_year = check_leap_year(date.year)
        if leap_year:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        print("invalid input")
    return days_in_month


def update_date(str_date, number):
    date = dt.datetime.strptime(str_date, '%d/%m/%Y').date()
    year = date.year
    month = date.month
    day = date.day
    days_in_month = how_many_days_in_month(date)
    get_day = day + number
    if get_day > days_in_month:
        get_day = get_day - days_in_month
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

    date = str(get_day) + "/" + str(month) + "/" + str(year)
    date = dt.datetime.strptime(date, '%d/%m/%Y').date()

    return date


if __name__ == "__main__":
    str_date = '25/12/2020'
    number = 8
    date = update_date(str_date, number)
    print(date)
