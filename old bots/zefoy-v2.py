from selenium import webdriver
from os import system, name
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import warnings
'''
Copyright (c) 2022 @xtekky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
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
███████╗███████╗███████╗ ██████╗ ██╗   ██╗    ██████╗  ██████╗ ████████╗
╚══███╔╝██╔════╝██╔════╝██╔═══██╗╚██╗ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
  ███╔╝ █████╗  █████╗  ██║   ██║ ╚████╔╝     ██████╔╝██║   ██║   ██║   
 ███╔╝  ██╔══╝  ██╔══╝  ██║   ██║  ╚██╔╝      ██╔══██╗██║   ██║   ██║   
███████╗███████╗██║     ╚██████╔╝   ██║       ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚═╝      ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                           
Credits to Github: @xtekky""")

vidUrl = input("TikTok video URL: ")

if vidUrl:
    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(r"C:/chromedriver.exe", options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Shares = 0
    Comments = 0
    totalKomen = 1
    jumlah_komentar = 0
    keBerapa = 0
    Username = "@Anonymouse"


def beautify(arg):
    return format(arg, ',d').replace(',', '.')


def title():  # Update the title IF option 1 was picked.
    global Views
    global Hearts
    global Shares
    global Comments
    global Username
    global keBerapa
    global jumlah_komentar

    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(
            f'title TIKTOK BOT ^| Views: {beautify(Views)} ^| Hearts: {beautify(Hearts)} ^| Shares: {beautify(Shares)} ^| Comments Hearts: {(Username)} [{beautify(Comments)}] = Comments {str(keBerapa)} of {str(jumlah_komentar)} ^|  Elapsed Time: {time_elapsed}')


def loop1():
    global Views

    try:
        ck = driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/p/small")
        if ck.text == "soon will be update":
            print("[x] Soon will be update! => Views")
            loop2()  # jika sedang update langsung lanjut
        else:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()

    except:
        print("[-] The captcha is unsolved!")
        sleep(10)
        driver.refresh()
        loop1()

    try:
        methodView()
        sleep(3)
        driver.refresh()
        loop2()

    except:
        try:
            lmt = driver.find_element_by_css_selector("h4")
            limitnya = lmt.text
            print("[=] Message: " + limitnya)

            splitDong = limitnya.split()

            if limitnya == "Checking Timer..." or limitnya == "Next Submit: READY....!":
                methodView()
            elif splitDong[4].isnumeric():
                menit = int(splitDong[2])
                detik = int(splitDong[4])

                if (menit == 0) and (detik <= 10):
                    sleeping = detik + 1
                    print("[=] Sleep: " + str(sleeping))
                    sleep(sleeping)
                    methodView()
                else:
                    print("[x] Skip the fitur views..")

            driver.refresh()
            loop2()

        except:
            try:
                fn = driver.find_element_by_xpath("//span[text()='Not found video.']")
                print("[x] Not found video..")
                methodView()
                sleep(3)
                driver.refresh()
                loop2()
            except:
                print("[-] An error occured. Skip this step => Views")
                sleep(3)
                driver.refresh()
                loop2()


def loop2():
    global Hearts

    try:
        ck = driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[2]/div/p/small")
        if ck.text == "soon will be update":
            print("[x] Soon will be update! => Hearts")
            loop3()  # jika sedang update langsung lanjut
        else:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()

    except:
        print("[-] The captcha is unsolved!")
        sleep(10)
        driver.refresh()
        loop2()

    try:
        methodHearts()
        sleep(3)
        driver.refresh()
        loop3()

    except:
        try:
            lmt = driver.find_element_by_css_selector("h4")
            limitnya = lmt.text
            print("[=] Message: " + limitnya)

            splitDong = limitnya.split()

            if limitnya == "Checking Timer..." or limitnya == "Next Submit: READY....!":
                methodHearts()
            elif splitDong[4].isnumeric():
                menit = int(splitDong[2])
                detik = int(splitDong[4])

                if (menit == 0) and (detik <= 10):
                    sleeping = detik + 1
                    print("[=] Sleep: " + str(sleeping))
                    sleep(sleeping)
                    methodHearts()
                else:
                    print("[x] Skip the fitur heart..")

            driver.refresh()
            loop3()

        except:
            try:
                fn = driver.find_element_by_xpath("//span[text()='Not found video.']")
                print("[x] Not found video..")
                methodHearts()
                sleep(3)
                driver.refresh()
                loop3()
            except:
                print("[-] An error occured. Skip this step => Hearts")
                sleep(3)
                driver.refresh()
                loop3()

def loop3():
    global Shares

    try:
        ck = driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[5]/div/p/small")
        if ck.text == "soon will be update":
            print("[x] Soon will be update! => Shares")
            loop4()  # jika sedang update langsung lanjut
        else:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("[-] The captcha is unsolved!")
        sleep(10)
        driver.refresh()
        loop3()
    try:
        methodShare()
        sleep(3)
        driver.refresh()
        loop4()
    except:
        try:
            lmt = driver.find_element_by_css_selector("h4")
            limitnya = lmt.text
            print("[=] Message: " + limitnya)

            splitDong = limitnya.split()

            if limitnya == "Checking Timer..." or limitnya == "Next Submit: READY....!":
                methodShare()
            elif splitDong[4].isnumeric():
                menit = int(splitDong[2])
                detik = int(splitDong[4])

                if (menit == 0) and (detik <= 10):
                    sleeping = detik + 1
                    print("[=] Sleep: " + str(sleeping))
                    sleep(sleeping)
                    methodShare()
                else:
                    print("[x] Skip the fitur shares..")
            driver.refresh()
            loop4()
        except:
            try:
                fn = driver.find_element_by_xpath("//span[text()='Not found video.']")
                print("[x] Not found video..")
                methodShare()
                sleep(3)
                driver.refresh()
                loop4()
            except:
                print("[-] An error occured. Skip this step => Shares")
                sleep(3)
                driver.refresh()
                loop4()

def loop4():
    global Username
    global Comments
    global totalKomen
    global jumlah_komentar
    global keBerapa
    
    if keBerapa == int(jumlah_komentar):
        keBerapa = 0
    try:
        ck = driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[3]/div/p/small")
        if ck.text == "soon will be update":
            print("[x] Soon will be update! => Comments Hearts")
            loop1()  # jika sedang update langsung lanjut
        else:
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("[-] The captcha is unsolved!")
        sleep(10)
        driver.refresh()
        loop4()
    try:
        methodComments()
        sleep(3)
        driver.refresh()
        loop1()
    except:
        try:
            lmt = driver.find_element_by_css_selector("h4")
            limitnya = lmt.text
            print("[=] Message: " + limitnya)
            splitDong = limitnya.split()
            if limitnya == "Checking Timer..." or limitnya == "Next Submit: READY....!":
                methodComments()
            elif splitDong[4].isnumeric():
                menit = int(splitDong[2])
                detik = int(splitDong[4])

                if (menit == 0) and (detik <= 10):
                    sleeping = detik + 1
                    print("[=] Sleep: " + str(sleeping))
                    sleep(sleeping)
                    methodComments()
                else:
                    print("[x] Skip the fitur comment hearts..")
            driver.refresh()
            loop1()
        except:
            try:
                fn = driver.find_element_by_xpath("//span[text()='Not found video.']")
                print("[x] Not found video..")
                methodComments()
                sleep(3)
                driver.refresh()
                loop1()
            except:
                print("[-] An error occured. Skip this step => Comments Hearts")
                sleep(3)
                driver.refresh()
                loop1()

def methodView():
    global Views
    print("[N] Getting link: ", vidUrl)
    # sleep(1)
    driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").clear()  # remove input
    driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)  # input url
    driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()  # submit
    sleep(2)
    tv = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button")
    print("[-] Total views: " + tv.text)
    Views = int(tv.text.replace(',', ''))

    driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()

    # Views += 1000
    print("[+] Views sended!")

def methodHearts():
    global Hearts

    print("[N] Getting link: ", vidUrl)

    # sleep(1)
    driver.find_element_by_xpath("//*[@id=\"sid2\"]/div/form/div/input").clear()  # remove input
    driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(vidUrl)  # input url
    driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()  # submit
    sleep(2)
    th = driver.find_element_by_xpath("//*[@id=\"c2VuZE9nb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button")
    print("[-] Total hears: " + th.text)
    Hearts = int(th.text.replace(',', ''))
    driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
    print("[+] Hearts sended!")

def methodShare():
    global Shares
    print("[N] Getting link: ", vidUrl)
    # sleep(1)
    driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/input").clear()  # remove input
    driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/input").send_keys(vidUrl)  # input url
    driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/div/button").click()  # submit
    sleep(2)
    ts = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button")
    print("[-] Total share: " + ts.text)
    Shares = int(ts.text.replace(',', ''))
    driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click()
    print("[+] Shares sended!")

def methodComments():
    global Username
    global Comments
    global totalKomen
    global jumlah_komentar
    global keBerapa
    print("[N] Getting link: ", vidUrl)
    # sleep(1)
    driver.find_element_by_xpath("//*[@id=\"sid3\"]/div/form/div/input").clear()  # remove input
    driver.find_element_by_xpath("//*[@id=\"sid3\"]/div/form/div/input").send_keys(vidUrl)  # input url
    driver.find_element_by_xpath("//*[@id=\"sid3\"]/div/form/div/div/button").click()  # submit
    sleep(2)
    tm = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button")
    jumlah_komentar = tm.text
    print("[=] Get number of comments: " + jumlah_komentar)
    # sleep(1)
    driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click()
    sleep(2)
    if totalKomen == int(jumlah_komentar):
        usernamenya = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/span[1]")
        komentarnya = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/span[2]")
        counlovenya = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/div/span")
        print("[?] " + usernamenya.text + " : " + komentarnya.text + " [" + counlovenya.text + " hearts]")
        Comments = int(counlovenya.text.replace(',', ''))
        Username = str(usernamenya.text)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/button").click()
        keBerapa = int(jumlah_komentar)
        totalKomen = 1

    else:
        usernamenya = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/span[1]")
        komentarnya = driver.find_element_by_xpath( "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/span[2]")
        counlovenya = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/div/span")
        print("[?] " + usernamenya.text + " : " + komentarnya.text + " [" + counlovenya.text + " hearts]")
        Comments = int(counlovenya.text.replace(',', ''))
        Username = str(usernamenya.text)

        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(totalKomen) + "]/ul/li/div/button").click()
        keBerapa += 1
        totalKomen += 1
    print("[+] Comments Hearts sended!")
clear()
print("Log:")

if int(len(vidUrl)) >= 20:
    driver.get("https://zefoy.com/")

    a = threading.Thread(target=title)
    b = threading.Thread(target=loop1)

    a.start()
    b.start()

else:
    print(f"{vidUrl} => URL is invalid!")
