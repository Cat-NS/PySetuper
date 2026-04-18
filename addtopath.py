import os
natives = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(natives)
os.system('setx apper {parent}\pysetuper.py')