from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import backend.const as Const

options = Options()
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)


class Api:
    def __init__(self):
        self.window = None

    # ログイン後の打刻成功判定
    def check_dakoku_before(self):
        res = 'none'
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Const.ATTENDANCE_BUTTON_XPATH)))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Const.LEAVING_BUTTON_XPATH)))
            attendance_button = driver.find_element(By.XPATH, Const.ATTENDANCE_BUTTON_XPATH)
            leaving_button = driver.find_element(By.XPATH, Const.LEAVING_BUTTON_XPATH)
            attendance_button_state = attendance_button.get_attribute('onclick')
            leaving_button_state = leaving_button.get_attribute('onclick')
            if attendance_button_state != '':  # 出勤ボタンが押せる状態
                print(attendance_button_state)
                res = 'leave'
            elif leaving_button_state != '':  # 退勤ボタンが押せる状態
                print(leaving_button_state)
                res = 'attend'

        except Exception as e:
            print("Ieyasu_Dakoku_Check_Error")

        finally:
            print(res)
            return res

    # ログイン後の打刻成功判定
    def check_dakoku_after(self):
        res = 'none'
        try:
            attendance_button = driver.find_element(By.XPATH, Const.ATTENDANCE_BUTTON_XPATH)
            leaving_button = driver.find_element(By.XPATH, Const.LEAVING_BUTTON_XPATH)
            attendance_button_state = attendance_button.get_attribute('onclick')
            leaving_button_state = leaving_button.get_attribute('onclick')
            if attendance_button_state != '':  # 出勤ボタンが押せる状態
                print(attendance_button_state)
                res = 'leave'
            elif leaving_button_state != '':  # 退勤ボタンが押せる状態
                print(leaving_button_state)
                res = 'attend'
            else:
                res = 'none'
        except Exception as e:
            print("Ieyasu_Dakoku_Check_After_Error")

        finally:
            driver.quit()
            return res

    def ieyasu_attendance(self):
        last_timestamp = ''
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Const.ATTENDANCE_BUTTON_XPATH)))
            attendance_button = driver.find_element(By.XPATH, Const.ATTENDANCE_BUTTON_XPATH)
            print(attendance_button.text)
            # TODO: クリック処理
            # TODO: クリック処理成功判定
            # 日付取得
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
            last_timestamp = driver.find_element(By.ID, 'day').text + " " + driver.find_element(By.ID, 'time').text
            return last_timestamp
        except Exception as e:
            print("Ieyasu_Attendance_Error")

        # finally:
        #     driver.quit()

    def ieyasu_leaving(self):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Const.LEAVING_BUTTON_XPATH)))
            leaving_button = driver.find_element(By.XPATH, Const.LEAVING_BUTTON_XPATH)
            print(leaving_button.text)
            # TODO: クリック処理
            # TODO: クリック処理成功判定
            # 日付取得
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
            last_timestamp = driver.find_element(By.ID, 'day').text + " " + driver.find_element(By.ID, 'time').text
            return last_timestamp
        except Exception as e:
            print("Ieyasu_Leaving_Error")

        # finally:
        #     driver.quit()

    def ieyasu_login(self, user_info):
        try:
            # URL接続
            driver.get(user_info["url"])
            # ログインボタンがクリック可能になるまで待機
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, str(Const.IEYASU_LOGIN_BUTTON_XPATH))))
            # ユーザー情報入力
            user_box = driver.find_element(By.ID, Const.USER_BOX_ID)
            user_box.send_keys(user_info["username"])
            password_box = driver.find_element(By.ID, Const.PASSWORD_BOX_ID)
            password_box.send_keys(user_info["password"])

            # ログインボタンクリック
            login_button = driver.find_element(By.XPATH, Const.IEYASU_LOGIN_BUTTON_XPATH)
            login_button.click()

            # ログイン成功判定
            if (driver.current_url == Const.IEYASU_TIMESTAMP_URL):
                return True
            else:
                driver.quit()
                return False
        except Exception as e:
            print("Ieyasu_Login_Error: " + str(e))

        return False
