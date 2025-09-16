holidays_number = int(input())

playtime_year = 30000
playtime_holidays_per_year = 127
playtime_per_working_day_year = 63
working_days = 365 - holidays_number
total_norm = working_days * playtime_per_working_day_year + holidays_number * playtime_holidays_per_year
total_norm_hours = (total_norm - playtime_year) // 60
total_norm_minutes = (total_norm - playtime_year) % 60

if total_norm > playtime_year:
    print("Tom will run away")
    print(f"{total_norm_hours} hours and {total_norm_minutes} minutes more for play")
elif total_norm < playtime_year:
    print("Tom sleeps well")
    print(f"{(playtime_year - total_norm) // 60} hours and {(playtime_year - total_norm) % 60} minutes less for play")