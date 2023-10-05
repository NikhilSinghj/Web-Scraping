import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode
from selenium.common.exceptions import StaleElementReferenceException
import mysql.connector


db_config ={
    "host":"localhost",
    "user":"nikhil",
    "password":"Nik212107@",
    "database":"scrape"
}

conn=mysql.connector.connect(**db_config)
cursor=conn.cursor()


citys = input("Enter the city: ")
preference = input("Enter residential preference (R for Residential and P for PG): ")

query_parameters = {
    "keyword": citys,
    "preference": preference,
    "area_unit": 1,
    "budget_min": 0,
    "res_com": "R",
    "isPreLeased": "N"
}
# https://www.99acres.com/search/property/rent/residential/mumbai?keyword=mumbai&preference=R&area_unit=1&budget_min=0&res_com=R&isPreLeased=N&page=1
base_url = "https://www.99acres.com/search/property/rent/residential/{citys}?"
encoded_query = urlencode(query_parameters)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)


page_number = 1

while True:
    try:
        url = base_url.format(citys=citys) + encoded_query + f"&page={page_number}"
        driver.get(url)
    except:
        print('wrong')

    try:
        elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-label='SEARCH']/section")))
    except StaleElementReferenceException:
        time.sleep(2)
        elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-label='SEARCH']/section")))

    for element in elements_list:
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            propertytitle = element.find_element(By.XPATH, ".//a[@id='srp_tuple_property_title']")
            propertyname = element.find_element(By.XPATH, ".//td[@id='srp_tuple_society_heading']")
            price = element.find_element(By.XPATH, ".//td[@id='srp_tuple_price']")
            area = element.find_element(By.XPATH, ".//td[@id='srp_tuple_primary_area']")
            bedroom = element.find_element(By.XPATH, ".//td[@id='srp_tuple_bedroom']")

            print(propertytitle.text)
            print(propertyname.text)
            print(price.text)
            print(area.text)
            print(bedroom.text)
            print("-" * 50)


            insert_query="INSERT INTO 99acres (property_title,property_name,price,area,bedroom) VALUES(%s,%s,%s,%s,%s)"
            data=(propertytitle.text,propertyname.text,price.text,area.text,bedroom.text)
            cursor.execute(insert_query,data)
            conn.commit()

        except StaleElementReferenceException:
            print("Element not Found")
            time.sleep(2)
            continue

   
    next_page_url = base_url.format(citys=citys) + encoded_query + f"&page={page_number + 1}"

    if next_page_url == driver.current_url:
      
        print("No more pages to scrape.")
        break

   
    user_input = input("Type 'Y' to go to the next page or any other key to exit: ")
    if user_input.lower() != 'y':
        print("Goodbye.")
        break

   
    page_number += 1


cursor.close()
conn.close()

driver.quit()
