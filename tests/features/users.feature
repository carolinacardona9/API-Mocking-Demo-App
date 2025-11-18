Feature: Users Grid
  As a user
  I want to view and interact with the users grid
  So that I can see user data displayed correctly

  Background:
    Given the application is running

  Scenario: Load users successfully
    Given I navigate to the users page
    When the page loads
    Then I should see users in the grid

  Scenario: Display users with no records
    Given I mock the API to return no users
    And the application is running
    And I navigate to the users page
    When the page loads
    Then I should see the message "No Rows To Show"

  Scenario: Display users with status colors
    Given I mock the API to return users with different statuses
    And the application is running
    And I navigate to the users page
    When the page loads
    Then I should see users with correct status colors

