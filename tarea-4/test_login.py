from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time


service = Service('./geckodriver')  


driver = webdriver.Firefox(service=service)

def test_login_page():
    
    driver.get("http://127.0.0.1:5001/login")  
    time.sleep(2)

   
    assert "Iniciar Sesión" in driver.title

    
    username = driver.find_element(By.ID, "username")
    username.send_keys("admin")
    password = driver.find_element(By.ID, "password")
    password.send_keys("password123")
    password.send_keys(Keys.RETURN)

    time.sleep(2)
    assert "Bienvenido, admin!" in driver.page_source

def close_browser():
    driver.quit()

if __name__ == "__main__":
    test_login_page()
    close_browser()
