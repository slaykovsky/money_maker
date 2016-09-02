#!/usr/bin/env python3

import common
from selenium import webdriver


def do_magic(cursor):
    driver = webdriver.Chrome()
    driver.get(common.REFFERAL_LINK)
    links = driver.find_elements_by_xpath("//*[@href]")
    for link in links:
        if "refferal link" in link.text:
            link.click()
            break

    link = driver.find_element_by_id('pic')
    link.click()

    random_string = common.get_random_string()
    print(random_string)
    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s);",
        (random_string + "@lackmail.ru", random_string)
    )
    cursor.close()
    while True:
        try:
            user_email = driver.find_element_by_id("UserEmail")
            break
        except:
            continue
    user_email.send_keys(random_string + "@lackmail.ru")
    user_password = driver.find_element_by_id("UserPassword")
    user_password.send_keys(random_string)
    user_password_confirm = driver.find_element_by_id("UserPasswordConfirm")
    user_password_confirm.send_keys(random_string)
    form = driver.find_element_by_id("UserRegisterForm")
    form.submit()

    driver.get("https://temp-mail.ru/option/change")

    mail = driver.find_element_by_xpath("//form[1]//input[@id='mail']")
    common.highlight(mail)
    mail.send_keys(random_string)

    for option in driver.find_elements_by_tag_name('option'):
        if option.text == '@lackmail.ru':
            option.click()
            break
    button = driver.find_element_by_id("postbut")
    button.click()

    driver.get("https://temp-mail.ru/option/refresh")

    while True:
        try:
            letter = driver.find_element_by_xpath(
                "//*[contains(text(), 'HashFlare account confirm')]"
            )
            break
        except:
            common.time.sleep(2)
            continue
    letter.click()

    driver.get(driver.current_url)

    links = driver.find_elements_by_xpath("//*[@href]")

    for link in links:
        if "https://hashflare.io/confirm" in link.text:
            link.click()
            break

    driver.quit()


db = common.make_db_connection()

for _ in range(100):
    cursor = db.cursor()
    do_magic(cursor)
    db.commit()
