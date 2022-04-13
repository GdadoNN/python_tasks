import datetime as dt

# Globals
INVALID_INPUT = -1


def get_feb_days(year):
    # loop year means
    # the year divided by 4 but not in 100,
    # the year divided by 400
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    else:
        return 28


def get_next_month_date(date, months_map):
    if (date.month + 1) == 13:
        cur_year_feb = get_feb_days(date.year + 1)
        months_map['February'] = int(cur_year_feb)
        return date.replace(day=1, month=1, year=date.year + 1)
    return date.replace(day=1, month=date.month + 1)


def update_last_month(date, number):
    return date.replace(day=number, month=date.month)


def update_days(reset_date, months_map, number):
    month = reset_date.strftime("%B")
    num_days_in_month = months_map.get(month)
    # num_days_in_month = num_days_in_month - 1
    if num_days_in_month > number:
        curr_date = update_last_month(reset_date, number)
        number = 0
        return curr_date, number
    number = number - num_days_in_month
    reset_date = get_next_month_date(reset_date, months_map)
    return reset_date, number


def how_many_days_in_month(date, number):
    long = 31
    short = 30
    month = date.strftime("%B")
    months_map = {
        'January': long,
        'February': get_feb_days(date.year),
        'March': long,
        'April': short,
        'May': long,
        'July': long,
        'June': short,
        'August': long,
        'September': short,
        'October': long,
        'November': short,
        'December': long
    }

    # Today
    current_day_in_month = date.day
    # Get number of days in month by month
    num_days_in_month = months_map.get(month)
    # number of days in month - today date equal the amount of days left to end the month.
    days_left_in_month = num_days_in_month - current_day_in_month
    # create future date at next month (1.X) if next month is in next year += to the year and make month at (1.1)
    number = number - days_left_in_month
    reset_date = get_next_month_date(date, months_map)
    while number > 0:
        reset_date, number = update_days(reset_date, months_map, number)

    return reset_date


def update_date(str_date, number):
    date = dt.datetime.strptime(str_date, '%d/%m/%Y').date()
    new_date = how_many_days_in_month(date, number)

    date = str(new_date.day) + "/" + str(new_date.month) + "/" + str(new_date.year)
    date = dt.datetime.strptime(date, '%d/%m/%Y').date()
    return date


if __name__ == "__main__":
    str_date = '2/12/2020'
    number = 90
    date = update_date(str_date, number)
    print(date)
