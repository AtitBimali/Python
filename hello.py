from selenium import webdriver
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
file = open("creds.txt","r")
lines = file.readlines()

		
username = browser.find_element("id","email")
username.send_keys(lines[0])
password = browser.find_element("id","pass")
password.send_keys(lines[1])
submit   = browser.find_element("name","login")

		
		
# Step 4) Click Login
submit.click()