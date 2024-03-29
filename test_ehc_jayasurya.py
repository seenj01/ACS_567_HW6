import pytest
from team_effort_hour_capacity import available_effort_hours

# Unit tests

# Happy paths

def test_available_effort_hours_happy_path_single_member():
    assert available_effort_hours(1, 8, 0, 1, 10) == 70  # Example values 1 team member

def test_available_effort_hours_happy_path_multiple_members():
    assert available_effort_hours(5, 8, 0, 1, 10) == 350  # 5 team members, each with 70 hours

def test_available_effort_hours_happy_path_long_sprint():
    assert available_effort_hours(5, 8, 0, 1, 20) == 700  # 20 days sprint

def test_available_effort_hours_happy_path_large_team():
    assert available_effort_hours(24, 10, 1, 3, 14) == 2016 # large team size and 2 week sprint

# Unhappy paths

def test_available_effort_hours_unhappy_path_negative_hours_values():
    with pytest.raises(ValueError):
        available_effort_hours(5, -8, -1, -1, 10) # negative hours values

def test_available_effort_hours_unhappy_path_negative_hours_values():
    with pytest.raises(ValueError):
        available_effort_hours(5, 8, 1, 1, -10) # negative sprint days value

def test_available_effort_hours_unhappy_path_zero_sprint_days():
    assert available_effort_hours(5, 8, 0, 1, 0) == 0  # No sprint days, result should be 0

def test_available_effort_hours_unhappy_path_zero_team_members():
    assert available_effort_hours(0, 8, 0, 1, 10) == 0  # No team members, result should be 0

def test_available_effort_hours_unhappy_path_invalid_input():
    with pytest.raises(TypeError):
        available_effort_hours(5, "8", "0", "1", "10")  # Invalid input types

def test_available_effort_hours_unhappy_path_negative_remaining_hours():
    with pytest.raises(ValueError):
        available_effort_hours(5, 8, 10, 20, 5)  # negative remaining hours


def test_available_effort_hours_unhappy_path_overflow():
    with pytest.raises(OverflowError):
        available_effort_hours(24, 999999999999999999999999999999999999999, 1, 3, 14)  # very large values for team members and sprint days
