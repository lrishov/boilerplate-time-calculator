def add_time(start, duration, weekday = None):
    start, phase = start.split()
    start = start.split(":")
    duration = duration.split(":")
    start = [int(x) for x in start]
    duration = [int(x) for x in duration]
    hours , minutes = divmod((start[1] + duration[1]), 60)
    days, hours = divmod((hours + start[0] + duration[0]), 24)
    if hours >= 12:
        if hours == 24:
            days = days + 1       
        elif phase == 'PM':
            phase = 'AM'
            days = days + 1
        else: phase = 'PM'
        if hours != 12:
            hours = hours - 12
    if minutes < 10:
        minutes = '0' + str(minutes)
    else: minutes = str(minutes)
    new_time = str(hours) + ":" + minutes + " " + phase
    if weekday != None:
        semana = {'Monday':0, 'Tuesday':1 , 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
        weekday = weekday.lower().capitalize()
        weekday = list(semana.keys())[(semana[weekday] + days) % 7]
        new_time = new_time + ", " + weekday
    if days == 1:
        new_time = new_time + " (next day)"
    elif days > 1:
        new_time = new_time + " (" + str(days) + " days later)"           
    return new_time
