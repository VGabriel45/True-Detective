days = {'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6, 'S': 7}


def is_twodigit(number):
    return len(str(number)) == 2 and int(number) % 2 != 0


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return True if user in users_groups or file_owner and (writable_by_owner == True) or (file_group and writable_by_group == True) or (writable_by_others and sudo_mode == True) else False


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0


def is_sunday(day, weekday_of_first):
    return True if weekday_of_first and days.keys() and (((days[weekday_of_first] - 1) + day) % 7 == 0) and ((days[weekday_of_first] - 1) + day <= 31) else False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return rains and wind_scale < 7 or ((cloudy and wind_scale < 7) and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) or (wind_scale < 7 and strong_sunshine)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return (want_to and not trouble_sleeping and not after_4pm) and ((not at_work and have_30m or have_10m) or (at_work and not mad_boss and (have_30m or have_10m)))
