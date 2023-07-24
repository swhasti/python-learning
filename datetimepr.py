import datetime


def get_weekday(wd):
    if wd == 0:
        return "Monday"
    elif wd == 1:
        return "Tuesday"
    elif wd == 2:
        return "Wednesday"
    elif wd == 3:
        return "Thursday"
    elif wd == 4:
        return "Friday"
    elif wd == 5:
        return "Saturday"
    elif wd == 6:
        return "Sunday"
    else:
        return "Unknown"


def get_month(mt):
    if mt == 1:
        return "January"
    elif mt == 2:
        return "February"
    elif mt == 3:
        return "March"
    elif mt == 4:
        return "April"
    elif mt == 5:
        return "May"
    elif mt == 6:
        return "June"
    elif mt == 7:
        return "July"
    elif mt == 8:
        return "August"
    elif mt == 9:
        return "September"
    elif mt == 10:
        return "october"
    elif mt == 11:
        return "November"
    elif mt == 12:
        return "December"
    else:
        return "Unknown"


def get_days_per_month(m):
    if m == 1:
        return 31
    elif m == 2:
        return 28
    elif m == 3:
        return 31
    elif m == 4:
        return 30
    elif m == 5:
        return 31
    elif m == 6:
        return 30
    elif m == 7:
        return 31
    elif m == 8:
        return 31
    elif m == 9:
        return 30
    elif m == 10:
        return 31
    elif m == 11:
        return 30
    elif m == 12:
        return 31
    else:
        return "Unknown"


def is_leap_year(lp):
    if lp % 4 == 0:
        return True
    else:
        return False


print("------ End Datetime ------")
dt = datetime.datetime.now()
print(dt)

print("------ End Day -------")

day = dt.day
print(day)

print("------- End Month -------")

month = dt.month
mt = get_month(month)
print(mt)
print(month)

print("-------- End Weekday --------")

weekday = dt.weekday()
wd = get_weekday(weekday)
print(wd)

print("-------- End Hour -------")

hour = dt.hour
print(hour)

print("-------- End Year --------")

year = dt.year
ly = is_leap_year(year)
print("is leap year: {}".format(ly))
print(year)

print("------- End Second --------")

second = dt.second
print(second)

print("-------- End Minute ---------")

minute = dt.minute
print(minute)

print("--------- End ---------")

month = dt.month
m = get_days_per_month(month)
print(m)
print(month)

