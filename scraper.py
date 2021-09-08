import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape
url = "https://www.usi.edu/photography/headshot-database/"

# initiating the webdriver. Parameter includes the path of the webdriver.

driver = webdriver.Chrome('C:/Users/KULJEET/Downloads/chromedriver')
driver.get(url)

time.sleep(3)
folder_name = 'photos'
cnt = 0

print("Downloading photos...\n")
ok = False

while cnt < 864:
	time.sleep(4)
	
	html = driver.page_source

	soup = BeautifulSoup(html, 'html5lib')
	atag = soup.find_all('a', {'class' : 'web-photo'})
	
	# if(ok):
	for a in atag:
		image_link = a.get('href')

		image_link = 'https:' + image_link
		#get content of image
		r = requests.get(image_link).content

		cnt += 1
		#write the image to disk
		with open(f"{folder_name}/images{cnt}.jpg", "wb+") as f:
			f.write(r)
	
	# ok = True
	print("Current count is: ", cnt)
	print("Opening new page........\n")

	try:
		driver.find_element_by_css_selector('.current + li a').click()
		print("clicking..\n")
	except:
		print("Error occured\n")
		print("Exiting.........\n")
		exit(0)
	else:
		print("working fine\n")



print("done\n")
driver.close() # closing the webdriver
