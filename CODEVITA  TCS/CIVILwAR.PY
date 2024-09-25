powers = list(map(int, input().split()))

team_a_power = 0
team_b_power = 0
# power_difference=0
# Sort the powers by absolute value (descending) and by value (ascending) for ties
powers.sort(key=lambda x: (abs(x), -x), reverse=True)

# Alternate assignment of powers to teams
for i, power in enumerate(powers):
	if i % 2 == 0:  # Team A's turn
		team_a_power += power
	else:           # Team B's turn
		team_b_power += power
			# Calculate and print the absolute power difference
power_difference = abs(team_a_power - team_b_power)
print(power_difference)

