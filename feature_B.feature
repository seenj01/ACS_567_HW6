Feature: Calculate Available Effort Hours

Scenario: Calculate available effort hours for a team
    Given there are <team_members> team members
    And each team member has <available_hours> available hours per day
    And each team member has <pto_hours> PTO hour per day
    And each team member commits <ceremony_hours> hours per day to sprint ceremonies
    And the sprint lasts for <sprint_days> days
    When calculating the available effort hours
    Then the total available effort hours for the team should be <total_effort_hours>

Examples:
    | team_members | available_hours | pto_hours | ceremony_hours | sprint_days | total_effort_hours |
    | 5            | 8               | 1         | 3              | 14          | 1750               |
    | 10           | 7               | 2         | 2              | 10          | 540                |
    | 8            | 6               | 0         | 1              | 20          | 880                |

