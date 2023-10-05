# driver.get("https://www.99acres.com/search/property/rent/delhi-ncr?city=1&preference=R&area_unit=1&budget_min=0&res_com=R&isPreLeased=N")

# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from urllib.parse import urlencode
  




# citys = input("Enter the city: ")
# preference = input("Enter residential preference (R for Residential and S for Buy and P for PG): ")

# query_parameters = {
#     "city": citys,
#     "preference": preference,
#     "area_unit": 1,
#     "budget_min": 0,
#     "res_com": "R",
#     "isPreLeased": "N"
# }

# base_url = "https://www.99acres.com/search/property/rent/{citys}?"
# encoded_query = urlencode(query_parameters)

# url = base_url + encoded_query




# driver = webdriver.Chrome()
# wait = WebDriverWait(driver,10)
# driver.get(url)



# elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@data-label='SEARCH']/section")))

# for element in elements_list:
#     driver.execute_script("arguments[0].scrollIntoView(true);",element)
#     propertytitle=element.find_element(By.XPATH,".//a[@id='srp_tuple_property_title']")
#     propertyname= element.find_element(By.XPATH,".//td[@id='srp_tuple_society_heading']")
#     price = element.find_element(By.XPATH,".//td[@id='srp_tuple_price']")
#     area= element.find_element(By.XPATH,".//td[@id='srp_tuple_primary_area']")
#     bedroom= element.find_element(By.XPATH,".//td[@id='srp_tuple_bedroom']")
#     # address = element.find_element(By.XPATH,".//div[@id='srp_tuple_description']/div")
#     print(propertytitle.text)
#     print(propertyname.text)
#     print(price.text)
#     print(area.text)
#     print(bedroom.text)
#     # print(address.text)
#     print("-"*50)
#     next_button=driver.find_element(By.XPATH,'.//a[@class="list_header_bold"]')




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# city = input("Enter the city: ")
# area = input("Enter the area: ")


# url = f"https://housing.com/in/buy/{city}/{area}"


# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)


# driver.get(url)

# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     driver.implicitly_wait(3)  


# elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="innerApp"]/div[2]/div[2]/div[1]')))


# # elements_list = driver.find_elements((By.XPATH, '//*[@id="innerApp"]/div[2]/div[2]/div[1]'))
# print(elements_list)
# # elem=[]

# for element in elements_list:
#     # driver.execute_script("arguments[0].scrollIntoView(true);", element)
#     # price = element.find_element(By.XPATH, '//*[@id="srp-0"]/div[1]/div[2]/div[1]')
#     price = wait.until(EC.visibility_of_all_element_located((By.XPATH, '//*[@id="srp-0"]/div[1]/div[2]/div[1]')))
#     print(price.text)


# driver.quit()

# //*[@id="innerApp"]/div[2]/div[2]/div[1]       main body
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[1]/div[1]/div   cost
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[1]/div[1]/span   emi
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[2]/a/h2/div      bhk
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[3]/section/div[1]/div[1]/div[2]/div[2]    buildup area 
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[3]/section/div[1]/div[2]/div[2]/div[2]    average price
# //*[@id="srp-0"]/div[1]/div[2]/div[1]/div[3]/section/div[1]/div[3]/div[2]/div[2]    facing
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# city = input("Enter the city: ")
# area = input("Enter the area: ")


# url = f"https://housing.com/in/buy/{city}/{area}"


# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)


# driver.get(url)


# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     driver.implicitly_wait(3)  


# price_elements = driver.find_elements(By.XPATH, '//div[@class="_sq1l2s _vv1q9c _ks15vq _vy1ipv _7ltvct _g3dlk8 _c81fwx _cs1nn1 value"]')

# for price_element in price_elements:
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     print(price_element.text)


# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# city = input("Enter the city: ")
# area = input("Enter the area: ")

# url = f"https://housing.com/in/buy/{city}/{area}"

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

# driver.get(url)


# elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="innerApp"]/div[2]/div[2]/div[1]')))

# for element in elements_list:
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     cost = element.find_element(By.XPATH, './/div[1]/div[2]/div[1]/div[1]/div[1]/div').text
#     emi = element.find_element(By.XPATH, './/div[1]/div[2]/div[1]/div[1]/div[1]/span').text
#     bhk = element.find_element(By.XPATH, './/div[2]/a/h2/div').text
#     buildup_area = element.find_element(By.XPATH, './/div[3]/section/div[1]/div[1]/div[2]/div[2]').text
#     average_price = element.find_element(By.XPATH, './/div[3]/section/div[1]/div[2]/div[2]/div[2]').text
#     facing = element.find_element(By.XPATH, './/div[3]/section/div[1]/div[3]/div[2]/div[2]').text

