import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def short_URL(long_url):
    options = Options()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=r'C:/chromedriver.exe', options=options)
    driver.get("https://bitly.com")  
    driver.find_element_by_id("shorten_url").send_keys(long_url)
    driver.execute_script("arguments[0].click();", driver.find_element_by_id('shorten_btn'))
    driver.get("https://www.google.com")    
    driver.execute_script("window.history.go(-1);")
    cookie = driver.get_cookie('anon_shortlinks')
    driver.close()   
    return str(cookie['value'])    

def main():
    long_url = str(input("Enter Long URL: "))
    if long_url[long_url.find("bit.ly"):14] == "bit.ly":
        print("URL is already shortened!")
    else:
        sh_url = short_URL(long_url)
        print("Shortened  URL: " + sh_url[8:len(sh_url)])       
                 
if __name__ == "__main__":
    main()
