Feature: Calculate Available Effort Hours

Scenario Outline: Calculate available effort hours for a team
    Given there are <team_members> team members
    And each team member has <available_hours> available hours per day
    And each team member has <pto_hours> PTO hour per day
    And each team member commits <ceremony_hours> hours per day to sprint ceremonies
    And the sprint lasts for <sprint_days> days
    When calculating the available effort hours
    Then the total available effort hours for the team should be <total_effort_hours>

Scenario: Calculate available effort hours for a team with multiple members
    Given there are 5 team members
    And each team member has 8 available hours per day
    And each team member has 0 PTO hours per day
    And each team member commits 1 hour per day to sprint ceremonies
    And the sprint lasts for 10 days
    When calculating the available effort hours
    Then the total available effort hours for the team should be 350


