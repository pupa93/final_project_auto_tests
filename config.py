class Data:
    # general data
    driver_path = 'driver/chromedriver'
    rostelekom_url = 'https://b2c.passport.rt.ru/'

    # user data
    user_email_right = 'yashkakk@gmail.com'
    user_password_right = 'Yanapupa123-'
    user_email_wrong = 'pupa_kill@yandex.ru'
    user_login_fake = 'jojo the rabbit'
    user_telephone_number_wrong = '+76666666666'
    user_telephone_number_right = '+79179713133'
    user_password_wrong = '666'
    user_name = 'Татьяна Ивановна'
    user_surname = 'Керасирова'
    litcevoj_shet = '363020488487'
    litcevoj_shet_invalid = '363020488487'

    # compare check data
    rgb_wrong_password_color = ''
    auth_menu_elements = 'Телефон\nПочта\nЛогин\nЛицевой счёт'
    default_auth_menu_option_tab = 'Мобильный телефон'

    # xpath for tabs
    telephone_xpath = "//div[@id='t-btn-tab-phone']"
    poshta_xpath = "//div[@id='t-btn-tab-mail']"
    login_xpath = "//div[@id='t-btn-tab-login']"
    personal_account_xpath = "//div[@id='t-btn-tab-ls']"

    # xpath for input box - login, password
    login_xpath = "//input[@id='username']"
    password_xpath = "//input[@id='password']"

    # xpath for Submit button
    submit_button_xpath = "//button[@id='kc-login']"

    # xpath for forgot password button
    forgot_password_button_xpath = "//a[@id='forgot_password']"

    # new user button xpath
    new_user_button_xpath = "//a[@id='kc-register']"

    # xpath for user name on account page
    account_user_name_xpath = "//span[@class='user-name__first-patronymic']"

    # xpath for button need help
    need_help_button_xpath = "//div[@id='widget_bar']"
    need_help_name_inbox_xpath = "//input[@id='full-name']"
    need_help_phone_inbox_xpath = "//input[@id='phone']"
    need_help_send_help_button = "//button[@id='widget_sendPrechat']"
    chat_text_xpath = "//div[@class='title-from-skill-group svelte-1ni618s']"

    # xpath for social_network buttons
    vk_xpath = "//a[@id='oidc_vk']"
    ok_xpath = "//a[@id='oidc_ok']"
    mail_xpath = "//a[@id='oidc_mail']"
    google_xpath = "//a[@id='oidc_google']"
    yandex_xpath = "//a[@id='oidc_ya']"

    # xpath for text from social network to check the place
    vk_text_xpath = "//div[@class='box_msg_gray box_msg_padded']"
    ok_text_xpath = "//div[@class='ext-widget_h_tx']"
    mail_text_xpath = "//span[@class='header__logo']"
    google_text_xpath = "//div[@class='kHn9Lb']"
    yandex_text_path = "//span[@class='passp-add-account-page-title']"




    #####################################
    # long string more than 2500 chars
    long_string = 'dddd@frfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmffddddfrfewmlmklmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmfddddfrfewmlmklmmmmmf.ru'
