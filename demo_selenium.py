from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Đường dẫn đến WebDriver
driver_path = "E:\\EPCHANNEL\\Tool\\chromedriver.exe"
extension_dir1 = "E:\\EPCHANNEL\\Tool\\CFHDOJBKJHNKLBPKDAIBDCCDDILIFDDB_4_0_0_0"  # Thay đổi đường dẫn này bằng đường dẫn thư mục của extension thứ nhất
extension_dir2 = "E:\\EPCHANNEL\\Tool\\HLIFKPHOLLLIJBLKNNMBFAGNKJNEAGID_0_1_6_0" 
service = Service(executable_path=driver_path)

# Cấu hình tùy chọn cho Chrome
chrome_options = Options()
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
chrome_options.add_argument(f"--load-extension={extension_dir1},{extension_dir2}")
chrome_options.add_argument("--disable-notifications")  # Từ chối tất cả các yêu cầu thông báo

# Tạo đối tượng WebDriver cho Chrome với các tùy chọn đã cấu hình
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
# Đọc dữ liệu từ file
    with open('E:\\EPCHANNEL\\Tool\\acc.txt', 'r') as file:
        account_info = file.readline().strip()
    tai_khoan, mat_khau = account_info.split('|')


    time.sleep(10)
    all_handles = driver.window_handles
    initial_handle = driver.current_window_handle  # Lưu handle của tab đầu tiên

    # Kiểm tra và đóng các tab không mong muốn, giữ lại tab ban đầu
    for handle in all_handles:
        if handle != initial_handle:
            driver.switch_to.window(handle)
            driver.close()

    # Chuyển về tab ban đầu
    driver.switch_to.window(initial_handle)

    # Bước 1: Mở URL và đợi 10 giây để trang web tải xong
    driver.get("https://bom.so/lNhZsq")
    time.sleep(10)  # Đợi để trang tải xong

    # Bước 2: Click vào element dựa trên full XPath
    first_button = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/a/span")
    first_button.click()
    time.sleep(5)  

    # Chuyển đến iframe
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe.iframe_guest")
    driver.switch_to.frame(iframe)

    # Bước 3: Click vào element trong iframe
    element_in_iframe = driver.find_element(By.XPATH, "/html/body/form/div/div[1]/a[2]")
    element_in_iframe.click()
    time.sleep(5)  

    # Bước tiếp theo: Click vào full xpath tiếp theo
    next_element_to_click = driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/input")
    next_element_to_click.click()

    xpath_username = "/html/body/form/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/input"
    xpath_password = "/html/body/form/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input"

    input_username = driver.find_element(By.XPATH, xpath_username)
    input_password = driver.find_element(By.XPATH, xpath_password)

    input_username.send_keys(tai_khoan)
    time.sleep(5)
    input_password.send_keys(mat_khau)
    time.sleep(5) 

    # login_button_xpath = "/html/body/form/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/button"
    # login_button = driver.find_element(By.XPATH, login_button_xpath)
    # login_button.click()

    
    # Đợi và quan sát hành động, không đóng trình duyệt ngay
    input("Press Enter to close the browser...") 

finally:
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.quit()  # Đóng trình duyệt sau khi nhấn Enter
