def number_to_minutes(number):
    if(number == 1):
        return "1 Minute"
    if(number > 0 and number < 60):
        return str(number) + " minutes"
    if(number == 60):
        return "1 hour"
    if(number <= 0):
        return
    if(number > 0 and number % 60 == 0):
        return str(int(number / 60)) + " hours"
    
    hour = 0 if(int(number / 60)) < 1 else int(number/60)
    minute = int(number % 60)

    hour_plural = "hour"
    hour_plural = "hours" if hour > 1 else hour_plural
    
    minute_prural = "minute"
    minute_prural = "minutes" if minute > 1 else minute_prural

    # Remove zeros from output for zero minutes and zero hours
    hour = str(hour) if hour > 0 else ""
    minute = str(minute) if minute > 0 else ""
    
    return hour + " " + hour_plural + " " + minute + " " + minute_prural