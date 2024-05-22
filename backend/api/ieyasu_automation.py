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

    # 出勤状態判定
    def check_attendance(self, is_quit=False):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, Const.ATTENDANCE_BUTTON_ID)))
        attendance_button = driver.find_element(By.ID, Const.ATTENDANCE_BUTTON_ID)
        attendance_button_state = attendance_button.get_attribute('onclick')
        if is_quit:
            driver.quit()
        # 出勤ボタンが押せる状態
        if attendance_button_state != '':
            return True

        return False


    # 打刻状態判定
    def check_leaving(self, is_quit=False):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, Const.LEAVING_BUTTON_ID)))
        leaving_button = driver.find_element(By.ID, Const.LEAVING_BUTTON_ID)
        leaving_button_state = leaving_button.get_attribute('onclick')
        if is_quit:
            driver.quit()
        # 出勤ボタンが押せる状態
        if leaving_button_state != '':
            return True

        return False


    # 打刻自動化処理
    def ieyasu_attendance(self):
        last_timestamp = ''
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Const.ATTENDANCE_BUTTON_ID)))
            attendance_button = driver.find_element(By.ID, Const.ATTENDANCE_BUTTON_ID)
            # クリック処理
            attendance_button.click()
            # 日付取得
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
            last_timestamp = driver.find_element(By.ID, 'day').text + " " + driver.find_element(By.ID, 'time').text
            return last_timestamp
        except Exception as e:
            print("Ieyasu_Attendance_Error")

        finally:
            return last_timestamp

    def ieyasu_leaving(self):
        last_timestamp = ''
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Const.LEAVING_BUTTON_ID)))
            leaving_button = driver.find_element(By.ID, Const.LEAVING_BUTTON_ID)
            # クリック処理
            leaving_button.click()
            # 日付取得
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'time')))
            last_timestamp = driver.find_element(By.ID, 'day').text + " " + driver.find_element(By.ID, 'time').text
            return last_timestamp
        except Exception as e:
            print("Ieyasu_Leaving_Error")

        finally:
            return last_timestamp

    # ログイン自動化処理
    def ieyasu_login(self, user_info):
        try:
            # 現在URL判定
            if (driver.current_url == Const.IEYASU_TIMESTAMP_URL):
                return True
            else:
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
                # ログイン完了判定
                if (driver.current_url == Const.IEYASU_TIMESTAMP_URL):
                    return True
                else:
                    driver.quit()
                    return False
        except Exception as e:
            print("Ieyasu_Login_Error: " + str(e))

        return False
