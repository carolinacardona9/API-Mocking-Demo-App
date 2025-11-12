Feature: Users Grid
  As a user
  I want to view and interact with the users grid
  So that I can see user data displayed correctly

  Background:
    Given the application is running
    And I navigate to the users page

  Scenario: Users grid is visible and loads data
    When the page loads
    Then users grid is visible and show records

  Scenario: Display users with no records
    Given I mock the API to return no users
    When the page loads
    Then I should see the message "No Rows To Show"

  Scenario: Display users with status colors
    Given I mock the API to return users with different statuses
    When the page loads
    Then I should see users with correct status colors
      | Status   | Color              |
      | Pending  | rgb(255, 165, 0) |
      | Inactive | rgb(255, 0, 0)   |
      | Active   | rgb(0, 128, 0)   |

