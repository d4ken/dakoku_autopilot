from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)


class Api:

    def __init__(self):
        self.window = None

    def ieyasu_attendance(self):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnIN1"]')))
            attendance_button = driver.find_element(By.XPATH, '//*[@id="btnIN1"]')
            print(attendance_button.text)
        except Exception as e:
            print("Ieyasu_Attendance_Error")

        finally:
            driver.quit()

    def ieyasu_login(self, user_info):
        last_timestamp = ""
        try:
            # URL接続
            driver.get(user_info["url"])
            # ログインボタンがクリック可能になるまで待機
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new_user"]/div[2]/input')))
            # ユーザー情報入力
            user_box = driver.find_element(By.ID, 'user_login_id')
            user_box.send_keys(user_info["username"])
            password_box = driver.find_element(By.ID, 'user_password')
            password_box.send_keys(user_info["password"])
            # ログインボタンクリック
            login_button = driver.find_element(By.XPATH, '//*[@id="new_user"]/div[2]/input')
            login_button.click()
            # 打刻準備
            sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
            last_timestamp = driver.find_element(By.ID, 'day').text + " " + driver.find_element(By.ID, 'time').text

        except Exception as e:
            print("Ieyasu_Login_Error")
            driver.quit()

        return last_timestamp
