import pytest
import re
import time

import my_module
from my_module import Page
from config import Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException

from matplotlib import colors


browser = webdriver.Chrome(Data.driver_path)


def test_pupa_tc01_authorization_valid_email():
    # client authorization by valid Email and password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Почта»
    rost_tel_page.select_tab('Почта')
    # put valid e-mail and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.user_email_right, Data.user_password_right)
    # check if login was successful
    assert rost_tel_page.check_if_login_successful() == True


def test_pupa_tc02_authorization_valid_email_but_wrong_password():
    # client authorization by valid email with invalid password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Почта»
    rost_tel_page.select_tab('Почта')
    # put invalid e-mail and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.user_email_right, Data.user_password_wrong)
    # check if login was unsuccessful
    assert rost_tel_page.check_if_login_successful() == None


def test_pupa_tc03_authorization_by_valid_phone_number_and_password():
    # client authorization by valid phone number and password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Телефон»
    rost_tel_page.select_tab('Телефон')
    # put valid telephone number and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.user_telephone_number_right, Data.user_password_right)
    # check if login was successful
    assert rost_tel_page.check_if_login_successful() == True


def test_pupa_04_authorization_by_valid_phone_number_and_invalid_password():
    # client authorization by valid phone number and invalid password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Телефон»
    rost_tel_page.select_tab('Телефон')
    # put invalid e-mail and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.user_telephone_number_right, Data.user_password_wrong)
    # check if login was unsuccessful
    assert rost_tel_page.check_if_login_successful() == None


def test_pupa_tc05_authorization_by_valid_personal_account_and_valid_password():
    # client authorization by valid personal account and valid password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Лицевой счёт»
    rost_tel_page.select_tab('Лицевой счёт')
    # put valid telephone number and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.litcevoj_shet, Data.user_password_right)
    # check if login was successful
    assert rost_tel_page.check_if_login_successful() == True


def test_pupa_tc06_authorization_by_invalid_personal_account_and_invalid_password():
    # client authorization by invalid personal account and invalid password
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Лицевой счёт»
    rost_tel_page.select_tab('Лицевой счёт')
    # put valid telephone number and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.litcevoj_shet_invalid, Data.user_password_wrong)
    # check if login was successful
    assert rost_tel_page.check_if_login_successful() == None


def test_pupa_tc07_client_authorization_by_email_and_password_more_2500_characters():
    # Client authorization by e-mail and password with a length of more than 2500 characters
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # Select authentication type «Почта»
    rost_tel_page.select_tab('Почта')
    # put valid telephone number and password into input form
    rost_tel_page.enter_auth_data_and_submit(Data.long_string, Data.long_string)
    # check if login was successful
    body_text = rost_tel_page.getting_body_text()
    assert body_text == 'Internal Server Error'


def test_pupa_tc08_the_functionality_forgot_password():
    # Checking the functionality of the "Forgot password" button
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # click on "forgot button" and check text from upper part
    upper_text_from_forgot_password = rost_tel_page.check_forgot_button()
    assert upper_text_from_forgot_password == 'Восстановление пароля'


def test_pupa_tc09_the_functionality_register_button():
    # Checking the functionality of the "Register" button
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # click on "Register button" and check text from upper part
    upper_text = rost_tel_page.check_register_button()
    assert upper_text == 'Регистрация'


def test_pupa_tc10_functionality_chat_button_and_welcome_message():
    # Checking the functionality of the chat button and receiving a welcome message
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # scnd - need to find button and click on it, compare text result
    text_from_chat = rost_tel_page.check_need_help_bttn()
    assert text_from_chat == 'Здравствуйте! Мы с удовольствием ответим на интересующие Вас вопросы'


def test_pupa_tc11_functionality_authorization_button_vkontakte():
    # Checking the functionality of the authorization button through the social network "VK"
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # need to find vkontakte button click on it and user sees the authorization form through the social
    vk_text_to_check = rost_tel_page.check_social_network_button('VK')
    assert vk_text_to_check == 'Sign in to VK to continue'


def test_pupa_tc12_functionality_authorization_button_ok():
    # Checking the functionality of the authorization button through the social network "OK"
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # need to find odnoklasniki button click on it and user sees the authorization form through the social
    ok_text_to_check = rost_tel_page.check_social_network_button('OK')
    assert ok_text_to_check == 'OK'


def test_pupa_tc13_functionality_authorization_button_mail():
    # Checking the functionality of the authorization button through the social network "Mail.RU"
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # need to find mail moi mir button click on it and user wil see the authorization form through the social
    mail_text_to_check = rost_tel_page.check_social_network_button('Mail')
    assert mail_text_to_check == 'My World@Mail.Ru'


def test_pupa_tc14_functionality_authorization_button_google():
    # Checking the functionality of the authorization button through the social network "Google"
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # need to find Google button click on it and user wil see the authorization form through the social
    mail_text_to_check = rost_tel_page.check_social_network_button('Google')
    assert mail_text_to_check == 'Войдите в аккаунт Google'


def test_pupa_tc15_functionality_authorization_button_yandex():
    # Checking the functionality of the authorization button through the social network "Yandex"
    # first - initialize class object
    rost_tel_page = Page()
    # frst - loading to page
    rost_tel_page.enter_page()
    # need to find Yandex button click on it and user wil see the authorization form through the social
    mail_text_to_check = rost_tel_page.check_social_network_button('Yandex')
    assert mail_text_to_check == 'Войдите с Яндекс ID'

