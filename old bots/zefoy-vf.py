from selenium import webdriver
from os import system, name
from time import time, strftime, gmtime, sleep
from selenium.webdriver.common.by import By
import threading, warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import os
import undetected_chromedriver as uc
from datetime import datetime


'''
Copyright (c) 2022 @xtekky

NO Permission is hereby granted, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software, including limitation of the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to forbid persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

warnings.filterwarnings("ignore")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title TIKTOK BOT')

print("""
███████╗███████╗███████╗ ██████╗ ██╗   ██╗    ██████╗  ██████╗ ████████╗    ██╗   ██╗███████╗ ██╗ TM
╚══███╔╝██╔════╝██╔════╝██╔═══██╗╚██╗ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝    ██║   ██║╚════██║███║
  ███╔╝ █████╗  █████╗  ██║   ██║ ╚████╔╝     ██████╔╝██║   ██║   ██║       ██║   ██║    ██╔╝╚██║
 ███╔╝  ██╔══╝  ██╔══╝  ██║   ██║  ╚██╔╝      ██╔══██╗██║   ██║   ██║       ╚██╗ ██╔╝   ██╔╝  ██║
███████╗███████╗██║     ╚██████╔╝   ██║       ██████╔╝╚██████╔╝   ██║        ╚████╔╝    ██║██╗██║
╚══════╝╚══════╝╚═╝      ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝         ╚═══╝     ╚═╝╚═╝╚═╝
F O L L O W E R S  -  E D I T I O N ™

Credits to Github: @xtekky
""")

#vidUrl = input("TikTok video URL: ")
vidUrl = 'https://www.tiktok.com/@MS4wLjABAAAAvjtzh7vjUGUzfdb77HHRiXWvXjXZFP-p97eBc94uZP50SxU6bR4bk9_s3tCh7M7w/video/7076804155981024517?is_from_webapp=1&sender_device=pc&web_id=7062836892223768069'

#PATH = input('Input Chromedriver path: ')


def timez():
    global current_time
    print("[*] Time Started")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sleep(0.5)


def main():
    global value
    global Views
    global Hearts
    global Shares
    global Comments
    global total_comments
    global comments_num
    global number
    global Username
    global current_time

    if vidUrl:
        start = time()
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        print("[* | "+str(current_time)+"] Loading silent driver")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chromedriver_autoinstaller.install()  # installing auto chromedriver
        chrome_options.headless = True
        driver = uc.Chrome(use_subprocess=True, options=chrome_options)
        driver.get("https://zefoy.com/")
        print("[* | "+str(current_time)+"] Page loaded")
        driver.add_cookie({"name": "PHPSESSID", "value": value})
        print("[* | "+str(current_time)+"] Cookie injected")
        driver.refresh()
        wait = WebDriverWait(driver, 15)
        waits = WebDriverWait(driver, 3)
        #driver.set_window_size(1024, 480)
        try:
            waits.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[1]/div')))
            print("[* | "+str(current_time)+"] Page loaded")
        except:
            pass

        Views = 0
        Hearts = 0
        Shares = 0
        Comments = 0
        total_comments = 1
        comments_num = 0
        number = 0
        Username = "@Anonymous"


    def beautify(arg):
        return format(arg, ',d').replace(',', '.')


    def title():  # Update the title IF option 1 was picked.
        global Views
        global Hearts
        global Shares
        global Comments
        global Username
        global number
        global comments_num
        global Followers

        while True:
            time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
            system(f'title ZEFOY BOT Follower version Github: @xtekky ')


    #Followers
    def loop0():
        global current_time
        global Followers

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/p/small')))
            if ck.text == "soon will be update":
                print("[x | "+str(current_time)+"] Followers are unavailable for now! - DM Discord: xtekky#9031 for cheap tiktok followers, fast and efficient")
                print("[x | "+str(current_time)+"] Waiting 10min")
                sleep(600)
                loop0()  # if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button'))).click()

        except:
            print("[- | "+str(current_time)+"] The captcha is unsolved!")
            sleep(10)
            driver.refresh()
            sessid()

        try:
            methodFollowers()
            sleep(3)
            driver.refresh()
            loop0()

        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print("[= | "+str(current_time)+"] Followers Timer: " + timer_message)

                message_split = timer_message.split()

                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodFollowers()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if timer:
                        sleeping = timer2 + 1
                        print("[= | "+str(current_time)+"] Waiting: " + str(sleeping), 'for next follow')
                        sleep(sleeping)
                        methodFollowers()
                    else:
                        print("[x | "+str(current_time)+"] Skipping Followers..")

                driver.refresh()
                loop0()

            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print("[x | "+str(current_time)+"] Not found video..")
                    methodFollowers()
                    sleep(3)
                    driver.refresh()
                    loop0()
                except:
                    print("[- | "+str(current_time)+"] An error occurred. Skipping => Followers")
                    sleep(0.5)
                    driver.refresh()
                    loop0()




    def methodFollowers():
        global current_time
        global Followers

        print("[N | "+str(current_time)+"] Getting TikTok link")
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid"]/div/form/div/input'))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid\"]/div/form/div/input"))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid\"]/div/form/div/div/button"))).click()  # submit

        waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button"))).click()

        Followers = Followers + 25
        print("[+ | "+str(current_time)+"] Followers Sent! - total:", Followers)
        driver.refresh()


    clear()
    print("Log:")

    if int(len(vidUrl)) >= 20:
        driver.get("https://zefoy.com/")

        a = threading.Thread(target=title)
        b = threading.Thread(target=loop0)

        a.start()
        b.start()

    else:
        print(f"{vidUrl} => URL is invalid!")


def sessid():
    global value
    global current_time
    t = threading.Thread(target=timez)
    t.start()
    if os.path.isfile('key.txt'):
        os.remove("key.txt")
        e = open("key.txt", "w+")
    else:
        e = open("key.txt", "w+")
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(900, 1080)
    browser.get("https://zefoy.com/")
    print("[* | "+str(current_time)+"] Complete captcha")
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button')))
    print("[* | "+str(current_time)+"] Generating session ID...")
    browser.set_window_position(-10000, 0)
    id = browser.get_cookie('PHPSESSID')
    f = open('key.txt', 'a+')
    f.write(id['value'])
    print("[* | "+str(current_time)+"] Session ID: " + id['value'])
    value = id['value']
    browser.quit()
    main()
sessid()
