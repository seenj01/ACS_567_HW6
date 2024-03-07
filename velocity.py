def calculate_average_velocity(sprint_pts_list):
    return sum(sprint_pts_list) / len(sprint_pts_list)

print("\nAverage Velocity Calculator")

sprint_cnt = int(input("Enter number of sprints to consider: "))

sprint_pts_list = []

for i in range(sprint_cnt):
    pts = int(input(f"Enter the total points completed during sprint {i}: "))
    sprint_pts_list.append(pts)

avg_velocity = calculate_average_velocity(sprint_pts_list)

print(f"\nAverage team velocity for {sprint_cnt} sprints = {avg_velocity}\n")