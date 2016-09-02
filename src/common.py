import time
import sys
import random
import string
import pg8000

CREDENTIALS = {
    'user': 'alex',
    'password': 'g2b6tAfu',
    'database': 'money',
    'host': 'localhost'
}


REFFERAL_LINK = ""


def get_random_string():
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_lowercase + string.digits) for _ in range(8)
        )


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element, s
        )
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


def make_db_connection():
    try:
        return pg8000.connect(**CREDENTIALS)
    except pg8000.DatabaseError as e:
        print(str(e))
        sys.exit(1)


def add_user(cursor, email_string, password_string):
    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s);",
        (email_string, password_string))
