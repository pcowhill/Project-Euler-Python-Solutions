import math

def datez():
    day = 2 #Sunday is 1, Monday is 2
    date = 1
    month = 1
    year = 1900
    total = 0
    while year < 2001:
        if (date == 1) and (day == 1) and (year>1900):
            total += 1
        day += 1
        date += 1
        if day == 8:
            day = 1
        if month in [9,4,6,11]:
            if date == 31:
                date = 1
        elif month == 2:
            if (year%4==0) and (year%100!=0 or year%400==0):
                if date == 30:
                    date = 1
            else:
                if date == 29:
                    date = 1
        else:
            if date == 32:
                date = 1
        if date == 1:
            month += 1
        if month == 13:
            month = 1
            year += 1
    print(total)
