from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Khởi tạo WebDriver
driver_path = r'E:\EPCHANNEL\Tool\chromedriver.exe'
driver = webdriver.Chrome(driver_path)

# Mở các tab theo yêu cầu
driver.execute_script("window.open('https://bom.so/lNhZsq')")
driver.execute_script("window.open('https://gmail.com')")
time.sleep(2)  # Đợi các tab mở xong

# Chuyển đến tab 1 (chỉ mục 0)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)  # Đợi tab load xong

# Thực hiện click theo yêu cầu ở tab 1
driver.find_element_by_xpath("/html/body/section[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/a").click()
time.sleep(5)  # Đợi 5 giây theo yêu cầu
driver.find_element_by_xpath("/html/body/form/div/div[1]/a[2]").click()

# Đọc dữ liệu từ file Excel
data = pd.read_excel('acc.xlsx')

# In dữ liệu để kiểm tra
print(data)

# Tiếp tục xử lý dữ liệu nếu cần
# ...

# Đóng trình duyệt
# driver.quit()
