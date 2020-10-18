Feature: this test password reset feature of dashboard

	Scenario: attempt password reset without email address
		Given login page of dashboard
		When forget your password link is clicked
		Then click on reset password without email
		Then reset password fail message is prompted

	Scenario: attempt reset password with valid email address
		Given login page of dashboard
		When forget your password link is clicked
		Then enter valid email and click reset button
		Then open login page with email sent message

	