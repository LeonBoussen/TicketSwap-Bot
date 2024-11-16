#imports
import time
from os import system as cmd

use_proxies = False
use_userAgents = False
proxy_list = {}
agent_list = []

def title_ascii(): # print title
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
    
def print_settings():
    global use_proxies
    global use_userAgents
    global proxy_list
    global agent_list

    print(f"Proxies: {use_proxies}\nUser-Agents: {use_userAgents}")
    if use_proxies == True:
        p = 0
        for i in proxy_list:
            p += 1
        print(f"Proxies loaded: {p}")
    if use_userAgents == True:
        u = 0
        for i in agent_list:
            u += 1
        print(f"Agents loaded: {u}")
    
    

def mainmenu(): # load the main menu widget
    cmd("title TicketSwap 360 SSSniper! - main menu")
    cmd("cls")
    print("")
    title_ascii()
    print("")
    cmd("cls")
    title_ascii()
    print("")
    print_settings()
    print("############################################################################################################################################################")
    print("")
    print("1 - function 1 (Start sniping)")
    print("2 - function 2 (load proxies)")
    print("3 - function 3 (User-agent config)")
    print("4 - config (Maximale prijs per ticket voor snipen / mogelijk meerdere tickets snipen wanneer mogelijk)")
    print("5 - exit")
    print("")
    print("############################################################################################################################################################")
    print("")

    #try except voor keuze input check voor outbounts / invalid invoer
    try:
        keuze = int(input("Keuze: "))
        if keuze <= 0 or keuze >= 6:
            raise Exception("Invalid input!")
        else:
            if keuze == 1:
                print("Start Snipe")
                start_botting()
            elif keuze == 2:
                global use_proxies
                global proxy_list
                while True:
                    cmd("cls")
                    print("Load proxies")
                    up = int(input("Do you want to use proxies? ( 1 - yes | 2 - no )"))
                    if up <= 0 or up >= 3:
                        print("Invalid input")
                        cmd("pause")
                    elif up == 1:
                        use_proxies = True
                        break
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

def start_botting(url):
    print(url)
    cmd("pause")

while True:
    mainmenu()