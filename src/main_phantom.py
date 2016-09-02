#!/usr/bin/env python3

from selenium import webdriver
import time
import common


def do_magic(cursor, proxy):

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }

    service_args = [
        '--proxy=' + proxy,
        '--proxy-type=socks5',
    ]

    for key, value in enumerate(headers):
        webdriver.DesiredCapabilities.PHANTOMJS[
            'phantomjs.page.customHeaders.{}'.format(key)] = value
    driver = webdriver.PhantomJS(service_args=service_args)

    driver.get("https://temp-mail.ru/option/change")

    random_string = common.get_random_string()
    email_string = random_string + "@lackmail.ru"

    mail = driver.find_element_by_xpath("//form[1]//input[@id='mail']")
    common.highlight(mail)
    mail.send_keys(random_string)

    for option in driver.find_elements_by_tag_name('option'):
        if option.text == '@lackmail.ru':
            option.click()
            break
    button = driver.find_element_by_id("postbut")
    button.click()

    driver.get(common.REFFERAL_LINK)
    links = driver.find_elements_by_xpath("//*[@href]")
    for link in links:
        if "refferal link" in link.text:
            link.click()
            break

    link = driver.find_element_by_id('pic')
    link.click()

    cursor.close()
    while True:
        try:
            user_email = driver.find_element_by_id("UserEmail")
            break
        except:
            continue

    user_email.send_keys(email_string)
    user_password = driver.find_element_by_id("UserPassword")
    user_password.send_keys(random_string)
    user_password_confirm = driver.find_element_by_id("UserPasswordConfirm")
    user_password_confirm.send_keys(random_string)
    form = driver.find_element_by_id("UserRegisterForm")
    form.submit()

    driver.get("https://temp-mail.ru/option/refresh")

    while True:
        try:
            letter = driver.find_element_by_xpath(
                "//*[contains(text(), 'HashFlare account confirm')]"
            )
            break
        except:
            time.sleep(2)
            continue
    letter.click()

    driver.get(driver.current_url)

    links = driver.find_elements_by_xpath("//*[@href]")

    for link in links:
        if "https://hashflare.io/confirm" in link.text:
            link.click()
            break

    common.add_user(email_string=email_string, password_string=random_string)
    driver.quit()


db = common.make_db_connection()

for _ in range(200):
    cursor = db.cursor()
    do_magic(cursor)
    db.commit()
