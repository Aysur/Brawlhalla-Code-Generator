# Developed by Aysur#8606 / ឵℥#8606. If you use and modify/improve it leave credit
#Shoutout to Zardex?#1337 who helped me with the code
import sys
from turtle import clear
import pystyle
from pystyle import Colors, Colorate
import random 
import string
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW(f'Brawlgen [by Aysur]')

def main():
    print(Colorate.Vertical(Colors.yellow_to_red, '''
                        ██████╗ ██████╗  █████╗ ██╗    ██╗██╗      ██████╗ ███████╗███╗   ██╗
                        ██╔══██╗██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝ ██╔════╝████╗  ██║
                        ██████╔╝██████╔╝███████║██║ █╗ ██║██║     ██║  ███╗█████╗  ██╔██╗ ██║
                        ██╔══██╗██╔══██╗██╔══██║██║███╗██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
                        ██████╔╝██║  ██║██║  ██║╚███╔███╔╝███████╗╚██████╔╝███████╗██║ ╚████║
                        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝               ''', 1))
    print(Colorate.Horizontal(Colors.red_to_yellow,'          ┌────────────────────────────────────────────────────────────────────────────────────────┐'))
    print(Colorate.Horizontal(Colors.red_to_yellow,'          │                                    Developed by aysur                                  │'))
    print(Colorate.Horizontal(Colors.red_to_yellow,'          │────────────────────────────────────────────────────────────────────────────────────────│'))
    print(Colorate.Horizontal(Colors.red_to_yellow,'          │                                      [1] Generate                                      │'))
    print(Colorate.Horizontal(Colors.red_to_yellow,'          └────────────────────────────────────────────────────────────────────────────────────────┘'))
    print('')


    userchoice = input(Colorate.Horizontal(Colors.red_to_yellow,(' [>] Choice: ')))

    if userchoice == '1':
        
        amount = int(input(Colorate.Horizontal(Colors.red_to_yellow,(' [>] How many codes: '))))
        codechars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        symbols = '-'
        
        count = 0
        for i in range(amount):
            a=random.sample(codechars,k=6)
            b=random.sample(codechars,k=6)
            code = (f'{"".join(a)}{symbols}{"".join(b)}')
            
            print(Colors.green,'[GENERATED] %s' % (code))
            with open("codes.txt", "a+") as c:
                c.write("%s\n" % (code))
                count += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'Brawlgen by Aysur | Generated: [{count}]')
        input(Colorate.Horizontal(Colors.red_to_yellow,(f' [>] Generated {count} codes, Press Enter to Exit! '))) 
        sys.exit()
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow,(' [X] Wrong Input! ')))
        input()
        sys.exit()
if __name__ == "__main__":
    main()

#TO BE FIXED:

#When at end of code say 'Want to generate again? Press y/n' if y clear all my inputs and start from '[>] Choice:' again if n say 'Press Enter to Exit!'
#When i run it in python it closes after last message for some reason and here in visual studio code it doesn't
