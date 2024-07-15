import re
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from database import database, Outlet

driver = webdriver.Chrome()
driver.get("https://www.subway.com.my/find-a-subway")

fp_searchAddress = driver.find_element(By.ID, "fp_searchAddress")
fp_searchAddress.send_keys("kuala lumpur")
fp_searchAddress.submit()

outlets = []
operatings =[]

fp_listitems = driver.find_elements(By.CLASS_NAME, "fp_listitem")
for fp_listitem in fp_listitems:
    outlet = {}
    outlet['address'] = fp_listitem.find_elements(By.TAG_NAME, 'p')[0].text
    outlet['name'] = fp_listitem.find_element(By.TAG_NAME, 'h4').text.replace('Subway ', '')
    outlet['waze_link'] = fp_listitem.find_element(By.XPATH, '//a[contains(@href, "waze")]').get_attribute('href')
    ps = fp_listitem.find_elements(By.TAG_NAME, 'p')
    outlet['operating_hours'] = []
    for p in ps:
        if len(p.text) and p.text not in outlet['address']:
            outlet['operating_hours'].append(
                p.text
                .replace(' AM', 'AM')
                .replace(' PM', 'PM')
                .replace('–', '-')
                .replace('&', '-')
                .replace('to', '-')
                .replace(',', '')
                .replace('(', '')
                .replace(')', '')
                .replace(' ', ', ')
                .replace(', -, ', ' - ')
                .replace('AM', ' AM')
                .replace('PM', ' PM')
            )
    outlet['operating_hours'] = json.dumps(outlet['operating_hours'])
    if re.findall(r'\b[56]\d{4}\b', outlet['address']): outlets.append(outlet)

database.create_tables([Outlet])

Outlet.insert_many(outlets).execute()

driver.quit()