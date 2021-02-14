
import time
import random, string
from colorama import Fore, Style


def main():
	print("""


███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝

█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀ ▄█ █▄░█   █▀ █░░ █ █▄░█ █▄▀ █▄█
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   ▄█ ░█ █░▀█   ▄█ █▄▄ █ █░▀█ █░█ ░█░


	""")

main();

amount = int(input('How Many Codes Do You Want To Generate:'))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Nitro_Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    value += 1
print("Done, All Codes Have Been Saved In Codes.txt")


