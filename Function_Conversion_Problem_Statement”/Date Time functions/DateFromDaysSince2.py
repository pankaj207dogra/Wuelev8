def get_DateFromDaysSince2():
    days = str(int(utc_now().split('-')[2]) + 2)
    newdt = ts.split('-')[0] + '-' + ts.split('-')[1] + '-' + days
    return newdt