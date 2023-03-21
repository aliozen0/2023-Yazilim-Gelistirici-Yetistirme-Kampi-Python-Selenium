from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class TestApp():
    def testUsername(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        errorMsg = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMsg.text == "Epic sadface: Username is required"
        print(f"> testUsername Fonk. Test Sonucu: {testResult}")
    
    def testPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("test123")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        errorMsg = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMsg.text == "Epic sadface: Password is required"
        print(f"> testPassword Fonk. Test Sonucu: {testResult}")
    
    def testLockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(2)
        
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        errorMsg = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMsg.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"> testLockedOutUser Fonk. Test Sonucu: {testResult}")
    
    def testIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        errorInput = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorInput.click()
        sleep(2)
                
        try:
            driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            print("> testIcon Fonk. Test Sonucu: False")
        
        except:
            print("> testIcon Fonk. Test Sonucu: True")
    
    def testPassPage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        pageMsg = driver.current_url
        testResult = pageMsg == "https://www.saucedemo.com/inventory.html"
        print(f"> testPassPage Fonk. Test Sonucu: {testResult}")
    
    def testSixProduct(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        
        loginButon = driver.find_element(By.ID, "login-button")
        loginButon.click()
        sleep(2)
        
        listProduct = driver.find_elements(By.CLASS_NAME,"inventory_item")

        testResult = len(listProduct) == 6
        print(f"> testSixProduct Fonk. Test Sonucu: {testResult}")

app = TestApp()
app.testUsername()
app.testPassword()
app.testLockedOutUser()
app.testIcon()
app.testPassPage()
app.testSixProduct()