def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def number_of_days_in(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap(year):
        return 29
    else:
        return 28
    
cur_weekday = 2  # Saturday is 0
cur_month = 1
cur_year = 1900

def progress_one_month():
    global cur_weekday, cur_month, cur_year
    cur_weekday = (cur_weekday + number_of_days_in(cur_month, cur_year)) % 7
    cur_month += 1
    if cur_month == 13:
        cur_month = 1
        cur_year += 1

def get_answer():
    # prepare the calculation for 1 Jan 1901
    while cur_year < 1901:
        progress_one_month()

    counter = 0
    while cur_year < 2001:
        if cur_weekday == 1:
            counter += 1
        progress_one_month()

    return counter

if __name__ == '__main__':
    print(get_answer())