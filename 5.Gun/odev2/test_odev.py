from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Class:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def test_username(self):
        self.waitForElementVisible((By.ID,"login-button"))
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        errorMsg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-username.png")
        assert errorMsg.text == "Epic sadface: Username is required"
       
    def test_password(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("test123")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        errorMsg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-password.png")
        assert errorMsg.text == "Epic sadface: Password is required"
        
    def test_locked_out_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        errorMsg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-user.png")
        assert errorMsg.text == "Epic sadface: Sorry, this user has been locked out."
    
    def test_icon(self):
        self.waitForElementVisible((By.ID,"login-button"))
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button"))
        errorInput = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorInput.click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            self.driver.save_screenshot(f"{self.folderPath}/test-icin.png")
            assert False

        except:
            self.driver.save_screenshot(f"{self.folderPath}/test-icon.png")
            assert True
    
    def test_pass_page(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        pageMsg = self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-pass-page.png")
        assert pageMsg == "https://www.saucedemo.com/inventory.html"
        
    def test_six_product(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        listProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-six-product.png")
        assert len(listProduct) == 6

    def test_price_bike_light(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div"))
        priceProduct = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div")
        self.driver.save_screenshot(f"{self.folderPath}/test-price-bike-light.png")
        assert priceProduct.text == '$9.99'
    
    def test_problem_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("problem_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        pageMsg = self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-problem-user.png")
        assert pageMsg == "https://www.saucedemo.com/inventory.html"
    
    def test_performance_glitch_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("performance_glitch_user")
        passwordInput.send_keys("secret_sauce")
        loginButon = self.driver.find_element(By.ID, "login-button")
        loginButon.click()
        pageMsg = self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-performance-glitch-user.png")
        assert pageMsg == "https://www.saucedemo.com/inventory.html"

    def getData():
        data=[("username1","password1"),
              ("deneme1","deneme2"),
              ("giris","sifre123")]
        return data

    @pytest.mark.parametrize("username,password",getData())
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"