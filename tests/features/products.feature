Feature: Products Grid
  As a user
  I want to view and interact with the products grid
  So that I can see product data with stock indicators

  Background:
    Given the application is running

  Scenario: Load products successfully
    Given I navigate to the products page
    When the page loads
    Then I should see products in the grid

  Scenario: Display products with stock color indicators
    Given I mock the API to return products with different stock levels
    And I navigate to the products page
    When the page loads
    Then I should see products with correct stock background colors

  Scenario: Display loading indicator during API delay 2
    Given I mock the API to have a delay of 10 seconds
    When I navigate to the products page
    Then I should see a loading spinner
