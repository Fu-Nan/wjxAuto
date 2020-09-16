from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import pyautogui


class VerificationCode:

    def keyboard_1(self):
        action_1 = ActionChains(self.driver)
        action_1.key_down(Keys.DOWN)
        action_1.key_down(Keys.ENTER)
        action_1.perform()

    def keyboard_2(self):
        action_2 = ActionChains(self.driver)
        action_2.key_down(Keys.DOWN)
        action_2.key_down(Keys.DOWN)
        action_2.key_down(Keys.ENTER)
        action_2.perform()

    def __init__(self):
        option = ChromeOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Chrome()
        # self.find_element = self.driver.find_element_by_css_selector
        self.driver.get('https://www.wjx.top/wjx/Join/VerifyPasswordMobile2.aspx?q=54772724&pwx=&returnUrl=%2fm%2f54772724.aspx')  # 打开登陆页面
        # 登录页面
        self.driver.maximize_window()  # 全屏显示
        self.driver.find_element_by_name("txtPassword").send_keys("1831607119")
        self.driver.find_element_by_id("btnContinue").click()
        # 选项1
        self.driver.find_element_by_id("select2-q1-container").click()
        time.sleep(1)
        self.keyboard_2()
        # 选项2
        self.driver.find_element_by_id("select2-q2-container").click()
        self.keyboard_1()
        # 选项3
        self.driver.find_element_by_id("q3").send_keys("18725975538")
        # 选项4
        self.driver.find_element_by_class_name("getLocalBtn").click()
        time.sleep(5)
        # 选项5
        self.driver.find_element_by_id("select2-q5-container").click()
        self.keyboard_2()
        # 选项6
        self.driver.find_element_by_id("select2-q16_0_0-container").click()
        self.keyboard_2()
        # 选项7
        self.driver.find_element_by_id("select2-q16_0_1-container").click()
        self.keyboard_2()
        # 选项8
        self.driver.find_element_by_id("select2-q16_0_2-container").click()
        self.keyboard_2()
        # 选项9
        self.driver.find_element_by_id("select2-q17-container").click()
        self.keyboard_1()
        # 选项10
        self.driver.find_element_by_id("select2-q18-container").click()
        self.keyboard_2()
        # 选项11
        self.driver.find_element_by_id("select2-q19-container").click()
        self.keyboard_2()
        # 表单提交
        self.driver.find_element_by_id("ctlNext").click()
        # 智能验证
        self.driver.find_element_by_id("rectMask").click()  # 点击按钮
        time.sleep(5)
        # 滑块
        pyautogui.click(819, 832, button="left")
        pyautogui.mouseDown()
        pyautogui.moveTo(1092, 835, duration=2)
        pyautogui.mouseUp()


if __name__ == '__main__':
    a = VerificationCode()
