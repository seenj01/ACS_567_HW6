def calculate_average_velocity(sprint_pts_list):
    if any(pt < 0 for pt in sprint_pts_list):
        raise ValueError("Sprint points cannot be negative")
    if not sprint_pts_list:
        return 0
    return sum(sprint_pts_list) / len(sprint_pts_list)


if __name__ == "__main__":
    sprint_cnt = int(input("Enter number of sprints to consider: "))

    sprint_pts_list = []

    for i in range(sprint_cnt):
        pts = int(input(f"Enter the total points completed during sprint {i}: "))
        sprint_pts_list.append(pts)

    avg_velocity = calculate_average_velocity(sprint_pts_list)

    print(f"\nAverage team velocity for {sprint_cnt} sprints = {avg_velocity}\n")
