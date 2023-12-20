from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import time
from recipe_dict import recipe_dict
from buttons import RecipeButton


class UI(Tk):
    def __init__(self):
        super().__init__()
        self.stock_report()
        self.driver = uc.Chrome()
        self.login()

        self.recipe_dict = recipe_dict

        chili_button = RecipeButton(self, "chili")
        chili_button.pack()

        self.mainloop()

    def login(self):
        self.driver.get(
            "https://id.meijer.com/oauth2/default/v1/authorize?response_type=code&client_id=0oa22cbewuCICOsKz697&scope=openid+offline_access&redirect_uri=https%3A%2F%2Fwww.meijer.com%2Fbin%2Fmeijer%2Fsignin%2Fv3%2Fcallback&state=https%3A%2F%2Fwww.meijer.com%2F")

        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input27"]')))
        email.send_keys("sirkillz1198@gmail.com")

        next_button = self.driver.find_element(By.XPATH, '//*[@id="form19"]/div[2]/input')
        next_button.click()

        password_entry = "TCqDHnxn9$@bxcX"
        password_input = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input61"]')))
        password_input.send_keys(password_entry)

        verify_button = self.driver.find_element(By.XPATH, '//*[@id="form53"]/div[2]/input')
        verify_button.click()

        time.sleep(2)

    def add_to_cart(self, recipe_key):
        recipe = self.recipe_dict[recipe_key]
        for item in recipe:
            try:
                self.driver.get(item.url)
                select_element = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located
                                                                       ((By.XPATH, item.in_cart_xpath)))
                select = Select(select_element)
                selected_option = select.first_selected_option
                value = int(selected_option.get_attribute('value'))

                new_value = value + 1

                select.select_by_value(str(new_value))

            except TimeoutException:
                add_to_cart = WebDriverWait(self.driver, timeout=2).until(EC.presence_of_element_located
                                                                           ((By.XPATH, item.add_xpath)))

                # Check for in stock or not
                stock_status = add_to_cart.text
                if stock_status == "Out of Stock":
                    print("This item is out of stock")
                    item_element = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/h1')
                    item_name = item_element.text
                    self.append_stock_report(item_name)

                else:
                    add_to_cart.click()
                    time.sleep(1)

    def stock_report(self):
        with open("stock_report.txt", mode="w") as file:
            file.write("Automated Stock Report")

    def append_stock_report(self, item_name):
        with open("stock_report.txt", mode="a") as file:
            file.write(f"\n\n{item_name} is Out of Stock")
