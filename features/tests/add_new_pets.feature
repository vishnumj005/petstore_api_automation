@api_add_new_pets
Feature: To test the add new pets to the store API for petstore

    Scenario Outline: Testing add new pets to the store API response
        When POST request is sent to add new pets with <name>
        Then verify the response code 200
        And verify response data
        Examples:
        | name   |
        | doggie |

    Scenario Outline: Testing add new pets to the store API with different group name
        When POST request is sent to add new pets with <name>
        Then verify the response code <status_code>
        Then verify response data
        Examples:
        | name       | status_code |
        | 123        | 200         |
        | r%$E$%#$%# | 200         |