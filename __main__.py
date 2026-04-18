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

# methods like time.sleep(1)
sleep = time.sleep
# dirs / files
parent = os.path.dirname(os.path.abspath(__file__))
# app
class PySetuper:
    def main(self):

     print(" ---------------------------------------------------------- ")
     print("|                      PySetuper V1.0                      |")
     print(" ---------------------------------------------------------- ")
     print("| Hello there!                                             |")
     print("| 1) Search packages                                       |")
     print("| 2) Install packages                                      |")
     print("| 3) Uninstall packages                                    |")
     print("| 4) Validate package (Checking manifest file)             |")
     print("| 5) Export installed packages                             |")
     print("| 6) Download packages (Do not install)                    |")
     print("| 7) List of installed packages                            |")
     print(" ---------------------------------------------------------- ")
     print("|  Made by necostudio inc.                                 |")
     print(" ---------------------------------------------------------- ")
     sel = input('> ').lower().strip()
     if sel=='1':
         self.search()
     elif sel=='2':
          self.install()
     elif sel=='3':
          self.Uninstall()
     elif sel=='4':
          self.validate()
     elif sel=='5':
          self.export()
     elif sel=='6':
          self.download()
     elif sel=='7':
          self.list()
    def search(self):
             os.system('cls')
             searchpackage = input("Package search> ")
             os.system('winget search {searchpackage}')
             os.system("echo.")
             self.main()
    def install(self):
         os.system('cls')
         installpackage = input("Install Package (Recommend use ID why can be more packages with name ex: claude) > ")
         os.system('winget install {installpackage}')
         os.system('echo.')
         self.main()
    def Uninstall(self):
         os.system('cls')
         uninstallpackage = input("Uninstall packages (Recommend use ID why can be more packages with name ex: claude) > ")
         os.system('winget uninstall {uninstallpackage}')
         os.system('echo.')
         self.main()
    def validate(self):
         os.system('cls')
         validatepackage = input("Validate packages (Recommend use ID why can be more packages with name ex: claude) > ")
         os.system("winget validate {validatepackage}")
         os.system('echo.')
         self.main()
    def export(self):
         os.system("cls")
         exportpackages = input("Are you sure want export all packages? ( y / n )").lower().strip()
         if exportpackages =='y':
              os.system('cls')
              print("Exporting...")
              os.system('winget export')
              print("Exported!")
              input("Press enter to return menu")
              self.main()
         if exportpackages =='n':
              os.system('cls')
              self.main()
    def download(self):
                  os.system('cls')
                  downloadpackage = input("download Package (Recommend use ID why can be more packages with name ex: claude) > ")
                  os.system('winget download {downloadpackage}')
                  os.system('echo.')
                  self.main()
    def list(self):
          os.system('cls')
          print("Listing programms (All programs)...")
          os.system('echo.')
          os.system('winget list')
          os.system('echo.')
          self.main()

# Class Using
if __name__ == '__main__':
     mainclass = PySetuper()
     mainclass.main()