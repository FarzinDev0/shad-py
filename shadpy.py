#Imports...
import time , tools , os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#----------www.Farzin-Dev.ir----------

#------------------------------------------------------------------------------------------------------------
def clear() : #Clear Screen...
    try :
        res = os.name
        if res == 'nt' :
            os.system('cls')
        else :
            os.system('clear')
    except :
        return Error
#------------------------------------------------------------------------------------------------------------


#pyfiglet , selenium , webdriver_manager
Error = 'We have an error...\nTry Again...\n'
#------------------------------------------------------------------------------------------------------------
#SetUp...
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')  # ignore chrome ssl error...
options.add_argument('--ignore-certificate-errors')  # ignore chrome certification error...
#------------------------------------------------------------------------------------------------------------
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #Firefox Driver...
clear() #clear Screen
#driver.set_window_position(-10000, 0) #Set Position...
driver.get("https://web.shad.ir")  # shad url
#------------------------------------------------------------------------------------------------------------
action = ActionChains(driver)
#------------------------------------------------------------------------------------------------------------
#Funcs...
def login() :
    try :
        phone = input('Example: 09141234567\nEnter Your Phone Number: ') #Get phone number...
        time.sleep(2)
        phoneInput = driver.find_element_by_name('phone_number') #Find Phone Number Input...
        time.sleep(2)
        phoneInput.send_keys(phone) #Enter Phone Number...
        time.sleep(2)
        phoneInput.send_keys(Keys.ENTER) #Press Enter...
        time.sleep(2)
        yes = driver.find_element_by_xpath('/html/body/div[1]/app-root/app-modal-container/div/app-modal-view/div/div/div/app-confirm-custom/div/div[2]/button[2]/span')
        time.sleep(2)
        yes.click() #Click ok message...
        code = input('Enter The Code: ') #Get Code From user...
        time.sleep(2)
        codeInput = driver.find_element_by_name('phone_code') #Find Code Input...
        time.sleep(2)
        codeInput.send_keys(code) #Enter Code to Input Box...
        time.sleep(2)
        clear()
    except :
        print(Error)
        exit()
#------------------------------------------------------------------------------------------------------------
def message(xpath , message) :
    try :
        chat = driver.find_element_by_xpath(xpath)
        chat.click()
        time.sleep(1)
        chatinput = driver.find_element_by_class_name('composer_rich_textarea')
        time.sleep(1)
        chatinput.send_keys(message)
        time.sleep(1)
        chatinput.send_keys(Keys.ENTER)
    except :
        print('There is an error\nTry again')
        tools.optionsb()

#------------------------------------------------------------------------------------------------------------
def start() :
    try :
        #------------------------------------
        clear()
        print(tools.mban('Shad-Py'))
        print('class name example: math or Mr Azadis class\nclass time example: 12:30 or 10:00\ntext example: Im Here sir.\n')
        #------------------------------------
        text = input('Enter A text. I will send it to your classes: ')
        #------------------------------------
        className1 = input('1st class Name: ')
        classTime1 = input('1st class Time: ').split(':')
        #------------------------------------
        #------------------------------------
        className2 = input('2st class Name: ')
        classTime2 = input('2st class Time: ').split(':')
        #------------------------------------
        #------------------------------------
        className3 = input('3st class Name: ')
        classTime3 = input('3st class Time: ').split(':')
        #------------------------------------
        #------------------------------------
        className4 = input('4st class Name: ')
        classTime4 = input('4st class Time: ').split(':')
        #------------------------------------
        print(f'1nd class: {className1} -- {classTime1} ---- 2nd class: {className2} -- {classTime2}')
        print(f'3nd class: {className3} -- {classTime3} ---- 4nd class: {className4} -- {classTime4}')
        #------------------------------------
        #------------------------------------
        class1 = f"//span[@verified='true'][contains(text(),'{className1}')]"
        class2 = f"//span[@verified='true'][contains(text(),'{className2}')]"
        class3 = f"//span[@verified='true'][contains(text(),'{className3}')]"
        class4 = f"//span[@verified='true'][contains(text(),'{className4}')]"
        #------------------------------------
        status1 = False
        status2 = False
        status3 = False
        status4 = False
        #------------------------------------
        while True :
            clear()
        #------------------------------------
            timed = datetime.now()
            time1 = timed.time()
            timeH = time1.strftime('%H')
            timeM = time1.strftime('%M')
            timeS = time1.strftime('%S')
        #------------------------------------
            print(tools.mban('Shad Py'))
            print(f"Time : {timeH} : {timeM} : {timeS}")  # print current time
            print(f'1nd class: {className1} -- {classTime1} ---- 2nd class: {className2} -- {classTime2}')
            print(f'3nd class: {className3} -- {classTime3} ---- 4nd class: {className4} -- {classTime4}')
        #------------------------------------
        #------------------------------------
            if timeH == classTime1[0] and timeM == classTime1[1] :
                if status1 == False and len(classTime1) == 2 :
                    message(class1 , text)
                    status1 = True
            elif timeH == classTime2[0] and timeM == classTime2[1] :
                if status2 == False and len(classTime2) == 2 :
                    message(class2 , text)
                    status2 = True
            elif timeH == classTime3[0] and timeM == classTime3[1] :
                if status3 == False and len(classTime3) == 2 :
                    message(class3 , text)
                    status3 = True
            elif timeH == classTime4[0] and timeM == classTime4[1] :
                if status4 == False and len(classTime4) == 2:
                    message(class4 , text)
                    status4 = True
            elif timeH >= classTime1[0] and timeM > classTime1[1] and timeH >= classTime2[0] and timeM > classTime2[1] and timeH >= classTime3[0] and timeM > classTime3[1] and timeH >= classTime4[0] and timeM > classTime4[1] :
                clear()
                print(tools.mban('Shad Py'))
                tools.optionsb()
                print('Mission completed')
                tools.optionsb()
            time.sleep(30)
    #------------------------------------------------------------------------------------------------------------
    #----------www.Farzin-Dev.ir----------
    except :
        clear()
        print(tools.mban('Shad Py'))
        tools.optionsb()