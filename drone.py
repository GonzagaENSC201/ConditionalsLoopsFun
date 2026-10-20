battery = 90
for altitude in range(200, 510, 10):
    battery -= 3
    print("Altitude:", altitude, "meters - Battery:", battery, "%")

