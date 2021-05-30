def main():
    dates = []
    dates.append(input("Введите первую дату: "))
    dates.append(input("Введите вторую дату: "))

    print(abs(date_days(dates[0]) - date_days(dates[1])))


def date_days(date):
    days = 0

    is_american = False
    is_alpha = False
    is_leap = False

    if date[0].isalpha():
        month = month_parse(date[0:3])
        is_american = True
        is_alpha = True

    if date[3].isalpha() and not is_american:
        month = month_parse(date[3:6])
        is_alpha = True

    if is_alpha:
        if is_american:
            delim = date[3]

            date = date.split(delim)

            days += int(date[1])
        else:
            delim = date[2]

            date = date.split(delim)

            days += int(date[0])
    else:
        delim = date[2]

        date = date.split(delim)

        if int(date[1]) > 12:
            is_american = True

        elif int(date[0]) <= 12:
            if input("Это американский формат записи даты? лат 'y' Да") == 'y':
                is_american = True

        if is_american:
            days += int(date[1])
            month = int(date[0]) - 1
        else:
            days += int(date[0])
            month = int(date[1]) - 1

    days += days_in_months(month)

    year = int(date[2])

    if not (year % 100) and (year % 400):
        is_leap = False
    elif not (year % 4):
        is_leap = True

    if (month > 1) and is_leap:
        days += 1

    days += year * 365
    
    leap_years = 0

    leap_years += (year - 1) // 4
    
    leap_years -= (year - 1) // 100

    leap_years += (year - 1) // 400

    days += leap_years

    return days


def month_parse(month):
    months = {}
    for i, mon in enumerate(("jan", "feb", "mar", "apr", "may", "jun",
                        "jul", "aug", "sep", "oct", "nov", "dec")):
        months[mon] = i
    for i, mon in enumerate(("янв", "фев", "мар", "апр", "май", "июн",
                        "июл", "авг", "сен", "окт", "ноя", "дек")):
        months[mon] = i

    month = month.lower()

    return months[month]

def days_in_months(month):
    months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days_at_all = 0

    for i in range(month):
        days_at_all += months[i]

    return days_at_all


if __name__ == "__main__":
    main()
