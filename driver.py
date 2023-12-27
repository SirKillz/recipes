from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from sheets_api import api_pull


class BrowserDriver(uc.Chrome):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.login()

    def login(self):
        self.get('https://id.meijer.com/oauth2/default/v1/authorize?response_type=code&client_id=0oa22cbewuCICOsKz697&scope=openid+offline_access&redirect_uri=https%3A%2F%2Fwww.meijer.com%2Fbin%2Fmeijer%2Fsignin%2Fv3%2Fcallback&state=https%3A%2F%2Fwww.meijer.com%2F')

        email = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input27"]')))
        email.send_keys("sirkillz1198@gmail.com")

        next_button = self.find_element(By.XPATH, '//*[@id="form19"]/div[2]/input')
        next_button.click()

        password_entry = "TCqDHnxn9$@bxcX"
        password_input = WebDriverWait(self, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="input61"]')))
        password_input.send_keys(password_entry)

        verify_button = self.find_element(By.XPATH, '//*[@id="form53"]/div[2]/input')
        verify_button.click()

        time.sleep(2)

    def add_to_cart(self, recipe_key):
        recipe = api_pull(recipe_key=recipe_key)

        # Statically declare the X-path of items already in cart or ready to add to cart
        in_cart_xpath = '//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/select'
        add_xpath = '//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button/span'

        # Loop through all urls in the api pull
        # First check to see if the item is already in our cart
        for item in recipe:
            try:
                self.get(item.url)
                select_element = WebDriverWait(self, timeout=5).until(EC.presence_of_element_located
                                                                             ((By.XPATH, in_cart_xpath)))
                select = Select(select_element)
                selected_option = select.first_selected_option
                value = int(selected_option.get_attribute('value'))

                new_value = value + 1

                select.select_by_value(str(new_value))

            # We will get a timeout exception if the item is not in our cart and thus we can proceed to add
            except TimeoutException:
                add_to_cart = WebDriverWait(self, timeout=5).until(EC.presence_of_element_located
                                                                          ((By.XPATH, add_xpath)))

                # First check if the item is in stock or not
                stock_status = add_to_cart.text
                if stock_status == "Out of Stock":
                    print("This item is out of stock")
                    # item_element = self.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/h1')
                    # item_name = item_element.text
                    # self.append_stock_report(item_name)

                    if item.sub_url != "":
                        try:
                            self.get(item.sub_url)
                            select_element = WebDriverWait(self, timeout=5).until(EC.presence_of_element_located
                                                                                         ((By.XPATH, in_cart_xpath)))
                            select = Select(select_element)
                            selected_option = select.first_selected_option
                            value = int(selected_option.get_attribute('value'))

                            new_value = value + 1

                            select.select_by_value(str(new_value))
                        except TimeoutException:
                            add_to_cart = WebDriverWait(self, timeout=5).until(EC.presence_of_element_located
                                                                                      ((By.XPATH, add_xpath)))
                            add_to_cart.click()

                # If the stock status is NOT "Out of Stock" we are good to simply add to cart
                else:
                    add_to_cart.click()
                    time.sleep(1)