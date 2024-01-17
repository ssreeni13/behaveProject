Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on Login


  Scenario: Login to OrangeHRM Application
    Then User must login to the Dashboard page

  Scenario: Search User
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search user
    When navigate to advanced search page
    Then advanced search page should display