#     print("Cost:", cost)
#     print("EMI:", emi)
#     print("BHK:", bhk)
#     print("Buildup Area:", buildup_area)
#     print("Average Price:", average_price)
#     print("Facing:", facing)
#     print("-" * 50)

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# city = input("Enter the city: ")
# area = input("Enter the area: ")

# url = f"https://housing.com/in/buy/{city}/{area}"

# driver = webdriver.Chrome()
# driver.get(url)
# # <div class="_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh">₹60.0 L</div>

# elements_list = driver.find_elements(By.CSS_SELECTOR, 'list-card-item')

# for element in elements_list:
#     cost = (element.find_element(By.CSS_SELECTOR, 'price-with-unit').text).strip()
#     # emi = element.find_element(By.CSS_SELECTOR, '.emi-class').text
#     # bhk = element.find_element(By.CSS_SELECTOR, '.bhk-class').text
#     # buildup_area = element.find_element(By.CSS_SELECTOR, '.buildup-area-class').text
#     # average_price = element.find_element(By.CSS_SELECTOR, '.average-price-class').text
#     # facing = element.find_element(By.CSS_SELECTOR, '.facing-class').text

#     print("Cost:", cost)
#     # print("EMI:", emi)
#     # print("BHK:", bhk)
#     # print("Buildup Area:", buildup_area)
#     # print("Average Price:", average_price)
#     # print("Facing:", facing)
#     print("-" * 50)

# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize a web driver (you need to specify the path to your driver executable)
# driver = webdriver.Chrome()

# # Open the website URL for the specific city and area
# city = "New Delhi"
# area = "Nawada"
# url = f"https://housing.com/in/buy/{city}/{area}" # Replace with the actual URL
# driver.get(url)

# # Find and extract data for all property listings across all pages
# try:
#     while True:
#         property_elements = driver.find_elements(By.CLASS_NAME, "css-1cb65ej")  # Class name for property listings

#         for property_element in property_elements:
#             # Extract data for each property listing
#             title_element = property_element.find_element(By.CLASS_NAME, "_sq1l2s")
#             property_title = title_element.text

#             price_element = property_element.find_element(By.CLASS_NAME, "_gqyh40")
#             property_price = price_element.text

#             # Print or store the property data as needed
#             print("Property Title:", property_title)
#             print("Property Price:", property_price)
#             print("\n")

#         # Check if there's a next page button and click it
#         next_page_button = driver.find_element(By.XPATH, "//button[text()='Next']")
#         if next_page_button.is_enabled():
#             next_page_button.click()
#             WebDriverWait(driver, 10).until(EC.staleness_of(property_elements[0]))  # Wait for new listings to load
#         else:
#             break  # No more pages to navigate

# except Exception as e:
#     print("An error occurred:", str(e))

# # Close the web driver
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.get('https://housing.com/in/buy/search?f=eyJ2IjoyLCJiYXNlIjpbeyJ0eXBlIjoiUE9MWSIsInV1aWQiOiJiOTcyZjYwZGIyNGFhOWVjZDAxMyIsImxhYmVsIjoiRm9ydCJ9LHsidHlwZSI6IlBPTFkiLCJ1dWlkIjoiNDMwM2U4ZTM1Yjk2OWI4MjhhYjciLCJsYWJlbCI6IkNvbGFiYSJ9LHsidHlwZSI6IlBPTFkiLCJ1dWlkIjoiZDAzZWJmNjZiYWRhNGZiZDY3NWEiLCJsYWJlbCI6IkJhbmRyYSBXZXN0In1dLCJzIjoiZCIsInRpbWVTdGFtcCI6MTUyMDI4NjEzNjA5NCwidXNlckNpdHkiOiJhMGZkMzI4MTZmNzM5NjE3NDhjZiJ9')

# iter = 1

# lastHeight = driver.execute_script("return document.body.scrollHeight")
# while True:
#     print(r"Page is Scrolling Down ...Wait({})".format(iter))
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(2)
#     iter += 1

#     newHeight = driver.execute_script("return document.body.scrollHeight")
#     if newHeight == lastHeight:
#         break
#     lastHeight = newHeight

# print(r"Scroll Down Completed ....")
# print('-----------------------------------------------------------')
# print()


# propertyName = []
# propertyAddedOn = []
# propertyPrice = []
# propertyAreaPerFeet = []
# propertyAddress = []
# propertyMoreInfo = []
# propertyEMIAvailability = []

# elements = driver.find_elements(By.CLASS_NAME, "list-card-item")
# print('The Count of Element is ', len(elements))
# for element in elements:
#     element.location_once_scrolled_into_view
#     actionitem = ActionChains(driver).move_to_element(element)
#     time.sleep(2)
#     actionitem.click()
#     actionitem.perform()

#     try:
        
