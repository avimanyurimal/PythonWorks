def get_weekend_average_temp(weekly_temperatures):
    """
    Calculates the average temperature over the weekend (Saturday and Sunday) for the
    weekly temperatures given as a dictionary of daily temperatures.
    """
    weekend_temps = []
    for day, temp in weekly_temperatures.items():
        if day.lower() in ['saturday', 'sunday']:
            weekend_temps.append(temp)
    if len(weekend_temps) > 0:
        return sum(weekend_temps) / len(weekend_temps)
    else:
        return None
weekly_temperatures = {
    'Monday': 23,
    'Tuesday': 24,
    'Wednesday': 21,
    'Thursday': 25,
    'Friday': 27,
    'Saturday': 26,
    'Sunday': 28
}
weekend_average_temp = get_weekend_average_temp(weekly_temperatures)
print(weekend_average_temp)
