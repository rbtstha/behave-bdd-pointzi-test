from selenium import webdriver


@given('login page')
def open_login_page(c):
	# c.browser = webdriver.Chrome("/mnt/c/Users/Chelsea/Desktop/test/chromedriver.exe")
	c.browser.get("https://dashboard.pointzi.com/login")
	c.browser.implicitly_wait(10)

@when('correct credentials are passed')
def with_correct_credentials(c):
	try:
		form = c.browser.find_element_by_tag_name('form')
		c.browser.find_element_by_css_selector('input[name="username"]').send_keys('test-robit@test.com')
		c.browser.find_element_by_css_selector('input[name="password"]').send_keys('just1000')
		c.browser.find_element_by_xpath('//button[text()=" Login "]').click()
		assert True
	except:
		c.browser.quit()
		assert False
@then('landed to dashboard')
def verify_login(c):		
	c.browser.implicitly_wait(5)
	currentTitle = c.browser.title
	c.browser.quit()
	assert currentTitle == "Pointzi Dashboard - Setup Tutorial"


@when('incorrect credentials are passed')
def incorrect__credentials_passed(c):
	try:
		form = c.browser.find_element_by_tag_name('form')
		c.browser.find_element_by_css_selector('input[name="username"]').send_keys('test---robit@test.com')
		c.browser.find_element_by_css_selector('input[name="password"]').send_keys('just1000000')
		c.browser.find_element_by_xpath('//button[text()=" Login "]').click()
		assert True
	except:
		c.browser.quit()
		assert False

@then('user is in same change')
def same_page(c):
	c.browser.implicitly_wait(5)
	currentTitle = c.browser.title
	c.browser.quit()
	assert currentTitle == "Pointzi Dashboard - Login"



@when('clicked on login button')
def incorrect__credentials_passed(c):
	c.browser.find_element_by_xpath('//button[text()=" Login "]').click()


@then('error message in the login page')
def error_message(c):
	try:
		c.browser.implicitly_wait(5)
		c.browser.find_element_by_xpath('//button[text()=" Login "]')
		c.browser.quit()
		assert True
	except:
		c.browser.quit()
		assert False

