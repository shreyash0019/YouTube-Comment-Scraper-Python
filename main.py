from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Initialize WebDriver
driver = webdriver.Chrome(r"C:/Users/hp/Anaconda3/chromedriver.exe")

# Open the YouTube video
video_url = 'https://www.youtube.com/watch?v=iFPMz36std4'
driver.get(video_url)

# Scroll to load comments
driver.execute_script('window.scrollTo(1, 500);')
time.sleep(5)
driver.execute_script('window.scrollTo(1, 3000);')
time.sleep(5)  # wait more to load additional comments

# Extract usernames and comments
username_elems = driver.find_elements(By.XPATH, '//*[@id="author-text"]')
comment_elems = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Collect data
items = []
for username, comment in zip(username_elems, comment_elems):
    item = {
        'Author': username.text.strip(),
        'Comment': comment.text.strip()
    }
    items.append(item)

# Save to CSV
filename = 'C:/Users/hp/Desktop/commentlist.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Author', 'Comment'])
    writer.writeheader()
    for item in items:
        writer.writerow(item)

# Close browser
driver.quit()
