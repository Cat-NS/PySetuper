import os
import subprocess
import time
import platform
# Sys check
os_name = platform.system
if os_name == 'Windows':
   print("Could load bootstrapper")
   os.system("cls")
elif os_name == 'Linux':
   print("Could not load bootstrapper (Error code: 404")
elif os_name == 'Darwin':
   print("Could not load bootstrapper (Error code: 404)")
# Bootstrapper
sleep = time.sleep
parent = os.path.dirname(os.path.abspath(__file__))
main = os.path.join(parent, "__main__.py")
os.system('mode con: cols=61 lines=26')
print(" ---------------------------------------------------------- ")
print("|               PySetuper BootStraper V0.1-pre             |")
print(" ---------------------------------------------------------- ")
print("| Preparing __main__..                                     |")
print("|                                                          |")
print("|                                                          |")
print(" ---------------------------------------------------------- ")
sleep(2)
os.system('cls')
print(" ---------------------------------------------------------- ")
print("|               PySetuper BootStraper V0.1-pre             |")
print(" ---------------------------------------------------------- ")
print("| Starting  __main__..                                     |")
print("|                                                          |")
print("|                                                          |")
print(" ---------------------------------------------------------- ")
sleep(2)
os.system('cls')
subprocess.run(["python", 'natives' , main])
