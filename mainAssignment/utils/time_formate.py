def str_val(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)


def min_to_hour_min(length):
    hours = int(length / 60)
    mins = length - hours * 60

    return str_val(hours) + " hours " + str_val(mins) + " mins"
