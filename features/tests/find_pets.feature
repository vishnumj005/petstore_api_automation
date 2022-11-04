@api_find_pets
Feature: To test the find pets by status API for petstore

    Scenario Outline: Testing the find pets by status API response
        When GET request is sent to find the pets by <status>
        Then verify the response code 200
        Examples:
        | status |
        | sold   |
