from pageObjects.LoginPage import LoginPage
from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # Test method
    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login ********")
        self.logger.info("************** Verifying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.logger.info("*********** Home Page title test is passed ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("************** Home Page title test failed *********")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.logger.info("************** Verifying Login test *********")
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver) # Create object to access methods of class LoginPage
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title=="<title>Dashboard / nopCommerce administration</title>":
            assert True
            self.logger.info("************** Login test passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************** Login test failed *********")
            self.driver.close()
            assert False
