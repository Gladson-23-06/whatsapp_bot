# imported pakges
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

# intialize the web broser & web driver
obj = Service("C:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=obj)



# start whatsapp in the browser
driver.get("https://web.whatsapp.com/")

while True:
    try:
        check = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[1]/div/span')
        print(check.is_displayed())
        if (check.is_displayed() == True):
            break
    except:
        print("loding ........")
    pass
sleep(20)