Feature: Calculate Average Velocity

Scenario Outline: Calculate average velocity for a list of sprint points
    Given a list of sprint points: <sprint_points>
    When calculating the average velocity
    Then the result should be <expected_average_velocity>

Examples:
    sprint_points                      expected_average_velocity 
    [10, 20, 30, 40, 50]               30                        
    [10]                               10                        
    [1000, 2000, 3000, 4000, 5000]     3000                  
    [10.5, 20.7, 30.3, 40.9, 50.2]     30.12                
    []                                 0                         
    [0, 0, 0, 0, 0]                    0                         
    [-10, -20, -30, -40, -50]          ValueError                
    [10, 20, '30', 40, 50]             TypeError                 
    [10**1000, 10**1000, 10**1000]     OverflowError       