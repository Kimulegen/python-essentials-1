hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_min = mins + dura
total_hours = (hour + (total_min // 60)) % 24
total_mins = total_min % 60

print(f"{total_hours}:{total_mins}")