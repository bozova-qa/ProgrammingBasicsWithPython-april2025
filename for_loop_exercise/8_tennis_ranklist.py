from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

tournament_points = 0
tournaments_winner = 0

for _ in range(1, number_of_tournaments + 1):
    tournament_level = str(input())
    if tournament_level == "W":
        tournaments_winner += 1
        tournament_points += 2000
    elif tournament_level == "F":
        tournament_points += 1200
    elif tournament_level == "SF":
        tournament_points += 720

average_points = tournament_points / number_of_tournaments
tournaments_won = (tournaments_winner / number_of_tournaments) * 100

print(f"Final points: {starting_points + tournament_points}")
print(f"Average points: {floor(average_points)}")
print(f"{tournaments_won:.2f}%")
