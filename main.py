from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import schedule
import requests
from discord import Webhook, RequestsWebhookAdapter


opt = Options()
opt.add_argument('headless')


# driver = webdriver.Chrome(options=opt,service_log_path='NUL')
driver = None
URL = "https://learnapp.com/scanner/?locale=en-us"



def start_browser():
	print("Getting the 52 Week High..\n\n")
	global driver
	driver = webdriver.Chrome(options=opt,service_log_path='NUL')

	driver.get(URL)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

	if("learnapp.com" in driver.current_url):
		scrap()


def scrap():
	global driver

	webhook = Webhook.from_url(
		"https://discord.com/api/webhooks/903934234471825448/VzVDotiqT0mz8_59OhQtDaps_gtOEX374UyzzwRWNWJerZaQ42kBy40sUPWGlbxI5Tfd",
		adapter=RequestsWebhookAdapter())

	webhook.send("The STOCKS This Week are :\n\n" + driver.find_element_by_class_name("stockLists").text)
	# return driver

schedule.every().friday.at("15:01").do(start_browser)


while True:
	schedule.run_pending()
