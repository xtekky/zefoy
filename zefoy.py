import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#vidUrl = input("TikTok Link: ")
vidUrl = 'https://www.tiktok.com/@repl1c4.world/video/7075744934300601605?is_from_webapp=1&sender_device=pc&web_id=7062786503562774021'


def captcha():
    print('\n')
    print('[*] - Github: @xtekky')
    print('[*] - Starting...')
    print('[*] - Solve Captcha')
    sleep(9)
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]")
        print('[*] - Captcha Solved')
        mode2()
    except:
        driver.refresh()
        captcha()

# -- V I E W S --
def loop1():
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[4]/div/button'))).click()  # selecting views
    except:
        print('[ERROR 0] - Failed selecting views')
        driver.refresh()
        loop1()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid4"]/div/form/div/input'))).send_keys(vidUrl) #pasting URL
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid4"]/div/form/div/div/button'))).click() #confirm
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'))).click()
        sleep(2)
        driver.refresh()
        print("\r", end="")
        print("[*] Sucess Views")
        print("\r")
        loop1()
    except:
        print("\r", end="")
        print('[ERROR 1] Timer On', end="")
        driver.refresh()
        sleep(3)
        loop1()

# -- C O M M E N T | H E A R T S --
def loop3():
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[3]/div/button'))).click() # selecting comment hearts
    except:
        print('[ERROR 0] - Failed selecting Comment Hearts')
        driver.refresh()
        loop3()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid3"]/div/form/div/input'))).send_keys(vidUrl)  # pasting URL
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid3"]/div/form/div/div/button'))).click()  # confirm
        waitl.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button'))).click()  # send comment hearts
        sleep(2)
        driver.refresh()
        print("[*] Sucess Comment Likes")
        loop3()
    except:
        print("\n", end="")
        print('[ERROR 1] Timer On', end="")
        driver.refresh()
        loop3()

# -- S H A R E S --
def loop5():
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[5]/div/button'))).click() # selecting shares
    except:
        print('[ERROR 0] - Failed selecting Comment Hearts')
        driver.refresh()
        loop5()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid7"]/div/form/div/input'))).send_keys(vidUrl)  # pasting URL
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid7"]/div/form/div/div/button'))).click()  # confirm
        waitl.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button'))).click()  # send shares
        sleep(2)
        driver.refresh()
        print("[*] Sucess Shares")
        loop5()
    except:
        print("\n", end="")
        print('[ERROR 1] Timer On', end="")
        driver.refresh()
        loop5()


def mode2():
    global bot

    if bot == 1:
        loop1() #views
    elif bot == 2:
        loop5() #share
    elif bot == 3:
        loop3() #heart comments

def mode():
    global bot

    if bot == 1:
        captcha()
    elif bot == 2:
        captcha()
    elif bot == 3:
        captcha()
    else:
        print("[ERROR 0] - Check input")
        mode()

def start():
    global bot
    global wait
    global waitl
    global driver

    chrome_options = webdriver.ChromeOptions()
    bot = int(input("[1] - Views\n[2] - Shares\n[3] - Comments Likes\n[UNAVAILABLE] - Likes\n[UNAVAILABLE] - Auto followers\nSelect: "))
    driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)
    wait = WebDriverWait(driver, 10)
    waitl = WebDriverWait(driver, 1999)
    driver.get("https://vipto.de/")
    mode()

if __name__ == "__main__":
    start()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-extensions')
    driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)

