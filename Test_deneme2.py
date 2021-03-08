import unittest
from selenium import webdriver

class TestDeneme2(unittest.TestCase):


    def setUp(self):
      
        self.driver = webdriver.Chrome("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
        self.driver.get("https://www.testpine.com/")
        self.driver.maximize_window()
        
        self.assertEqual("a",self.driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a").tag_name," hata")
        self.driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a").click()        
        self.driver.find_element_by_id("email").send_keys('sudesenacizmeci@gmail.com')
        self.driver.find_element_by_id("password").send_keys("sudeberkay1")    
        self.assertEqual("button",self.driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button").tag_name," hata")
        self.driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button").click()


    def test_practise(self):
        self. requirement=self.driver.find_element_by_css_selector("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a")
        self.requirement.click()
        self.newRequirement=self.driver.find_element_by_id("returnList")
        self.newRequirement.click()
        self.requirementName=self.driver.find_element_by_name("requirementName")
        self.requirementName.send_keys("practise")
        self.requirementKayit=self.driver.find_element_by_id("btnAddRequirement")
        self.requirementKayit.click()
     
     
     
     
    def tearDown(self):
        self.driver.quit()
    


