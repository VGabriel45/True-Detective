days = {'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6, 'S': 7}


def is_twodigit(number):
    if len(str(number)) == 2:
        if int(number) % 2 != 0:
            return True
    else:
        return False


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


def is_sunday(day, weekday_of_first):
    if weekday_of_first in days.keys():
        if (((days[weekday_of_first] - 1) + day) % 7 == 0):
            if ((days[weekday_of_first] - 1) + day <= 31):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


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


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if not trouble_sleeping:
            if not after_4pm:
                if not at_work:
                    if have_30m:
                        return True
                    else:
                        if have_10m:
                            return True
                        else:
                            return False
                elif not mad_boss:
                    if have_30m:
                        return True
                    elif have_10m:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
