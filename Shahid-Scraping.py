from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openpyxl import Workbook

# Open Driver/Browser and navigate to Google

driver = webdriver.Chrome()
driver.get("http://www.google.com")

wait = WebDriverWait(driver, 10)

# amazon Search

elem = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
elem.send_keys("Amazon")
elem.send_keys(Keys.RETURN)

time.sleep(20)

# Click on Amazon link

elem = driver.find_element(By.PARTIAL_LINK_TEXT,"Amazon")
elem.click()

time.sleep(15)

#Books search

elem = driver.find_element(By.ID,"twotabsearchtextbox")
elem.send_keys("Books")
elem.send_keys(Keys.RETURN)
time.sleep(8)


wb = Workbook()
ws = wb.active
ws.title = "Books Title with Prices"

# Header
ws.append(["Book Name", "Price"])


prices = driver.find_elements(By.CSS_SELECTOR,".a-price-whole")

books = driver.find_elements(By.CSS_SELECTOR,"h2 span")

print("Books:", len(books))
print("Prices:", len(prices))

for i in range(min(len(books), len(prices))):
    driver.execute_script("arguments[0].scrollIntoView();", books[i])
    print(f"Product Name: {books[i].text} | Product price: ₹{prices[i].text}")
    ws.append([books[i].text, prices[i].text])

wb.save("books with prices.xlsx")

print("\n✅ Data saved to Books Title with Prices.xlsx")

input("Press Enter to continue...") 
driver.quit()