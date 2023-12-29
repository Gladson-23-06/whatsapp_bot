# imported pakges
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

# input for program
name = input("name or number: ")
message = input("Enter the message: ")
no_of_times = int (input("how many times should this message send ="))

# intialize the web broser & web driver
obj = Service("C:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=obj)

# start whatsapp in the browser
driver.get("https://web.whatsapp.com/")

# whatsapp site loding code
while True:
    try:
        check = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[1]/div/span')
        print(check.is_displayed())
        if (check.is_displayed() == True):
            print("------loading completed--------")
            break
    except:
        sleep(1)
    pass

# This is the time delay fun for every driver action
# driver.implicitly_wait(2)

def chat_find_fun():
        
        for x in range(1,30):    
            xpath = '//*[@id="pane-side"]/div/div/div/div['+str(x)+']/div/div/div/div[2]/div[1]/div[1]/div/span'
            try:
                check=driver.find_element(By.XPATH,xpath)
                if check.is_displayed():
                    print("main chat found") 
                    try:   
                        check=driver.find_element(By.XPATH,xpath)
                        value = check.get_attribute("title")
                        if value == name:
                            print("defined chat found")
                            ############### funtion call ######################## 
                            chat_click_fun(xpath)                               #
                            #####################################################
                            break
                        else:
                            print("defined chat not found")            
                    except:
                        print("'chat_name_find_fun' Error found")    
                else:
                     print("main chat not found")   
            except:
                print("ERROR found 'chat_find_fun' ")
                                    
def chat_click_fun(xpath): 
        try:
            driver.find_element(By.XPATH,xpath).click()
            loop_fun(no_of_times)
        except:
                print("ERROR found in 'chat_click_fun' ")

def message_fun():
     driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(message)
     driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

def loop_fun(no_of_times):
     for x in range(1,no_of_times+1):
          message_fun()

chat_find_fun()
print("----------closing the browser--------")
driver.quit() 


