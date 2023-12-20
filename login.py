from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def login(driver_instance):
    driver_instance.get("https://id.meijer.com/oauth2/default/v1/authorize?response_type=code&client_id=0oa22cbewuCICOsKz697&scope=openid+offline_access&redirect_uri=https%3A%2F%2Fwww.meijer.com%2Fbin%2Fmeijer%2Fsignin%2Fv3%2Fcallback&state=https%3A%2F%2Fwww.meijer.com%2F")

    email = WebDriverWait(driver_instance, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input27"]')))
    email.send_keys("sirkillz1198@gmail.com")

    next_button = driver_instance.find_element(By.XPATH, '//*[@id="form19"]/div[2]/input')
    next_button.click()

    password_entry = "TCqDHnxn9$@bxcX"
    password_input = WebDriverWait(driver_instance, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="input61"]')))
    password_input.send_keys(password_entry)

    verify_button = driver_instance.find_element(By.XPATH, '//*[@id="form53"]/div[2]/input')
    verify_button.click()

    time.sleep(2)