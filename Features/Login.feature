Feature: Login

  Background:
    Given I navigate to the Login page

  Scenario: Valid credentials
    When I enter username "herb@test.com" and password "Password1"
    And I click on the Log-in button
    Then I am taken to the Post-Login Home page
    And I am successfully logged into the Dashboard page
    And I can close the browser
