#imports
import os
import random
from os import system as cmd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# variables
use_proxies = False
use_userAgents = False
proxy_list = []
agent_list = []
userAgentTemp = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36","Accept-Language": "en-US,en;q=0.9",}

# print title
def title_ascii(): 
    print("############################################################################################################################################################")
    print("##                                                                                                                                                        ##")
    print("##░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░       ░▒▓███████▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓██████▓▒░    ░▒▓█▓▒░           ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░   ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░                 ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░                 ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ##")
    print("##   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░  ░▒▓█▓▒░          ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░  ##")
    print("##                                                                                                                                                        ##")    
    print("############################################################################################################################################################")

#clears screen
def clear():
    cmd("cls")

def maximize_console():
    # TO DO
    # i did not get it working so not doing it now >:|
    return



def print_settings():
    global use_proxies
    global use_userAgents
    global proxy_list
    global agent_list

    print(f"Proxies: {use_proxies}\nUser-Agents: {use_userAgents}")

    # if use proxies is true it will be added to the list of displayed settings
    if use_proxies == True:
        p = 0
        for i in proxy_list:
            p += 1
        print(f"Proxies loaded: {p}")
    # if use useragents is true it will be added to the list of displayed settings
    if use_userAgents == True:
        u = 0
        for i in agent_list:
            u += 1
        print(f"Agents loaded: {u}")
    
    
# checks is proxies.txt is in current directory and other wise ask use for path to proxy list
def get_proxy_path():
    global use_proxies
    global proxy_list
    # get current directory and add proxies.txt to directory path
    dir = os.path.dirname(os.path.abspath(__file__))
    proxy_dir = os.path.join(dir, "proxies.txt")

    # check if path exists
    if os.path.isfile(proxy_dir):
        with open(proxy_dir, "r") as proxy_file:
            proxy_list = proxy_file.readlines()
    else:
        # make loop so when the users give a invalid input the users can try again
        # and to profent the program from crashing
        while True:
            print("not file called proxies.txt was found in the current directory")
            print("please import your own proxy file")
            proxy_dir = input("Drag and drop proxy file here: ")

            # check if given input is a file and if true add to proxy list
            if os.path.isfile(proxy_dir):
                with open(proxy_dir, "r") as proxy_file:
                    proxy_list = proxy_file.readlines()
                break
            
            # if user can tget a proxy file they can type exit to leave the loop and disable use proxies
            elif proxy_dir == "exit":
                use_proxies = False
                break

            # if path is not file print error and exit text
            else:
                clear()
                print("Dont have a proxy file?")
                print("type exit to go back")
                print("")

def mainmenu(): # load the main menu widget
    cmd("title TicketSwap 360 SSSniper! - main menu")
    clear()
    print("")
    title_ascii()
    print("")
    print_settings()
    print("############################################################################################################################################################")
    print("")
    print("1 - function 1 (Start sniping)")
    print("2 - function 2 (proxy settings)")
    print("3 - function 3 (User-agent settings)")
    print("4 - config (Maximale prijs per ticket voor snipen / mogelijk meerdere tickets snipen wanneer mogelijk)")
    print("5 - exit")
    print("")
    print("############################################################################################################################################################")
    print("")

    # try except voor keuze input check voor outbounts / invalid invoer
    try:
        keuze = int(input("Keuze: "))

        # keuze input validatie check
        if keuze <= 0 or keuze >= 6:
            raise Exception("Invalid input!")
        else:
            # start / begin botting process
            if keuze == 1:
                print("Start Snipe")
                start_botting()
            
            # proxy settings
            elif keuze == 2:
                # inport global vars in scope
                global use_proxies
                global proxy_list

                # proxy keuze menu loop tot er een juiste input word gegeven
                while True:
                    clear()
                    print("proxy settings!")
                    up = int(input("Do you want to use proxies? ( 1 - yes | 2 - no ) : "))

                    # input validatie for up input
                    if up <= 0 or up >= 3:
                        print("Invalid input")
                        cmd("pause")

                    # set use proxies setting true
                    # TO DO import proxy list, first check if 
                    # proxies.txt is in current directory,
                    # If not ask for path to proxy file.
                    elif up == 1:
                        use_proxies = True
                        get_proxy_path()
                        break

                    # if the users doesnt want to use proxies it will set use proxies to false,
                    # and will warm the user of the danger of not using a proxy
                    elif up == 2:
                        use_proxies = False
                        print("Not using proxies will get you temp banned on the website")
                        cmd("pause")
                        break
                        
            elif keuze == 3:
                print("configure user-agents")
            elif keuze == 4:
                print("Sniping config")
            elif keuze == 5:
                exit()
    except Exception as error:
        print(error)

def start_botting():
    global userAgentTemp

    global use_proxies
    global proxy_list
    global use_userAgents
    global agent_list

    while True:
        try:
            clear()
            title_ascii()
            print("")
            print("Type exit to go back")
            print("")
            url = input("Enter url of the ticketpage: ")
            if url == "exit":
                break
            else:
                while True:
                    options = Options()
                    # make a request to the website and get html code and check for tickets
                    
                    # if the user want to use proxies it here gets a random proxy from list and addes it in de driver settings
                    if use_proxies or use_userAgents:
                        if use_proxies:
                            proxy = random.choice(proxy_list)
                            options.add_argument(f"--proxy-server={proxy}")
                            print(f"Using proxy {proxy}")
                    
                    # TO DO now only using temp user agent
                    options.add_argument(f"user-agent={userAgentTemp}")

                    # create a web browser instance to load website
                    # loading this way will also load dynamic content like tickets
                    try:
                        driver = webdriver.Chrome(options=options)
                        driver.get(url)

                        # try to wait for page to fully load to ensure the ticket links will be load
                        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "css-3b4ilh")))
                        

                    except Exception as error:
                        print(error)
                        print("line 222")

                        #remove bad / not working proxy from list
                        if use_proxies:
                            proxy_list.remove(proxy)
                            print(f"removed {proxy} from proxy list {len(proxy_list) + 1} proxies left")

                        cmd("pause")
                        
                    
                    # get html from page source and parse it using beautifulsoup 
                    # so we can search through the code for the class containing the ticket url
                    html = driver.page_source
                    s = BeautifulSoup(html, 'html.parser')
                    print(s, "line 228")
                    cmd("pause")
                    ticket_class = s.find_all("a", class_="css-3b4ilh e1uk6tfj3")
                    for i in ticket_class:
                        a = 0
                        a += 1
                        print(a)
                    cmd("pause")
                    if ticket_class:
                        ticket_urls = [url.get('href') for url in ticket_class]
                        for url in ticket_urls:
                            print(url)
                        cmd("pause")
                    else:
                        print("No ticket")
                        cmd("pause")
            
        except Exception as error:
            print(error)
            cmd("pause")



#program start

while True:
    mainmenu()