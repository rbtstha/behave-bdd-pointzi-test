Feature: this test the login feature of dashboard
	
	Scenario: attempt login with correct credentials
		Given login page
		When correct credentials are passed
		Then landed to dashboard

	Scenario: attempt login with incorrect credentials
		Given login page
		When incorrect credentials are passed
		Then user is in same change

	Scenario: attempt login without credentials
		Given login page
		When clicked on login button
		Then error message in the login page
