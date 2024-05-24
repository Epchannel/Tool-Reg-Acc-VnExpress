from selenium import webdriver

driver=webdriver.Chrome()


# Mở các tab theo yêu cầu
driver.execute_script("window.open('https://bom.so/lNhZsq')")
driver.execute_script("window.open('https://gmail.com')")
time.sleep(2)  # Đợi các tab mở xong

# Chuyển đến tab 1 (chỉ mục 0)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)  # Đợi tab load xong
