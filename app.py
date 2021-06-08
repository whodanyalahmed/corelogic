from platform import system
import time,os
from credentials import IdPass
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def resource_path(relative_path):
    try:
        base_path = system._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

path = resource_path('I:/clients/chromedriver.exe')
        
print("\n\nProcessing.....")
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-extensions')
# options.add_argument('--profile-directory=Default')
# # options.add_argument("--incognito")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("--start-maximized")
# options.add_argument('headless')
options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver =webdriver.Chrome(path,options=options)
driver.maximize_window()
def loadSiteNAcceptCookies():
    try:
        driver.get("https://access-api.corelogic.asia/access/loginPage.html")
        # driver.get("https://www.uber.com/us/en/drive/")
        print("success : Loaded...")
    except Exception as e:
        print("info : website taking too long to load...stopped")
        driver.refresh()
    finally:
        time.sleep(1)
        try:
            
            time.sleep(0.25) #sleep for 250 milliseconds
            
            driver.find_element_by_css_selector("button.ub-emb-close").click()

            time.sleep(0.25) #sleep for 250 milliseconds
            driver.find_element_by_css_selector("button.eu-cookie-compliance-secondary-button").click()
        except:
            print("error : cant find cookies")
        finally:
            # driver.find_element_by_xpath("//div[@id='block-nicemenus-4']/ul/li[2]/span[@class='toolbar-icon-menu-link-content:54a7115a-1027-4029-9be3-3396fe77d372']").click()
            li = driver.find_element_by_xpath("//div[@id='block-nicemenus-4']/ul/li[2]")
            time.sleep(2)
            container = driver.find_element_by_xpath("//div[@id='block-nicemenus-4']/ul/li[2]/ul")
            driver.execute_script("arguments[0].style.display = 'block';", container)
            driver.execute_script("arguments[0].className += ' over';", li)
            # driver.find_element_by_css_selector("span.toolbar-icon']")
            time.sleep(1)
            driver.find_element_by_link_text("RP Data Professional").click()
        print("success : Clicked Accept Cookies")
        
loadSiteNAcceptCookies()
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])

def login():
    try:
        driver.find_element_by_id("username").send_keys(IdPass.username)
        driver.find_element_by_id("password").send_keys(IdPass.password)
        driver.find_element_by_id("login").click()
        print("success : successfully logged in")
    except:
        print("error : cant login...")

login()    


time.sleep(10)
def addressSearchNDownload(address):
    if(driver.title == "CoreLogic RP Data"):
        print("info : Older version")
        time.sleep(5)
        driver.find_element_by_xpath("//span[@id='cruxInvited']/a").click()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:

    # while(True):
    #     if(driver.title=="CoreLogic RP Data"):
    #         break
    #     else:
    #         time.sleep(5)
        print("info : Newer version")
        input = driver.find_element_by_xpath('//input[@aria-controls="react-autowhatever-1"]')
        time.sleep(2)
        input.send_keys(address)
        time.sleep(3)
        input.send_keys(Keys.ARROW_DOWN)
        input.send_keys(Keys.ENTER)

addressSearchNDownload("5 Wirildar Drive Elanora")