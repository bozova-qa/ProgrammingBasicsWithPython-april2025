deposit_amount = float(input())
deposit_duration = int(input())
annual_interest_rate = float(input())

annual_rate = deposit_amount * (annual_interest_rate / 100)
monthly_interest_rate = annual_rate / 12
deposit_amount_at_period_end = deposit_amount + deposit_duration * monthly_interest_rate

print(deposit_amount_at_period_end)