def test_pupa_tc16_menu_auth_checking_all_elements():
    # checking all menu elements for authentication
    browser.get(Data.rostelekom_url)
    browser.implicitly_wait(10)
    auth_elm_menu = browser.find_element(By.XPATH, "//div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']")
    assert(auth_elm_menu.text == Data.auth_menu_elements)


def test_pupa_tc17_checking_menu_auth_default():
    # checking default option whe page is loaded for auth menu
    browser.get(Data.rostelekom_url)
    browser.implicitly_wait(10)
    default_auth_menu_option = browser.find_element(By.XPATH, "//div[@class='rt-input-container tabs-input-container__login']//span[@class='rt-input__placeholder']")
    assert (default_auth_menu_option.text == Data.default_auth_menu_option_tab)


def test_pupa_tc18_password_form():
    # checking if main page has input form -password-
    browser.get(Data.rostelekom_url)
    browser.implicitly_wait(10)
    input_form_password = browser.find_element(By.XPATH, "//div[@class='rt-input-container']//span[@class='rt-input__placeholder']")
    assert (input_form_password.text == 'Пароль')


def test_pupa_tc19_moto_rosttelekom():
    # checking if main page has moto
    browser.get(Data.rostelekom_url)
    browser.implicitly_wait(10)
    try:
        browser.find_element(By.XPATH, "//p[@class='what-is__desc']")
    except NoSuchElementException:
        return False
    return True


def test_pupa_tc20_auto_shifting_tab():
    # phone number / email / login / personal account - the authentication selection tab changes automatically
    browser.get(Data.rostelekom_url)
    browser.implicitly_wait(10)

    # find telephone inbox
    telephone_input_place_sign = browser.find_element(By.XPATH, "//span[@class='rt-input__placeholder']")
    telephone_input_place = browser.find_element('id', 'username')
    # find password inbox
    password_input_place = browser.find_element('id', 'password')

    # put email into telephone inbox

    if telephone_input_place_sign.text == 'Мобильный телефон':
        telephone_input_place.send_keys(Data.user_email_wrong + Keys.RETURN)
        browser.implicitly_wait(10)
    else:
        return False

    # put password into inbox in order to shift did happen
    password_input_place.send_keys(Data.user_password_wrong)
    browser.implicitly_wait(15)

    telephone_input_place_sign2 = browser.find_element(By.XPATH, "//input[@id='username']")

    try:
        if telephone_input_place_sign2.text == 'Электронная почта':
            # erase everything form login inbox
            browser.find_element(By.XPATH, "//input[@name='username']").clear()
            # put a fake login in order to make shift
            telephone_input_place_sign2.send_keys(Data.user_login_fake)
    except NoSuchElementException:
        return False
    browser.implicitly_wait(5)

    # checking if input box shifted and its for mail and for the telephone number
    telephone_input_place_sign3 = browser.find_element(By.XPATH, "//input[@id='username']")
    try:
        if telephone_input_place_sign3.text == 'Логин':
            return True
    except NoSuchElementException:
        return False

    # checking if possible to shift if "Littcevoj shet" number was added to Login textbox
    # frst - we should move to "Pochta" tab
    posta_tab = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']")
    posta_tab.click()

    # scnd - put "litcevoj shet" into "Электронная почта" box
    telephone_input_place_sign3.send_keys(Data.litcevoj_shet + Keys.RETURN)

    # check if tab was shifted
    telephone_input_place_sign3 = browser.find_element(By.XPATH, "//input[@id='username']")
    try:
        if telephone_input_place_sign3.text == 'Лицевой счёт':
            return True
    except NoSuchElementException:
        return False


def test_pupa_tc21_knopka_nomer_right_number():
    # test of customer successful authorization by phone number
    browser.implicitly_wait(10)
    browser.get(Data.rostelekom_url)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(Data.user_telephone_number_right + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(Data.user_password_right + Keys.RETURN)
    browser.implicitly_wait(10)

    # click on the new user button
    search_button = browser.find_element(By.XPATH, "//button[@name='login']")
    search_button.click()
    browser.implicitly_wait(10)

    # pulling user name and surname
    user_surname = browser.find_element(By.XPATH, "//span[@class='user-name__last-name']")
    user_name = browser.find_element(By.XPATH, "//span[@class='user-name__first-patronymic']")

    assert user_surname.text == Data.user_surname and user_name.text == Data.user_name
    browser.get('about:blank')


def test_pupa_tc22_knopka_nomer_wrong_number():
    # test of customer none successful authorization by phone number
    browser.implicitly_wait(10)
    browser.get(Data.rostelekom_url)

    input_field = browser.find_element('id', 'username')
    input_field.send_keys(Data.user_telephone_number_wrong + Keys.RETURN)

    input_field = browser.find_element('id', 'password')
    input_field.send_keys(Data.user_password_wrong + Keys.RETURN)
    browser.implicitly_wait(10)

    # click on the new user button
    search_button = browser.find_element(By.XPATH, "//button[@name='login']")
    search_button.click()
    browser.implicitly_wait(10)

    # if password or number wrong we will see error-message
    popup_error_message = browser.find_element(By.XPATH, "//span[@id='form-error-message']")

    # checking if forget password button is orange
    forgot_passwrd_bttn = browser.find_element(By.XPATH, "//a[@id='forgot_password']")

    # getting css color value
    css_color = forgot_passwrd_bttn.value_of_css_property('color')
    print(css_color)
    print(Color.from_string(css_color))
    print(colors.is_color_like(css_color))



    assert popup_error_message.text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'












