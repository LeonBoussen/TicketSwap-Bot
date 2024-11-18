#imports
import time
import os
from os import system as cmd
import requests

# variables
use_proxies = False
use_userAgents = False
proxy_list = []
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
            respons = requests.get(url)
            if respons.status_code != 200:
                badresponse = str(respons.status_code) + " " + str(respons)
                raise Exception(badresponse)
            elif respons.status_code == 200:
                print("Response good")
                html = respons.text
                print(html)
            else:
                print("Un unforseen error has appeerd >:(")
                cmd("pause")
                break

            cmd("pause")
        except Exception as error:
            print(error)
            cmd("pause")



#program start

while True:
    mainmenu()