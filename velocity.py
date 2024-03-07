print("\nAverage Velocity Calculator")

sprint_cnt = int(input("Enter number of sprints to consider: "))

sprint_pts_list = []

for i in range(sprint_cnt):
    pts = int(input(f"Enter the total points picked up during sprint {i}: "))
    sprint_pts_list.append(pts)

avg_velocity = sum(sprint_pts_list) / sprint_cnt

print(f"\nAverage team velocity for {sprint_cnt} sprints = {avg_velocity}\n")