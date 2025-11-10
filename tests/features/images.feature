Feature: Images Grid
  As a user
  I want to view product images
  So that I can see visual content

  Background:
    Given the application is running

  Scenario: Load images successfully
    Given I navigate to the images page
    When the page loads
    Then I should see 20 image cards
    And at least one image should be loaded

  Scenario: Abort image loading to speed up tests
    Given I configure route interception to abort image requests
    When I navigate to the images page
    Then I should see 20 image cards
    And no images should be loaded
    And I should see error or loading indicators
    And the test should complete faster than loading all images

  Scenario: Abort partial image set
    Given I configure route interception to abort the first 5 images
    When I navigate to the images page
    Then I should see 20 image cards
    And some images should be loaded
    And some images should show error state

