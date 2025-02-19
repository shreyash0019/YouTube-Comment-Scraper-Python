import csv
import time
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome(r"C:/Users/hp/Anaconda3/chromedriver.exe")

# Open YouTube video
driver.get('https://www.youtube.com/watch?v=iFPMz36std4')

# Scroll to load comments
driver.execute_script('window.scrollTo(1, 500);')
time.sleep(5)
driver.execute_script('window.scrollTo(1, 3000);')

# Find and extract comments
username_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')

# Collect data
items = []
for username, comment in zip(username_elems, comment_elems):
    item = {
        'Author': username.text,
        'Comment': comment.text
    }
    items.append(item)

# Write data to CSV file
filename = 'C:/Users/hp/Desktop/commentlist.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['Author', 'Comment'])
    w.writeheader()
    for item in items:
        w.writerow(item)

# Close the WebDriver
driver.quit()
