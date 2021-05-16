#Imports...
import os , pyfiglet , webbrowser , shadpy

#------------------------------------------------------------------------------------------------------------

#----------www.Farzin-Dev.ir----------

Error = 'We have an error...\nTry Again...\n'
#------------------------------------------------------------------------------------------------------------
#banners...
def mban(text) : #Make Banner...
    try :
        res = pyfiglet.figlet_format(text)
        return res
    except :
        return Error
#------------------------------------------------------------------------------------------------------------
def banner() : #Main Banner...
    try :
        text = mban('shad-py')
        banner = text + 'Creator: www.Farzin-Dev.ir\nReason: Learn Programming...\nMessage from creator: Please dont use this for illegal things...\n'
        print(banner)
    except :
        return Error
#------------------------------------------------------------------------------------------------------------
def optionsb() : #Options Banner...
    print('1 - Start Bot\n2 - Help\n3 - Open HelpPage\n4 - Load Menu again\n5 - Exit')
    option = int(input('Enter Your Choice: '))
    if option == 5 :
        exit() #Exit From Script...
    elif option == 4 :
        clear()
        optionsb()
    elif option == 3 :
        clear()
        webbrowser.open_new_tab('https://farzin-dev.ir/2021/05/14/shad-py/')
        banner()
        optionsb()
    elif option == 2 :
        print('\nStart the bot and Enter what it wants!\nPlease Dont use it for illegal thins...')
        yes = input('\nEnter for main menu: ')
        if yes == '' :
            clear()
            banner()
            optionsb()
        else :
            clear()
            banner()
            optionsb()
    elif option == 1 :
        shadpy.start()
    else :
        clear()
        optionsb()
#------------------------------------------------------------------------------------------------------------
#Tools...
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
#----------www.Farzin-Dev.ir----------
#------------------------------------------------------------------------------------------------------------
