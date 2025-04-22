import os
import sys
import time

def troll():
    print("Loading... (this may take a while)")
    time.sleep(2)
    print("Almost there...")
    time.sleep(3)
    print("Just kidding! I'm not actually doing anything.")
    print("This is a troll script.")
    print("You wasted your time running this.")
    print("Ha ha ha!")
    print("Exiting in 5 seconds...")
    time.sleep(5)
    print("Just kidding again! I'm still here.")
    print("Exiting now, really...")
    time.sleep(1)
    sys.exit()

if __name__ == "__main__":
    troll()