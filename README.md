# PetStore API Automation
* https://petstore.swagger.io/

This project contains API automations for Petstore with find, add and delete pets APIs.
Behave bdd test framework and python is used for implementation

# Links

* [Github link to clone project](https://github.com/vishnumj005/petstore_api_automation.git)
* please note: the currently used version for python is 3.10.
* Install requirements before executing the scripts
  file before running the script.

# How to run test?

1. Via Terminal

    * Run `behave --tags=@{specific_tag}`
    * Run `behave --tags={tag1,tag2}`
    * Run `behave <path to feature file>`

2. Via PyCharm
    * Run directly from the feature file

3. Run Script with allure reporting
   * Run `behave -f allure_behave.formatter:AllureFormatter -o <path to result>`
   * Then Run `allure serve`

4. Run Script through Jenkins
   1. Create new pipeline
   2. Choose pipeline script from SCM
   3. Select github project and add URL
   4. Change branch specifier to */main
   5. Give jenkins file (jenkins/jenkins_file) in script path 
   6. Save the configuration
   7. Run the script
   * note: uncomment line number 7 from jenkins_file to run in Linux/mac machine
   
# Folder Structure

	.
	├── features
	│     ├── steps                                 # Step definitions
	│     │     ├── commons_api_steps.py
	│     │     ├── find_pets_steps.py                           
	│     │     ├── add_new_pets_steps.py
	│     │     ├── delete_pets_steps.py
	│     ├── tests
	│     │     ├── add_new_pets.feature                     	
	│     │     ├── delete_pets.feature
	│     │     ├── find_pets.feature    # Test scenarios for API
	│     ├── services                             # API services
	│     │     ├── api_commons.py
  	|     │     └── api_requests.py
	│     ├── schema                             # API response schemas
	│     │     └── schema.py
    │     ├── service_constants                    # Constants data for API
    │         ├── api_config.py
	├── requriements.txt                            # Required libraries
    ├── jenkins                                     #Jenkin related files
        ├── jenkins_file