#Feature: OrangeHRM Login
#
#  Scenario: Login to OrangeHRM with valid parameters
#    Given launch chrome browser
#    When open orange hrm homepage
#    And Enter username "admin" and password "admin123"
#    And Click on Login button
#    Then User must successfully login to the Dashboard page
#
#  Scenario Outline: Login to OrangeHRM with valid parameters
#    Given launch chrome browser
#    When open orange hrm homepage
#    And Enter username "admin" and password "admin123"
#    And Click on Login button
#    Then User must successfully login to the Dashboard page
#
#    Examples:
#      | username  |  password |
#      | admin     |  admin123 |
#      | admin123  |  admin    |
#      | admin345  |  admin123 |
#      | admin     |  admin345 |
#
