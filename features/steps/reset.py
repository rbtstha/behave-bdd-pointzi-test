@given('login page of dashboard')
def step_impl(c):
    c.browser.get('https://dashboard.pointzi.com/login')

@when('forget your password link is clicked')
def step_impl(c):
    c.browser.implicitly_wait(50)
    try:
        reset_link = c.browser.find_element_by_xpath('//*[@id="loginFm"]/div[4]/a')
        reset_link.click()
        assert True
    except:
        c.browser.quit()
        assert False

@then('click on reset password without email')
def step_impl(c):
    try:
        c.browser.implicitly_wait(20)
        # c.browser.find_element_by_name('email')
        # form button[type="submit"] css bata form vanne tag vitra ko button vanne element 
        # jo sanga type='submit' vanne attribute chha teslai find garne
        c.browser.find_element_by_css_selector('button[type="submit"]').click()
        assert True
    except:
        c.browser.quit()
        assert False

@then('reset password fail message is prompted')
def step_impl(c):
    try:
        c.browser.implicitly_wait(5)
        c.browser.find_element_by_xpath('//span[text()="      Reset password failed by unknown issue. Please contact for support.    "]')
        c.browser.quit()
        assert True
    except:
        c.browser.quit()
        assert False



@then('enter valid email and click reset button')
def step_impl(c):
    c.browser.implicitly_wait(5)
    try:
        c.browser.find_element_by_css_selector('input[name="email"]').send_keys('robitstha90@gmail.com')
        c.browser.find_element_by_xpath('//button[text()=" Reset Password "]').click()
        assert True
    except:
        c.browser.quit()
        assert False
@then('open login page with email sent message')
def step_impl(c):
    c.browser.implicitly_wait(5)
    try:
        c.browser.find_element_by_xpath('//button[text()=" Login "]')
        c.browser.quit()
        assert  True
    except:
        c.browser.quit()
        assert False



