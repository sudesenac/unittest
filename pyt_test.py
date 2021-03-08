from selenium import webdriver


def test_setup():
                global driver
                driver = webdriver.Chrome("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
                driver.maximize_window()
               
              
             
def testLogin():
                
                driver.get("https://www.testpine.com/") 
                driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a").click()
                driver.find_element_by_id("email").send_keys("sudesenacizmeci@gmail.com")
                driver.find_element_by_id("password").send_keys("sudeberkay1")
                driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button").click()
                x = driver.title
                assert x =="Testpine"
                
def requirement():
                driver.find_element_by_css_selector("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a").click()
                driver.find_element_by_id("returnList").click()
                driver.find_element_by_name("requirementName").send_keys("practise")
                driver.find_element_by_id("btnAddRequirement").click()
                
def test_teardown():
                driver.close()
                driver.quit()
                print("test ")