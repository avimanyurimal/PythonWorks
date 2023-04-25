def add_daily_temp(temps_dict, temp, day):
    if day not in temps_dict:
        temps_dict[day] = temp
    return temps_dict
daily_temps = {}
daily_temps = add_daily_temp(daily_temps, 25, "Monday")
daily_temps = add_daily_temp(daily_temps, 30, "Tuesday")
daily_temps = add_daily_temp(daily_temps, 27, "Monday") # This won't add a new temperature for "Monday"
print(daily_temps)
