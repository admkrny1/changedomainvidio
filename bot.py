from selenium import webdriver
import time

def login(driver, email, password):
    driver.get('https://www.vidio.com/users/login')

    email_input = driver.find_element_by_id('email')
    password_input = driver.find_element_by_id('password')

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_button = driver.find_element_by_xpath("//button[contains(text(),'Masuk')]")
    login_button.click()

def change_domain(driver):
    driver.get('https://www.vidio.com/dashboard/setting/email')

    domain_input = driver.find_element_by_id('domain')

    domain_input.clear()
    domain_input.send_keys('ckress.me')

    save_button = driver.find_element_by_xpath("//button[contains(text(),'Simpan')]")
    save_button.click()

def logout(driver):
    driver.get('https://www.vidio.com/users/logout')

def process_single_account(driver):
    email = input('Masukkan email: ')
    password = input('Masukkan password: ')

    login(driver, email, password)
    change_domain(driver)
    logout(driver)

def process_bulk_accounts(driver, file_path):
    with open(file_path, 'r') as file:
        accounts = file.readlines()

    for account in accounts:
        email, password = account.strip().split(',')

        login(driver, email, password)
        change_domain(driver)
        logout(driver)
        time.sleep(2)  # Menambahkan jeda antara akun

# Main program
option = input('Pilih opsi:\n1. Masukkan email dan password\n2. Unggah file CSV\n')

driver = webdriver.Chrome('/path/to/chromedriver')

if option == '1':
    process_single_account(driver)
elif option == '2':
    file_path = input('Masukkan path file CSV: ')
    process_bulk_accounts(driver, file_path)

driver.quit()
