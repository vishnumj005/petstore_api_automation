@api_delete_pets
Feature: To test the delete existing pets API for petstore

    Scenario Outline: Testing delete existing pets API response
        When POST request is sent to add new pets with <name>
        And DELETE request is sent to delete the existing pets
        Then verify the response code 200
        And verify delete pets response data
        Examples:
        | name   |
        | doggie |