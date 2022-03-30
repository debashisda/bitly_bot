import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    long_url = str(input("Enter Long URL: "))
    global driver
    driver = webdriver.Chrome(executable_path=r'C:/chromedriver.exe')
    driver.get("https://bitly.com")  
    driver.find_element_by_id("shorten_url").send_keys(long_url)  
    driver.find_element_by_id("shorten_btn").click()
    driver.get("https://www.google.com")
    driver.execute_script("window.history.go(-1)")
    cookie = driver.get_cookie('anon_shortlinks')
    print("Shortened URL: " + cookie['value'])
    driver.close()
                 
if __name__ == "__main__":
    main()
