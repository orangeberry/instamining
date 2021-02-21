import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


INSTAGRAM_ID = ""
INSTAGRAM_PASSWORD = ""

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.instagram.com/")

WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ"))
)

insta_id = browser.find_element_by_name("username")
insta_password = browser.find_element_by_name("password")

insta_id.send_keys(INSTAGRAM_ID)
insta_password.send_keys(INSTAGRAM_PASSWORD)

insta_password.send_keys(Keys.ENTER)

WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "qNELH"))
)

main_hashtag = "cat"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

search_bar = browser.find_element_by_class_name("XTCLo")
print(search_bar)

# search_bar.send_keys("#cat")


# search_result = browser.find_element_by_class_name("fuqBx")

# hashtags = search_result.find_element_by_class_name("uL8Hv")


# time.sleep(3)
browser.quit()
