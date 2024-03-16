Feature: Calculate Available Effort Hours

Scenario Outline: Calculate available effort hours for a team
    Given there are <team_members> team members
    And each team member has <available_hours> available hours per day
    And each team member has <pto_hours> PTO hour per day
    And each team member commits <ceremony_hours> hours per day to sprint ceremonies
    And the sprint lasts for <sprint_days> days
    When calculating the available effort hours
    Then the total available effort hours for the team should be <total_effort_hours>

Examples:
     team_members  available_hours  pto_hours  ceremony_hours  sprint_days  total_effort_hours 
     1             8                0          1               10           70                 
     5             8                0          1               10           350                
     5             8                0          1               20           700                
     24            10               1          3               14           2016               
     5             -8               -1         -1              10           ValueError         
     5             8                1          1               -10          ValueError         
     5             8                0          1               0            0                  
     0             8                0          1               10           0                  
     5             8                0          1               5            ValueError         
     24            999999999999999999999999999999999999999  1  3  14        OverflowError      

