def is_twodigit(number):
    return len(number) == 2 and int(number) % 2 != 0


print(is_twodigit('21'))


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0


def is_sunday(day, weekday_of_first):
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
