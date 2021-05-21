def main():
    dates = []
    dates.append(input("Введите первую дату: "))
    dates.append(input("Введите вторую дату: "))


def date_days(date):
    days = 0

    is_american = False
    is_alpha = False

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

        if 

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


if __name__ == "__main__":
    main()
