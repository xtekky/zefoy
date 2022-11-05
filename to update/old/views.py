# import fade
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
import os
import io
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from datetime import datetime
from selenium import webdriver


def time():
    global current_time
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sleep(0.5)


def main():
    global driver
    global wait

    try:
        # selecting views
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button'))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/input'))).clear() #clearing input
    except:

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/p/small")))
            if ck.text == "soon will be update":
                print("[x | "+str(current_time)+"] Unavailable => Views", end="\r")
                sleep(999)
                captcha_ai()
            else:
                driver.refresh()
                main()
        except:
            pass
        print("[x | "+str(current_time)+"] HUH? ERROR")
        sleep(1)
        driver.refresh()
        sleep(5)
        captcha_ai()
    try:
        print(fade.water('[* | '+str(current_time)+'] Sending URL'), end="\r")
        sleep(0.1)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/input'))).send_keys(url)
        sleep(0.1)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/div/button'))).click()  # searching
        try:
            tv = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[5]/div/div/div[1]/div/form/button"))) #get views num on send button
            print(fade.brazil("[- | "+str(current_time)+"] Total views: " + tv.text), end="\r")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/div/div[1]/div/form/button'))).click()  # send views
        except:
            sleep(2)
            lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
            timer_message = lmt.text
            minutes = int(timer_message.split()[2])
            seconds = int(timer_message.split()[4])

            time_to_wait = (minutes * 60 + seconds)
            print("[* | "+str(current_time)+"] Waiting => ", time_to_wait, 'seconds')
            sleep(time_to_wait)
            main()
        main()
    except:
        try:
            driver.refresh()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button').click()
            main()
        except:
            captcha_ai()

def captcha_ai():
    driver.set_window_position(0, 0)
    print('[*] Solve Captcha')
    sleep(5)
    
    try:
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button').click()
        driver.refresh()
        print(fade.random("[* | " + str(current_time) + "] Boyzz, we are in!"), end="\r")
        driver.set_window_position(-10000, 0)
        main()
    except:
        captcha_ai()


if __name__ == "__main__":
    print(fade.purplepink(r'''
._______.______  ._______._______     .___     .___ ._______         ___ .________  TM
:_ ____/: __   \ : .____/: .____/     |   |___ : __|: .____/.___    |   ||    ___/  
|   _/  |  \____|| : _/\ | : _/\      |   |   || : || : _/\ :   | /\|   ||___    \
|   |   |   :  \ |   /  \|   /  \     |   :   ||   ||   /  \|   |/  :   ||       /
|_. |   |   |___\|_.: __/|_.: __/      \      ||   ||_.: __/|   /       ||__:___/ 
  :/    |___|       :/      :/          \____/ |___|   :/   |______/|___|   :     
  :                                                                 :             
                                                                    :             
'''))

    #start = input('[*] Type any key to start: ')
    url = input('[*] Url: ')

    opts = webdriver.ChromeOptions()
    driver = uc.Chrome(options=opts)
    driver.get('https://zefoy.com')
    wait = WebDriverWait(driver, 5)


    a = threading.Thread(target=time)
    b = threading.Thread(target=captcha_ai)

    a.start()
    b.start()
