import pendulum
from django.contrib.auth import get_user_model

# init user
User = get_user_model()


# get date suffice
def get_day_suffix(day):
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return suffix


# main date format
def dateformat(value):
    return f'{value.strftime("%B")} {value.strftime("%d")}, {value.strftime("%Y")}'  # noqa: E501


def intcomma(value):
    # check if number is greater than 999
    if abs(value) >= 1000:
        # divide the number by 1000 and round it to one decimal place
        formatted_num = round(value / 1000, 1)
        # check if the result is a whole number
        if formatted_num.is_integer():
            # convert formatted number to an integer if it's a whole number
            formatted_num = int(formatted_num)
        # append 'K' to the formatted number
        formatted_num = str(formatted_num) + 'K'
    else:
        # else just show only the value
        formatted_num = str(value)
    return formatted_num


def timesince(value):
    # get the current time in UTC
    current_timestamp = pendulum.now('Africa/Johannesburg')

    # time difference
    delta = current_timestamp - value
    # Convert delta to days, hours, minutes, and seconds
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    if seconds < 60 and minutes == 0 and hours == 0 and days == 0:
        return f'{seconds} sec. ago'
    elif minutes > 0 and hours == 0 and days == 0:
        return f'{minutes} min. ago'
    elif hours > 0 and days == 0:
        return f'{hours} hr. ago'
    elif days > 0:
        message = f'{days} days ago'
        if days == 1:
            message = f'{days} day ago'
        return message
    else:
        return '0 min. ago'
