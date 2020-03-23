def is_twodigit(number):
    return len(str(number)) == 2 and int(number) % 2 != 0


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0


def is_sunday(day, weekday_of_first):
    if weekday_of_first == 'M':
        weekday_of_first = 1
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'T':
        weekday_of_first = 2
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'W':
        weekday_of_first = 3
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'Th':
        weekday_of_first = 4
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'F':
        weekday_of_first = 5
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'Sa':
        weekday_of_first = 6
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    if weekday_of_first == 'S':
        weekday_of_first = 7
        if ((weekday_of_first - 1) + day) % 7 == 0 and (weekday_of_first - 1) + day <= 31:
            return True
    else:
        return False


print(is_sunday(7, 'W'))


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return rains and wind_scale < 7 or ((cloudy and wind_scale < 7) and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) or (wind_scale < 7 and strong_sunshine)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
