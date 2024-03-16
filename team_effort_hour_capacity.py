def calculate_available_effort_hours(teammate_cnt, available_hrs, pto_hours, sprint_ceremony_hrs, sprint_days):
    if sprint_days == 0 or teammate_cnt == 0:
        return 0

    if available_hrs < 0 or pto_hours < 0 or sprint_ceremony_hrs < 0 or sprint_days < 0 or teammate_cnt < 0:
        raise ValueError("Input values cannot be negative")

    if available_hrs > (1 << 32) or pto_hours > (1 << 32) or sprint_ceremony_hrs > (1 << 32) or sprint_days > (1 << 32) or teammate_cnt > (1 << 32):
        raise OverflowError("Input values are too large")

    return (available_hrs - pto_hours - sprint_ceremony_hrs) * sprint_days * teammate_cnt



if __name__ == "__main__":
    sprint_days = int(input("Enter number of sprint days: "))
    teammate_cnt = int(input("Enter number of team members: "))

    team_available_effort_hrs = 0

    for i in range(teammate_cnt):
        print(f"\nEnter details for team member {i+1}")
        available_hrs = int(input("Enter number of available hours per day: "))
        pto_hours = int(input("Enter number of PTO hours per day: "))
        sprint_ceremony_hrs = int(input("Enter number of hours per day committed to sprint ceremonies: "))

        available_effort_hrs = calculate_available_effort_hours(teammate_cnt, available_hrs, pto_hours, sprint_ceremony_hrs, sprint_days)

        team_available_effort_hrs += available_effort_hrs

        print(f"Available Effort-Hours for team member {i+1} for sprint with {sprint_days} days = {available_effort_hrs}")

    print(f"\nAvailable Effort-Hours for entire team for sprint with {sprint_days} days = {team_available_effort_hrs}")
