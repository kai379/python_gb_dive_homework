def is_leap_year(year_var: int) -> bool:
    return bool(not year_var % 4 and year_var % 100 or not year_var % 400)


def is_relevant_date(date: str) -> bool:
    if len(list_date := date.split('.')) == 3:
        day, month, year = map(int, list_date)
    else:
        print('Введена некорректная дата.')
        return False

    months = {1: 31, 2: 29 if is_leap_year(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    return 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= months[month]


if __name__ == '__main__':
    print(is_relevant_date('15.11.2000'))
    print(is_relevant_date('29.02.2000'))
    print(is_relevant_date('29.02.2001'))
    print(is_relevant_date('32.01.1941'))
