#imports
import time
from os import system as cmd

# variables
use_proxies = False
use_userAgents = False
proxy_list = {}
agent_list = []

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
    
# print a list of settings where the functions is called
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
    
    
# load the main menu widget
def mainmenu(): 
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
                    cmd("cls")
                    print("proxy settings!")
                    up = int(input("Do you want to use proxies? ( 1 - yes | 2 - no )"))

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

def start_botting(url):
    print(url)
    cmd("pause")

while True:
    mainmenu()