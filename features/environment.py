from selenium import webdriver

def before_scenario(context, scenario):
	context.location = "https://dashboard.pointzi.com"

	browser = webdriver.Chrome("/mnt/c/Users/Chelsea/Desktop/test/chromedriver.exe")
	browser.set_window_size(1024, 768)
	context.browser = browser

	
	
