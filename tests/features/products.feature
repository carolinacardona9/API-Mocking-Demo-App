Feature: Products Grid
  As a user
  I want to view and interact with the products grid
  So that I can see product data with stock indicators

  Background:
    Given the application is running
    And I navigate to the products page

  Scenario: Display products with stock color indicators
    Given I mock the API to return products with different stock levels
    When the page loads
    Then I should see products with correct stock background colors
      | Stock Range | Color               |
      | 0-9         | rgb(255, 235, 238)|
      | 10-49       | rgb(255, 243, 224)|
      | 50+         | rgb(232, 245, 233)|

  Scenario: Display loading indicator during API delay
    Given I mock the API to have a delay of 10 seconds
    When I navigate to the products page
    Then I should see a loading spinner
    And the grid should eventually load

