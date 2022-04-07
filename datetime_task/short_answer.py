import datetime as dt


def update_date(str_date, number):
    date = dt.datetime.strptime(str_date, '%d/%m/%y').date()
    date += dt.timedelta(days=number)
    return date


str_date = '25/02/21'
number = 5
date = update_date(str_date, number)
print(date)
