import pytest
from velocity import average_velocity

# Unit tests

# Happy paths

def test_average_velocity_happy_path():
    sprint_pts_list = [10, 20, 30] # normal expected input
    expected_average = sum(sprint_pts_list) / len(sprint_pts_list)
    assert average_velocity(sprint_pts_list) == expected_average

def test_average_velocity_happy_path_single_sprint():
    sprint_pts_list = [10] # single sprint
    assert average_velocity(sprint_pts_list) == 10

def test_average_velocity_happy_path_large_numbers():
    sprint_pts_list = [1000, 2000, 3000, 4000, 5000] # large numbers
    expected_average = sum(sprint_pts_list) / len(sprint_pts_list)
    assert average_velocity(sprint_pts_list) == expected_average

def test_average_velocity_happy_path_float_numbers():
    sprint_pts_list = [10.5, 20.7, 30.3, 40.9, 50.2] # floating point sprint values
    expected_average = sum(sprint_pts_list) / len(sprint_pts_list)
    assert average_velocity(sprint_pts_list) == expected_average

# Unhappy paths

def test_average_velocity_unhappy_path_empty_list():
    sprint_pts_list = [] # empty list input
    assert average_velocity(sprint_pts_list) == 0

def test_average_velocity_unhappy_path_zero_points():
    sprint_pts_list = [0, 0, 0, 0, 0] # all zero points
    assert average_velocity(sprint_pts_list) == 0

def test_average_velocity_unhappy_path_negative_points():
    sprint_pts_list = [-10, -20, -30, -40, -50] # negative sprint values
    with pytest.raises(ValueError):
        average_velocity(sprint_pts_list)

def test_average_velocity_unhappy_path_invalid_input():
    sprint_pts_list = [10, 20, '30', 40, 50]  # '30' is a string instead of an integer
    with pytest.raises(TypeError):
        average_velocity(sprint_pts_list)

def test_average_velocity_unhappy_path_overflow():
    sprint_pts_list = [10**1000, 10**1000, 10**1000]  # check overflow scenario
    with pytest.raises(OverflowError):
        average_velocity(sprint_pts_list)
