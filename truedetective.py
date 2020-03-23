def is_twodigit(number):
<<<<<<< HEAD
    return True if len(str(number)) == 2 and int(number) % 2 != 0 else False


# print(is_twodigit('11'))


def is_leap_year(year):
    # if year % 4 == 0 and year % 100 != 0:
    #     return True
    # if year % 100 == 0 and year % 400 == 0:
    #     return True
    # else:
    #     return False
    return True if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0 else False


# print(is_leap_year(1995))
=======
    return len(str(number)) == 2 and int(number) % 2 != 0


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0
>>>>>>> acc68ed612a7b476d345fc1a9c8e1e95e67ca0f5


def is_sunday(day, weekday_of_first):
    days = {'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6, 'S': 7}
    for key in days.keys():
        if (weekday_of_first == key) and (((days[key] - 1) + day) % 7 == 0) and ((days[key] - 1) + day <= 31):
            return True
    else:
        return False

    # if weekday_of_first == 'M':
    #     weekday_of_first = 1
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'T':
    #     weekday_of_first = 2
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'W':
    #     weekday_of_first = 3
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'Th':
    #     weekday_of_first = 4
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'F':
    #     weekday_of_first = 5
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'Sa':
    #     weekday_of_first = 6
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # if weekday_of_first == 'S':
    #     weekday_of_first = 7
    #     if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
    #         return True
    # else:
    #     return False


print(is_sunday(7, 'M'))


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return rains and wind_scale < 7 or ((cloudy and wind_scale < 7) and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) or (wind_scale < 7 and strong_sunshine)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
