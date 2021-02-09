import time
import schedule
import encr
import socket
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def mainfunc():
    def is_connected(hostname):
        try:
            host = socket.gethostbyname(hostname)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:
            pass
        return False

    # Here we use encry.py to decrypt all the usernames and password
    print('Decrypting Username')
    usernameStr = encr.username_plain()
    usernameAcademia = encr.username_aca_plain()
    print('Username Decrypted')
    print('Decrypting Password')
    passwordAcademia = encr.password_aca_plain()
    passwordStr = encr.password_plain()
    print('Password Decrypted')
    login_link = 'https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/'
    
    options = Options()
    options.add_argument('--disable-infobars')
    options.set_preference("permissions.default.microphone", 1)
    options.set_preference("permissions.default.camera", 1)
    driver = webdriver.Firefox(options=options,
                               executable_path=r'D:\Projects\Google Meet Attendance Bot')
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)

    REMOTE_SERVER = "1.1.1.1"

    firstC = "09:00"
    secondC = "09:50"
    thirdC = "10:50"
    fourthC = "11:40"
    fifthC = "12:30"
    sixthC = "13:20"
    seventhC = "14:10"
    eightC = "15:00"

    pcb_mnd = 'https://meet.google.com/lookup/'
    seminar_2 = 'https://meet.google.com/lookup/'
    employability = 'https://meet.google.com/lookup/'
    maths = 'https://meet.google.com/lookup/'
    oops = 'https://meet.google.com/lookup/'
    prof_skills = 'https://meet.google.com/lookup/'
    smart_grid = 'https://meet.google.com/lookup/'
    indian_art_form = 'https://meet.google.com/lookup/'
    microcontrollers = 'https://meet.google.com/lookup/'
    power_system_protection = 'https://meet.google.com/lookup/'
    comprehension = 'https://meet.google.com/lookup/'

    print('___________Initialization Complete___________')

    def disable_cam_mic_and_join():
        video = driver.find_element_by_css_selector('.GOH7Zb')
        mic = driver.find_element_by_css_selector('.ZB88ed')
        join_now = driver.find_element_by_css_selector('div.uArJ5e:nth-child(1)')
        video.click()
        mic.click()
        time.sleep(2)
        join_now.click()


    def load_page(url, meetlnk=True):
        if meetlnk:
            time.sleep(1)
            driver.get(url)
            time.sleep(2)
            disable_cam_mic_and_join()
        else:
            driver.get(url)

    def login_mn():
        print("Loading Academia")
        driver.get('https://academia.srmist.edu.in/#Page:WELCOME')
        driver.switch_to.frame(0)
        w = WebDriverWait(driver, 10)
        try:
            w.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn')))
        except TimeoutError:
            print("Timed out")

        print("Waited for 10s")
        print("Switching to inner frame")

        print("Entering email and password")
        driver.find_element_by_id('Email').send_keys(usernameAcademia)
        driver.find_element_by_id("Password").send_keys(passwordAcademia)
        print("Logging In")
        driver.find_element_by_class_name("btn").click()
        driver.switch_to.parent_frame()
        try:
            w.until(ec.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.highlight:nth-child(4) > strong:nth-child(1) > font')))
        except TimeoutError:
            print("Timed out")
        print("Logged In")
        dorr = driver.find_element_by_css_selector('span.highlight:nth-child(4) > strong:nth-child(1) > font').text
        if dorr == 'Day Order:No Day Order':
            dorr = 0
        else:
            dorr = dorr[len(dorr) - 1]

        print('Day Order: ' + str(dorr))
        print('___________End Day Order Detection___________')
        return int(dorr)

    def login_g():
        print('Loading Google Sign In Page')
        load_page(login_link, False)
        username = driver.find_element_by_id('identifierId')
        print('Sending Username')
        username.send_keys(usernameStr)
        next_button = driver.find_element_by_id('identifierNext')
        print('Next')
        next_button.click()
        wttm = 2
        print('Waiting ' + str(wttm) + ' seconds')
        time.sleep(2)
        password = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        print('Sending Password')
        password.send_keys(passwordStr)
        sign_in_button = driver.find_element_by_id('passwordNext')
        print('Attempting Sign-In')
        sign_in_button.click()
        wttm = 5
        print('Waiting ' + str(wttm) + ' seconds')
        time.sleep(5)
        print('___________End Google Login___________')

    def smartgrid():
        print('Loading Smart Grid Class')
        load_page(smart_grid)

    def oopss():
        print('Loading Principles of OOPS Class')
        load_page(oops)

    def pcb_m():
        print('Loading PCB Design and Manufacturing Class')
        load_page(pcb_mnd)

    def seminar():
        print('Loading Seminar-II Class')
        load_page(seminar_2)

    def employ():
        print('Loading Employability Class')
        load_page(employability)

    def math():
        print('Loading Math Class')
        load_page(maths)

    def prof_sk():
        print('Loading Professional Skills Class')
        load_page(prof_skills)

    def indian_art():
        print('Loading Indian Art Class')
        load_page(indian_art_form)

    def microcontrol():
        print('Loading Microcontrollers Class')
        load_page(microcontrollers)

    def powersp():
        print('Loading Power System Protection Class')
        load_page(power_system_protection)

    def compre():
        print('Loading Comprehension Class')
        load_page(comprehension)

    def do_1():
        print('exec DO 1')
        schedule.every().day.at(firstC).do(microcontrol)
        schedule.every().day.at(sixthC).do(math)
        schedule.every().day.at(seventhC).do(employ)

    def do_2():
        print('exec DO 2')
        schedule.every().day.at(firstC).do(powersp)
        schedule.every().day.at(sixthC).do(oopss)
        schedule.every().day.at(seventhC).do(pcb_m)

    def do_3():
        print('exec DO 3')
        schedule.every().day.at(firstC).do(math)
        schedule.every().day.at(thirdC).do(seminar)
        schedule.every().day.at(sixthC).do(powersp)
        schedule.every().day.at(seventhC).do(indian_art)
        schedule.every().day.at(eightC).do(oopss)

    def do_4():
        print('exec DO 4')
        schedule.every().day.at(firstC).do(oopss)
        schedule.every().day.at(thirdC).do(microcontrol)
        schedule.every().day.at(fifthC).do(pcb_m)
        schedule.every().day.at(seventhC).do(compre)
        schedule.every().day.at(eightC).do(smartgrid)

    def do_5():
        print('exec DO 5')
        schedule.every().day.at(firstC).do(smartgrid)
        schedule.every().day.at(thirdC).do(prof_sk)
        schedule.every().day.at(sixthC).do(microcontrol)
        schedule.every().day.at(seventhC).do(math)

    if is_connected(REMOTE_SERVER):
        print('Internet Check Passed')
        print('exec login_g()')
        login_g()
        print('exec login_mn()')
        day_order = login_mn()

        if day_order == 1:
            do_1()
        elif day_order == 2:
            do_2()
        elif day_order == 3:
            do_3()
        elif day_order == 4:
            do_4()
        elif day_order == 5:
            do_5()
        else:
            print('Sat/Sun hf')

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print(r"You're Offline")

    driver.quit()


if __name__ == "mainfunc":
    mainfunc()
