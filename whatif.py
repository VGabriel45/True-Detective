def is_twodigit(number):
    if len(str(number)) == 2:
        if int(number) % 2 != 0:
            return True
    else:
        return False


print(is_twodigit('21'))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(is_leap_year(1900))


# def is_sunday(day, weekday_of_first):
#     pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if rains:
        if wind_scale < 7:
            return True
        else:
            return False
    if cloudy:
        if wind_scale < 7:
            if red_sky:
                return True
            elif strong_flower_smell:
                return True
            elif spiders_down:
                return True
            elif lying_cattle:
                return True
            else:
                return False
        else:
            return False
    if strong_sunshine:
        if wind_scale < 7:
            return True
        else:
            return False
    else:
        return False


# def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
# pass