#         time.sleep(2)

       
#         try:
#             property_name = driver.find_element(By.CSS_SELECTOR, '.text').text
#         except:
#             property_name = "No Property Name"

       
#         try:
#             added_on = driver.find_element(By.CSS_SELECTOR, '.added-on').text
#         except:
#             added_on = "No Added On Information"

       
#         try:
#             price = driver.find_element(By.CSS_SELECTOR, '.price-with-unit').text.strip()
#         except:
#             price = "No Price Given"

       
#         try:
#             area_per_sqft = driver.find_element(By.CSS_SELECTOR, '.formatted-price').text
#         except:
#             area_per_sqft = "No Per Square Feet"

        
#         try:
#             address = driver.find_element(By.CSS_SELECTOR, '.landmark span:first-child').text
#         except:
#             address = "No Address Provided"

        
#         try:
#             more_info_elements = driver.find_elements(By.CSS_SELECTOR, '.overview-point')
#             more_info = ",".join([el.text for el in more_info_elements])
#         except:
#             more_info = "RERA Registered"

        
#         try:
#             emi_availability = driver.find_element(By.CSS_SELECTOR, '.emi-txt').text
#             if len(emi_availability) == 0:
#                 emi_availability = "No-EMI-Option"
#         except:
#             emi_availability = "No-EMI-Option"

    
#         propertyName.append(property_name)
#         propertyAddedOn.append(added_on)
#         propertyPrice.append(price)
#         propertyAreaPerFeet.append(area_per_sqft)
#         propertyAddress.append(address)
#         propertyMoreInfo.append(more_info)
#         propertyEMIAvailability.append(emi_availability)

#     except Exception as e:
#         print("Error:", e)

# driver.quit()
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from urllib.parse import urlencode

# citys = input("Enter the city: ")
# preference = input("Enter residential preference (R for Residential and S for Buy and P for PG): ")

# query_parameters = {
#     "city": citys,
#     "preference": preference,
#     "area_unit": 1,
#     "budget_min": 0,
#     "res_com": "R",
#     "isPreLeased": "N"
# }

# base_url = "https://www.99acres.com/search/property/rent/{citys}?"
# encoded_query = urlencode(query_parameters)

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

# # Initialize page number
# page_number = 1

# while True:
#     url = base_url.format(citys=citys) + encoded_query + f"&page={page_number}"
#     driver.get(url)

#     elements_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-label='SEARCH']/section")))

#     for element in elements_list:
#         driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         propertytitle = element.find_element(By.XPATH, ".//a[@id='srp_tuple_property_title']")
#         propertyname = element.find_element(By.XPATH, ".//td[@id='srp_tuple_society_heading']")
#         price = element.find_element(By.XPATH, ".//td[@id='srp_tuple_price']")
#         area = element.find_element(By.XPATH, ".//td[@id='srp_tuple_primary_area']")
#         bedroom = element.find_element(By.XPATH, ".//td[@id='srp_tuple_bedroom']")

#         print(propertytitle.text)
#         print(propertyname.text)
#         print(price.text)
#         print(area.text)
#         print(bedroom.text)
#         print("-" * 50)

#     # Check if the "Next" page exists by constructing the URL for the next page
#     next_page_url = base_url.format(citys=citys) + encoded_query + f"&page={page_number + 1}"

#     if next_page_url == driver.current_url:
#         # Exit the loop if the next page URL is different (no more pages)
#         break

#     # Increment the page number for the next iteration
#     page_number += 1

# driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode
from selenium.common.exceptions import StaleElementReferenceException
import mysql.connector


# db_config ={
#     "host":"localhost",
#     "user":"nikhil",
#     "password":"Nik212107@",
#     "database":"scrape"
# }

# conn=mysql.connector.connect(**db_config)
# cursor=conn.cursor()


citys = input("Enter the city: ")
preference = input("Enter residential preference (R for Residential and S for Buy and P for PG): ")

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


            # insert_query="INSERT INTO 99acres (property_title,property_name,price,area,bedroom) VALUES(%s,%s,%s,%s,%s)"
            # data=(propertytitle.text,propertyname.text,price.text,area.text,bedroom.text)
            # cursor.execute(insert_query,data)
            # conn.commit()

        except StaleElementReferenceException:
           
            time.sleep(2)
            continue

   
    # next_page_url = base_url.format(citys=citys) + encoded_query + f"&page={page_number + 1}"

    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'pagination__next')]")
    except :
            # Exit the loop if the "Next" button is not found (no more pages)
        print("No more pages to scrape.")
        break

        # Ask the user if they want to go to the next page
    user_input = input("Type 'Y' to go to the next page or any other key to exit: ")
    if user_input.lower() != 'y':
        print("Goodbye.")
        break

        # Increment the page number for the next iteration
    page_number += 1



# cursor.close()
# conn.close()

driver.quit()






                             