# Feature A Acceptance tests file

Feature: Calculate Average Velocity

Scenario: Calculate average velocity for a list of sprint points
    Given a list of sprint points
    When calculating the average velocity
    Then the result should be the sum of all points divided by the number of sprints

Scenario: Calculate average velocity for an empty list
    Given an empty list of sprint points
    When calculating the average velocity
    Then the result should be 0
