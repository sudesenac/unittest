import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def setUp(self):
 
        self.driver = webdriver.Chrome("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
        self.driver.get("https://www.testpine.com/")
        self.driver.maximize_window()

    def test_practise(self):
        
        self.assertEqual("Testpine - No Code Automation and Test Case Management Platform", self.driver.title," should be  Testpine - No Code Automation and Test Case Management Platform")
        
        self.assertEqual("a",self.driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a").tag_name," hata")
        self.driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a").click()        
        
        
        email = self.driver.find_element_by_id("email")
        email.send_keys('sudesenacizmeci@gmail.com')
        sifre=self.driver.find_element_by_id("password")
        sifre.send_keys("sudeberkay1")    
        
        self.assertEqual("button",self.driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button").tag_name," hata")
        self.driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button").click()
        pass

if __name__ == "__main__":
    unittest.main()
    

