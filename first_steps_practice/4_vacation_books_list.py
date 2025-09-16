from math import floor

total_number_of_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_needed_per_book = floor(total_number_of_pages / pages_per_hour)
hours_needed_per_day = floor(hours_needed_per_book / days_per_book)

print(hours_needed_per_day)