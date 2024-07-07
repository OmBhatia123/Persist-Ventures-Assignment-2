from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def create_wallet():
    driver = webdriver.Chrome()
    try:
        driver.get('https://pump.fun')
        time.sleep(10)  # Wait for the page to load

        # Click the button to create a new wallet (update with the correct ID or class)
        driver.find_element(By.ID, 'create_wallet_button').click()
        time.sleep(5)

        # Fill in the wallet details
        driver.find_element(By.ID, 'wallet_name').send_keys('New Wallet')
        driver.find_element(By.ID, 'create_wallet_submit').click()
        time.sleep(5)

        # Get the wallet address (update with the correct ID or class)
        wallet_address = driver.find_element(By.ID, 'wallet_address').text
        return wallet_address
    finally:
        driver.quit()

def post_comment(wallet_address):
    driver = webdriver.Chrome()
    try:
        driver.get('https://pump.fun')
        time.sleep(10)

        # Connect the wallet (update with the correct ID or class)
        driver.find_element(By.ID, 'connect_wallet_button').click()
        driver.find_element(By.ID, 'wallet_input').send_keys(wallet_address)
        driver.find_element(By.ID, 'connect_wallet_submit').click()
        time.sleep(5)

        # Post a comment
        comment = "Check out this new trading bot: [link]"
        driver.find_element(By.ID, 'comment_input').send_keys(comment)
        driver.find_element(By.ID, 'post_comment_button').click()
        time.sleep(5)
    finally:
        driver.quit()
