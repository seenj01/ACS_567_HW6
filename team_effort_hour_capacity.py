def calculate_available_effort_hours(available_hrs, pto_hours, sprint_ceremony_hrs, sprint_days):
    return (available_hrs - pto_hours - sprint_ceremony_hrs) * sprint_days

sprint_days = int(input("Enter number of sprint days: "))
teammate_cnt = int(input("Enter number of team members: "))

team_available_effort_hrs = 0

for i in range(teammate_cnt):
    print(f"\nEnter details for team member {i+1}")
    available_hrs = int(input("Enter number of available hours per day: "))
    pto_hours = int(input("Enter number of PTO hours per day: "))
    sprint_ceremony_hrs = int(input("Enter number of hours per day committed to sprint ceremonies: "))

    available_effort_hrs = calculate_available_effort_hours(available_hrs, pto_hours, sprint_ceremony_hrs, sprint_days)

    team_available_effort_hrs += available_effort_hrs

    print(f"Available Effort-Hours for team member {i+1} for sprint with {sprint_days} days = {available_effort_hrs}")

print(f"\nAvailable Effort-Hours for entire team for sprint with {sprint_days} days = {team_available_effort_hrs}")


