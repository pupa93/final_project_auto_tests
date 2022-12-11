# file with most used functionality
from config import Data
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#browser = webdriver.Chrome(Data.driver_path)


class Page:
    # Class variable
    def __init__(self):
        self.browser = webdriver.Chrome(Data.driver_path)

    def enter_page(self):
        # rosttelekom page entry
        self.browser.get(Data.rostelekom_url)
        self.browser.implicitly_wait(10)

    def select_tab(self, tab_name):
        tab_xpath = ''
        # find tab and click on it
        if tab_name == 'Телефон':
            # Use the find_element_by_xpath() method to find the button element using its text
            tab = self.browser.find_element(By.XPATH, Data.telephone_xpath)
            # Click on the button using the click() method
            tab.click()
        elif tab_name == 'Почта':
            # Use the find_element_by_xpath() method to find the button element using its text
            tab = self.browser.find_element(By.XPATH, Data.poshta_xpath)
            # Click on the button using the click() method
            tab.click()
        elif tab_name == 'Логин':
            # Use the find_element_by_xpath() method to find the button element using its text
            tab = self.browser.find_element(By.XPATH, Data.login_xpath)
            # Click on the button using the click() method
            tab.click()
        elif tab_name == 'Лицевой счёт':
            # Use the find_element_by_xpath() method to find the button element using its text
            tab = self.browser.find_element(By.XPATH, Data.personal_account_xpath)
            # Click on the button using the click() method
            tab.click()


    def enter_auth_data_and_submit(self, login, password):
        # Find the login input box using the id attribute
        login_input = self.browser.find_element(By.XPATH, Data.login_xpath)

        # Enter the login into the login input box using the send_keys() method
        login_input.send_keys(login)

        # Find the password input box using the id attribute
        password_input = self.browser.find_element(By.XPATH, Data.password_xpath)

        # Enter the password into the password input box using the send_keys() method
        password_input.send_keys(password)

        # Click on Submit button
        submit_button = self.browser.find_element(By.XPATH, Data.submit_button_xpath)
        submit_button.click()
        self.browser.implicitly_wait(5)

    def getting_body_text(self):
        body_text = self.browser.find_element(By.TAG_NAME, 'body')
        return body_text.text


    def check_if_login_successful(self):
        # Wait for the page to fully load
        user_name = 'xxx'
        wait = WebDriverWait(self.browser, 10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Data.account_user_name_xpath)))
        except:
            False

        # we need to check if name of the user appear in upper part of page
        # lets get the expecetd user name
        try:
            user_name = self.browser.find_element(By.XPATH, Data.account_user_name_xpath)
        except:
            False

        try:
            if user_name.text == Data.user_name:
                return True
            else:
                False
        except:
            False


    def check_forgot_button(self):
        # click on forgot button and go to forgot password page
        # frst- find forgot password button
        forgot_button = self.browser.find_element(By.XPATH, Data.forgot_password_button_xpath)
        # click on forgot button
        forgot_button.click()
        self.browser.implicitly_wait(5)
        # getting text from upper part of the page
        upper_text = self.browser.find_element(By.XPATH, "//h1[@class='card-container__title']")
        return upper_text.text

    def check_register_button(self):
        # click on new user button and go to new user page
        # frst - find the new user button
        new_user_button = self.browser.find_element(By.XPATH, Data.new_user_button_xpath)
        #click on new user button
        new_user_button.click()
        self.browser.implicitly_wait(5)
        # getting text from upper part of the page
        upper_text = self.browser.find_element(By.XPATH, "//h1[@class='card-container__title']")
        return upper_text.text

    def check_need_help_bttn(self):
        # click on need help button
        # frst - find button
        need_help_button = self.browser.find_element(By.XPATH, Data.need_help_button_xpath)
        #click on button
        need_help_button.click()
        self.browser.implicitly_wait(5)
        # scnd -looking for name need help inbox
        name_need_help_inbox = self.browser.find_element(By.XPATH, Data.need_help_name_inbox_xpath)
        # put name
        name_need_help_inbox.send_keys(Data.user_name)
        # thrd -looking for telephone number need help inbox
        number_need_help_inbox = self.browser.find_element(By.XPATH, Data.need_help_phone_inbox_xpath)
        # put number
        number_need_help_inbox.send_keys(Data.user_telephone_number_right)
        # fourth - looking for Napisat button
        send_help_button = self.browser.find_element(By.XPATH, Data.need_help_send_help_button)
        send_help_button.click()
        self.browser.implicitly_wait(5)
        # fifth - looking for text chat
        upper_text_chat = self.browser.find_element(By.XPATH, Data.chat_text_xpath)
        return upper_text_chat.text

    def check_social_network_button(self, social_network):
        # frst - need identify what auth social network we need to check
        if social_network == 'VK':
            # Use the find_element_by_xpath() method to find the button element using its text
            social_net_button = self.browser.find_element(By.XPATH, Data.vk_xpath)
            # Click on the button using the click() method
            social_net_button.click()
            self.browser.implicitly_wait(5)
            # taking text from vk page
            text_vk = self.browser.find_element(By.XPATH, Data.vk_text_xpath)
            return text_vk.text
        elif social_network == 'OK':
            # Use the find_element_by_xpath() method to find the button element using its text
            social_net_button = self.browser.find_element(By.XPATH, Data.ok_xpath)
            # Click on the button using the click() method
            social_net_button.click()
            self.browser.implicitly_wait(5)
            # taking text from ok page
            text_ok = self.browser.find_element(By.XPATH, Data.ok_text_xpath)
            return text_ok.text
        elif social_network == 'Mail':
            # Use the find_element_by_xpath() method to find the button element using its text
            social_net_button = self.browser.find_element(By.XPATH, Data.mail_xpath)
            # Click on the button using the click() method
            social_net_button.click()
            self.browser.implicitly_wait(5)
            # taking text from ok page
            text_mail = self.browser.find_element(By.XPATH, Data.mail_text_xpath)
            return text_mail.text
        elif social_network == 'Google':
            # Use the find_element_by_xpath() method to find the button element using its text
            social_net_button = self.browser.find_element(By.XPATH, Data.google_xpath)
            # Click on the button using the click() method
            social_net_button.click()
            self.browser.implicitly_wait(5)
            # taking text from google page
            text_google = self.browser.find_element(By.XPATH, Data.google_text_xpath)
            return text_google.text
        elif social_network == 'Yandex':
            # Use the find_element_by_xpath() method to find the button element using its text
            social_net_button = self.browser.find_element(By.XPATH, Data.yandex_xpath)
            # Click on the button using the click() method
            social_net_button.click()
            self.browser.implicitly_wait(5)
            # taking text from yandex page
            text_yandex = self.browser.find_element(By.XPATH, Data.yandex_text_path)
            return text_yandex.text


































