
def str_val(val):
    if val < 10:
        return "0" + str(val)
    else:
        return str(val)

def min_to_hour_min(minutes):
    hours = minutes / 60
    mins = minutes - hours * 60

    return str_val(hours) + " hours " + str_val(mins) + " mins"