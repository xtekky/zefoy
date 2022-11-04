try:
    from selenium import webdriver
    from os import system, name
    from time import time, strftime, gmtime, sleep
    from selenium.webdriver.common.by import By
    import threading, warnings
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from pystyle import *
    import undetected_chromedriver as uc
    from datetime import datetime
    from selenium.webdriver.chrome.options import Options
except:
    print("ERROR - Importing modules, check if all requirements are installed")


"""
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
SOFTWARE."""

warnings.filterwarnings("ignore")


def timez():
    global current_time
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
        time_elapsed = strftime("%H:%M:%S", gmtime(time() - start))
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[* | " + str(current_time) + "] Loading silent driver",
                1,
            )
        )
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        chrome_options.headless = True
        driver = uc.Chrome(use_subprocess=True, options=chrome_options)
        driver.get("https://zefoy.com/")
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple, "[* | " + str(current_time) + "] Page loaded", 1
            )
        )
        driver.add_cookie({"name": "PHPSESSID", "value": value})
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[* | " + str(current_time) + "] Cookie injected",
                1,
            )
        )
        driver.refresh()
        wait = WebDriverWait(driver, 15)
        waits = WebDriverWait(driver, 3)
        # driver.set_window_size(1024, 480)
        try:
            waits.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[1]/div'))
            )
            print("[* | " + str(current_time) + "] Page loaded")
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
        return format(arg, ",d").replace(",", ".")

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
            time_elapsed = strftime("%H:%M:%S", gmtime(time() - start))
            system(
                f"title ZEFOY BOT V7 Github: @xtekky ^| Views: {beautify(Views)} ^| Hearts: {beautify(Hearts)} ^| Shares: {beautify(Shares)} ^| Elapsed Time: {time_elapsed}"
            )

    # Followers
    def loop0():
        global current_time
        global Followers

        try:
            ck = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/p/small")
                )
            )
            if ck.text == "soon will be update":
                print(
                    Colorate.Horizontal(
                        Colors.red_to_black,
                        "[x | " + str(current_time) + "] Unavailable => Followers",
                        1,
                    )
                )
                loop1()  # if it's being updated, continue right away
            else:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button",
                        )
                    )
                ).click()

        except:
            print("[- | " + str(current_time) + "] The captcha is unsolved! 1")
            sleep(10)
            driver.refresh()
            loop1()

        try:
            methodFollowers()
            sleep(3)
            driver.refresh()
            loop1()

        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[= | "
                        + str(current_time)
                        + "] Followers Timer: "
                        + timer_message,
                        1,
                    )
                )

                message_split = timer_message.split()

                if (
                    timer_message == "Checking Timer..."
                    or timer_message == "Next Submit: READY....!"
                ):
                    methodFollowers()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(
                            "[= | " + str(current_time) + "] Waiting:" + str(sleeping),
                            "s",
                        )
                        sleep(sleeping)
                        methodFollowers()
                    else:
                        print(
                            Colorate.Horizontal(
                                Colors.blue_to_purple,
                                "[x | " + str(current_time) + "] Skipping Followers..",
                                1,
                            )
                        )

                driver.refresh()
                loop1()

            except:
                try:
                    fn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='Not found video.']")
                        )
                    )
                    print("[x | " + str(current_time) + "] Not found video..")
                    methodFollowers()
                    sleep(3)
                    driver.refresh()
                    loop1()
                except:
                    print(
                        Colorate.Horizontal(
                            Colors.blue_to_purple,
                            "[- | "
                            + str(current_time)
                            + "] An error occurred. Skipping => Followers",
                            1,
                        )
                    )
                    sleep(0.5)
                    driver.refresh()
                    loop1()

    # Views
    def loop1():
        global current_time
        global Views

        try:
            ck = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/p/small")
                )
            )
            if ck.text == "soon will be update":
                print(
                    Colorate.Horizontal(
                        Colors.red_to_black,
                        "[x | " + str(current_time) + "] Unavailable => Views",
                        1,
                    )
                )
                loop2()  # if it's being updated, continue right away
            else:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button",
                        )
                    )
                ).click()
        except:
            print("[- | " + str(current_time) + "] The captcha is unsolved! 2")
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
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[= | " + str(current_time) + "] Views Timer: " + timer_message,
                        1,
                    )
                )

                message_split = timer_message.split()

                if (
                    timer_message == "Checking Timer..."
                    or timer_message == "Next Submit: READY....!"
                ):
                    methodView()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(
                            "[= | " + str(current_time) + "] Waiting:" + str(sleeping),
                            "s",
                        )
                        sleep(sleeping)
                        methodView()
                    else:
                        print(
                            Colorate.Horizontal(
                                Colors.blue_to_purple,
                                "[x | " + str(current_time) + "] Skipping Views..",
                                1,
                            )
                        )

                driver.refresh()
                loop2()

            except:
                try:
                    fn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='Not found video.']")
                        )
                    )
                    print("[x | " + str(current_time) + "] Not found video..")
                    methodView()
                    sleep(3)
                    driver.refresh()
                    loop2()
                except:
                    print(
                        Colorate.Horizontal(
                            Colors.blue_to_purple,
                            "[- | "
                            + str(current_time)
                            + "] An error occurred. Skipping => Views",
                            1,
                        )
                    )
                    sleep(3)
                    driver.refresh()
                    loop2()

    # Hearts
    def loop2():
        global current_time
        global Hearts

        try:
            ck = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/p/small")
                )
            )
            if ck.text == "soon will be update":
                print(
                    Colorate.Horizontal(
                        Colors.red_to_black,
                        "[x | " + str(current_time) + "] Unavailable => Hearts",
                        1,
                    )
                )
                loop3()  # if it's being updated, continue right away
            else:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button",
                        )
                    )
                ).click()

        except:
            print("[- | " + str(current_time) + "] The captcha is unsolved! 3")
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
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[= | "
                        + str(current_time)
                        + "] Hearts Timer: "
                        + timer_message,
                        1,
                    )
                )

                message_split = timer_message.split()

                if (
                    timer_message == "Checking Timer..."
                    or timer_message == "Next Submit: READY....!"
                ):
                    methodHearts()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(
                            "[= | " + str(current_time) + "] Waiting:" + str(sleeping),
                            "s",
                        )
                        sleep(sleeping)
                        methodHearts()
                    else:
                        print("[x | " + str(current_time) + "] Hearts Unavailable")

                driver.refresh()
                loop3()

            except:
                try:
                    fn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='Not found video.']")
                        )
                    )
                    print("[x | " + str(current_time) + "] Not found video..")
                    methodHearts()
                    sleep(3)
                    driver.refresh()
                    loop3()
                except:
                    print(
                        Colorate.Horizontal(
                            Colors.blue_to_purple,
                            "[- | "
                            + str(current_time)
                            + "] An error occurred. Skipping => Hearts",
                            1,
                        )
                    )
                    sleep(3)
                    driver.refresh()
                    loop3()

    # Shares
    def loop3():
        global current_time
        global Shares

        try:
            ck = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/p/small")
                )
            )
            if ck.text == "soon will be update":
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[x | " + str(current_time) + "] Unavailable => Shares",
                        1,
                    )
                )
                loop4()  # if it's being updated, continue right away
            else:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button",
                        )
                    )
                ).click()
        except:
            print("[- | " + str(current_time) + "] The captcha is unsolved! 4")
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
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[= | "
                        + str(current_time)
                        + "] Shares Timer: "
                        + timer_message,
                        1,
                    )
                )

                message_split = timer_message.split()

                if (
                    timer_message == "Checking Timer..."
                    or timer_message == "Next Submit: READY....!"
                ):
                    methodShare()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(
                            "[= | "
                            + str(current_time)
                            + "] Waiting: "
                            + str(sleeping)
                            + "s"
                        )
                        sleep(sleeping)
                        methodShare()
                    else:
                        print(
                            Colorate.Horizontal(
                                Colors.blue_to_purple,
                                f"[x | {str(current_time)}] Skipping Shares",
                                1,
                            )
                        )
                driver.refresh()
                loop4()
            except:
                try:
                    fn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='Not found video.']")
                        )
                    )
                    print("[x | " + str(current_time) + "] Not found video..")
                    methodShare()
                    sleep(3)
                    driver.refresh()
                    loop4()
                except:
                    print(
                        Colorate.Horizontal(
                            Colors.blue_to_purple,
                            "[- | "
                            + str(current_time)
                            + "] An error occurred. Skipping => Shares",
                            1,
                        )
                    )
                    sleep(3)
                    driver.refresh()
                    loop4()

    # comment hearts
    def loop4():
        global current_time
        global Username
        global Comments
        global total_comments
        global comments_num
        global number

        if number == int(comments_num):
            number = 0
        try:
            ck = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[3]/div/p/small")
                )
            )
            if ck.text == "soon will be update":
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[x | "
                        + str(current_time)
                        + "] Unavailable => Comments Hearts",
                        1,
                    )
                )
                loop0()  # if it's being updated, continue right away
            else:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button",
                        )
                    )
                ).click()
        except:
            print("[- | " + str(current_time) + "] The captcha is unsolved! 5")
            sleep(10)
            driver.refresh()
            loop4()
        try:
            methodComments()
            sleep(3)
            driver.refresh()
            loop0()
        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(
                    Colorate.Horizontal(
                        Colors.blue_to_purple,
                        "[= | "
                        + str(current_time)
                        + "] Comments Timer: "
                        + timer_message,
                        1,
                    )
                )
                message_split = timer_message.split()
                if (
                    timer_message == "Checking Timer..."
                    or timer_message == "Next Submit: READY....!"
                ):
                    methodComments()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(
                            "[= | " + str(current_time) + "] Waiting:" + str(sleeping),
                            "s",
                        )
                        sleep(sleeping)
                        methodComments()
                    else:
                        print(
                            Colorate.Horizontal(
                                Colors.blue_to_purple,
                                "[x | "
                                + str(current_time)
                                + "] Skipping Comment-Hearts..",
                                1,
                            )
                        )
                driver.refresh()
                loop0()
            except:
                try:
                    fn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//span[text()='Not found video.']")
                        )
                    )
                    print("[x | " + str(current_time) + "] Video Not Found..")
                    methodComments()
                    sleep(3)
                    driver.refresh()
                    loop0()
                except:
                    print(
                        Colorate.Horizontal(
                            Colors.blue_to_purple,
                            "[- | "
                            + str(current_time)
                            + "] An error occurred. Skipping => Comments Hearts",
                            1,
                        )
                    )
                    sleep(3)
                    driver.refresh()
                    loop0()

    def methodFollowers():
        global current_time
        global Followers

        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[N | " + str(current_time) + "] Getting TikTok link",
                1,
            )
        )
        # sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid"]/div/form/div/input'))
        ).clear()  # remove input
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid"]/div/form/div/input'))
        ).send_keys(
            vidUrl
        )  # input url
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="sid"]/div/form/div/div/button')
            )
        ).click()  # submit

        waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button',
                )
            )
        ).click()

        Followers += 25
        print(
            Colorate.Horizontal(
                Colors.green_to_white,
                "[+ | " + str(current_time) + "] Followers Sent!",
                1,
            )
        )
        driver.refresh()

    def methodView():
        global current_time
        global Views
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[N | " + str(current_time) + "] Getting TikTok link",
                1,
            )
        )
        # sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid4"]/div/form/div/input'))
        ).clear()  # remove input
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid4"]/div/form/div/input'))
        ).send_keys(
            vidUrl
        )  # input url
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="sid4"]/div/form/div/div/button')
            )
        ).click()  # submit
        sleep(2)
        tv = waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button',
                )
            )
        )
        print(
            Colorate.Horizontal(
                Colors.green_to_white,
                "[- | " + str(current_time) + "] Total views: " + tv.text,
                1,
            )
        )
        Views = int(tv.text.replace(",", ""))

        waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button',
                )
            )
        ).click()

        Views += 800
        print(
            Colorate.Horizontal(
                Colors.green_to_white, "[+ | " + str(current_time) + "] Views Sent!", 1
            )
        )

    def methodHearts():
        global current_time
        global Hearts

        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[N | " + str(current_time) + "] Getting TikTok link",
                1,
            )
        )

        # sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid2"]/div/form/div/input'))
        ).clear()  # remove input
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid2"]/div/form/div/input'))
        ).send_keys(
            vidUrl
        )  # input url
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="sid2"]/div/form/div/div/button')
            )
        ).click()  # submit
        sleep(2)
        th = waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button',
                )
            )
        )
        print(
            Colorate.Horizontal(
                Colors.green_to_white,
                "[- | " + str(current_time) + "] Total hearts: " + th.text,
                1,
            )
        )
        Hearts = int(th.text.replace(",", ""))
        waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button',
                )
            )
        ).click()
        print(
            Colorate.Horizontal(
                Colors.green_to_white, "[+ | " + str(current_time) + "] Hearts Sent!", 1
            )
        )

    def methodShare():
        global current_time
        global Shares
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[N | " + str(current_time) + "] Getting TikTok link",
                1,
            )
        )
        # sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid7"]/div/form/div/input'))
        ).clear()  # remove input
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid7"]/div/form/div/input'))
        ).send_keys(
            vidUrl
        )  # input url
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="sid7"]/div/form/div/div/button')
            )
        ).click()  # submit
        sleep(2)
        ts = waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button',
                )
            )
        )
        print(
            Colorate.Horizontal(
                Colors.green_to_white,
                "[- | " + str(current_time) + "] Total shares: " + ts.text,
                1,
            )
        )
        Shares = int(ts.text.replace(",", ""))
        waits.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button',
                )
            )
        ).click()
        print(
            Colorate.Horizontal(
                Colors.green_to_white, "[+ | " + str(current_time) + "] Shares Sent!", 1
            )
        )

    def methodComments():
        global current_time
        global Username
        global Comments
        global total_comments
        global comments_num
        global number
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[N | " + str(current_time) + "] Getting TikTok link",
                1,
            )
        )
        # sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid3"]/div/form/div/input'))
        ).clear()  # remove input
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sid3"]/div/form/div/input'))
        ).send_keys(
            vidUrl
        )  # input url
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="sid3"]/div/form/div/div/button')
            )
        ).click()  # submit
        sleep(2)
        tm = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button',
                )
            )
        )
        comments_num = tm.text
        print(
            Colorate.Horizontal(
                Colors.blue_to_purple,
                "[= | " + str(current_time) + "] Comments: " + comments_num,
                1,
            )
        )
        # sleep(1)
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button',
                )
            )
        ).click()
        sleep(2)
        if total_comments == int(comments_num):
            username_1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/span[1]",
                    )
                )
            )
            comment_1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/span[2]",
                    )
                )
            )
            comment_likes = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/div/span",
                    )
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.blue_to_purple,
                    "[? | "
                    + str(current_time)
                    + "] "
                    + username_1.text
                    + " : "
                    + comment_1.text
                    + " ["
                    + comment_likes.text
                    + " hearts]",
                    1,
                )
            )
            Comments = int(comment_likes.text.replace(",", ""))
            Username = str(username_1.text)
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/button",
                    )
                )
            ).click()
            number = int(comments_num)
            total_comments = 1

        else:
            username_1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/span[1]",
                    )
                )
            )
            comment_1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/span[2]",
                    )
                )
            )
            comment_likes = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/div/span",
                    )
                )
            )
            print(
                Colorate.Horizontal(
                    Colors.blue_to_purple,
                    "[? | "
                    + str(current_time)
                    + "] "
                    + username_1.text
                    + " : "
                    + comment_1.text
                    + " ["
                    + comment_likes.text
                    + " hearts]",
                    1,
                )
            )
            Comments = int(comment_likes.text.replace(",", ""))
            Username = str(username_1.text)
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form['
                        + str(total_comments)
                        + "]/ul/li/div/button",
                    )
                )
            ).click()
            number += 1
            total_comments += 1
        print(
            Colorate.Horizontal(
                Colors.green_to_white,
                "[+ | " + str(current_time) + "] Comments Hearts Sent!",
                1,
            )
        )

    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("Log:")
    """

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
    print(
        Colorate.Horizontal(
            Colors.blue_to_purple, "[* | " + str(current_time) + "] Complete captcha", 1
        )
    )
    try:
        WebDriverWait(browser, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button")
            )
        )
    except:
        print(
            Colorate.Horizontal(
                Colors.red_to_white,
                "[* | " + str(current_time) + "] Solve Captcha !!",
                1,
            )
        )
        sessid()
    print(
        Colorate.Horizontal(
            Colors.blue_to_purple,
            "[* | " + str(current_time) + "] Generating session ID...",
            1,
        )
    )
    browser.set_window_position(-10000, 0)
    id = browser.get_cookie("PHPSESSID")
    print(
        Colorate.Horizontal(
            Colors.blue_to_purple,
            "[* | " + str(current_time) + "] Session ID: " + id["value"],
            1,
        )
    )
    value = id["value"]
    browser.quit()
    main()


if __name__ == "__main__":
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    system("title TIKTOK BOT")

    title = """                                  ZEFOY BITCH"""

    print(Colorate.Horizontal(Colors.blue_to_purple, title, 1))
    print("\n")

    # url input
    Write.Print("[?] TikTok URL ↓\n", Colors.blue_to_purple, interval=0.001)
    vidUrl = Write.Input(" >  ", Colors.blue_to_purple, interval=0.5, hide_cursor=True)

    # credits
    print(" ")
    print(" ")
    Write.Print(
        "                 * Thanks for using our Tool, Full credits to > Tekky#9999 | t.me/xtekky | .gg/onlp *\n",
        Colors.red_to_white,
        interval=0.01,
    )
    print(" ")
    print(" ")

    sleep(2.5)
    Views = 0

    t = threading.Thread(target=timez)
    t.start()
    global value
    global current_time
    chrome_options = Options()
    browser = uc.Chrome(options=chrome_options)
    browser.set_window_size(900, 1080)
    browser.get("https://zefoy.com/")

    sessid()
