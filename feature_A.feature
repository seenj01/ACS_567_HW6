Feature: Calculate Average Velocity

Scenario Outline: Calculate average velocity for a list of sprint points
    Given a list of sprint points: <sprint_points>
    When calculating the average velocity
    Then the result should be <expected_average_velocity>

Scenario: Calculate average velocity for a list of sprint points
    Given there are 3 sprints
    And the total points completed during sprint 0 is 10
    And the total points completed during sprint 1 is 20
    And the total points completed during sprint 2 is 30
    When calculating the average velocity
    Then the average team velocity for 3 sprints should be 20