from selenium import webdriver
from time import sleep 

class ScreenShoter:
    def screen(self,url):
        self.url=url
        DRIVER = "chromedriver.exe"
        driver = webdriver.Chrome(DRIVER)
        driver.get(url)
        sleep(2) 
        screenshot = driver.save_screenshot("my_screenshot.png")
        driver.quit()
        scr='my_screenshot.png'
        return scr

    #def parser_webdriver(self,url,element_css):
        driver_path = 'chromedriver.exe'
        browser = webdriver.Chrome(executable_path=driver_path)
        browser.get(url)
        #"div[class='name main-name']"
        item = browser.find_elements_by_css_selector(element_css)
        browser.close()
        print(item)
        return item
        