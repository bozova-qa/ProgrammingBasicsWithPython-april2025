from math import ceil

show_name = str(input())
show_duration = int(input())
lunch_break = int(input())

lunch_time = (1 / 8) * lunch_break
rest_time = (1 / 4) * lunch_break
movie_time = lunch_break - lunch_time - rest_time

if movie_time >= show_duration:
    print(f"You have enough time to watch {show_name} and left with {ceil(movie_time - show_duration)} "
          f"minutes free time.")

elif movie_time < show_duration:
    print(f"You don't have enough time to watch {show_name}, "
          f"you need {ceil(abs(movie_time - show_duration))} more minutes.")
