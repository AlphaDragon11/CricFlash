from cric_scorer.gui import CricketScore
from tkinter import Tk

def main():
    rootWindow = Tk()
    obj = CricketScore(rootWindow)
    rootWindow.mainloop()

if __name__ == "__main__":
    main()