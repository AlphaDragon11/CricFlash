from tkinter import *
from tkinter.ttk import Combobox, Treeview, Style, Scrollbar
from PIL import ImageTk, Image
from cric_scorer.scraper import get_live_matches

class CricketScore:

    def __init__(self, rootWindow):
        self.rootWindow = rootWindow
        self.rootWindow.title("LIVE CRICKET SCORE")
        self.rootWindow.geometry('800x500')

        self.rootWindow.configure(bg="#282c34")

        self.bg = ImageTk.PhotoImage(file="cric.jpg")
        bg = Label(self.rootWindow, image=self.bg).place(x=0, y=0)

        self.label = Label(self.rootWindow, text='Live Matches', font=("Helvetica", 25, "bold italic"), fg="#ffffff", bg="#282c34")
        self.label.pack(pady=20)

        self.var = StringVar()
        self.matches = get_live_matches()
        self.data = [i for i in self.matches.keys()]
        self.select_label = Label(self.rootWindow, text='Select Match:', font=("Helvetica", 15, "bold"), fg="#ffffff", bg="#282c34")
        self.select_label.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.cb = Combobox(self.rootWindow, values=self.data, width=50)
        self.cb.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.b1 = Button(self.rootWindow, text="Check Score", font=("Helvetica", 15, "bold"), bg="#61afef", fg="#282c34", command=self.show_match_details)
        self.b1.pack(side=BOTTOM, pady=20)

        self.b2 = Button(self.rootWindow, text="Show All Results", font=("Helvetica", 15, "bold"), bg="#61afef", fg="#282c34", command=self.show_all_results)
        self.b2.pack(side=BOTTOM, pady=10)

    def select(self):
        return self.cb.get()

    def show_match_details(self):
        details_window = Toplevel(self.rootWindow)
        details_window.title("Match Details")
        details_window.geometry('900x600')

        details_window.update_idletasks()
        width = details_window.winfo_width()
        height = details_window.winfo_height()
        x = (details_window.winfo_screenwidth() // 2) - (width // 2)
        y = (details_window.winfo_screenheight() // 2) - (height // 2)
        details_window.geometry(f'{width}x{height}+{x}+{y}')

        common_bg_frame = Frame(details_window, bg="#1c1c1c", bd=2, relief=SOLID)
        common_bg_frame.place(relwidth=1, relheight=1)

        left_frame = Frame(common_bg_frame, bg="#ffffff", bd=2, relief=SOLID)
        right_frame = Frame(common_bg_frame, bg="#f0f0f0", bd=2, relief=SOLID)
        left_frame.place(relwidth=0.6, relheight=1)
        right_frame.place(relx=0.6, relwidth=0.4, relheight=1)

        self.score_bg = Image.open("ScoreCheck.jpg")
        self.score_bg = ImageTk.PhotoImage(self.score_bg)
        score_bg_label = Label(right_frame, image=self.score_bg)
        score_bg_label.pack(fill=BOTH, expand=True)

        match_details = self.matches[self.select()]

        Label(left_frame, text=self.select() + " - " + match_details['match_header'], font=("Helvetica", 12, "bold"), fg="#282c34", bg="#ffffff", anchor="w", justify=LEFT).pack(fill=X, padx=10, pady=10)

        Label(left_frame, text="Score Details:", font=("Helvetica", 10, "bold"), fg="#282c34", bg="#ffffff", anchor="w", justify=LEFT).pack(anchor="w", padx=10)
        Label(left_frame, text=match_details['score_card'], font=("Helvetica", 10, "bold"), fg="#282c34", bg="#ffffff", anchor="w", justify=LEFT).pack(anchor="w", padx=10)

        Label(left_frame, text="Summary:", font=("Helvetica", 10, "bold"), fg="#282c34", bg="#ffffff", anchor="w", justify=LEFT).pack(anchor="w", padx=10, pady=(10, 0))
        summary_text = Text(left_frame, font=("Helvetica", 10), fg="#282c34", bg="#ffffff", wrap=WORD, height=5, width=55)
        summary_text.insert(END, match_details['summary'])
        summary_text.pack(anchor="w", padx=10, pady=(0, 10))

        Label(left_frame, text="Scoreboard:", font=("Helvetica", 10, "bold"), fg="#282c34", bg="#ffffff", anchor="w", justify=LEFT).pack(anchor="w", padx=10, pady=(10, 0))
        scoreboard_text = Text(left_frame, font=("Helvetica", 10), fg="#282c34", bg="#ffffff", wrap=WORD, height=20, width=55)
        scoreboard_text.insert(END, match_details['scoreboard'])
        scoreboard_text.pack(anchor="w", padx=10, pady=(0, 10))

    def show_all_results(self):
        results_window = Toplevel(self.rootWindow)
        results_window.title("All Match Results")
        results_window.geometry('800x500')

        results_window.update_idletasks()
        width = results_window.winfo_width()
        height = results_window.winfo_height()
        x = (results_window.winfo_screenwidth() // 2) - (width // 2)
        y = (results_window.winfo_screenheight() // 2) - (height // 2)
        results_window.geometry(f'{width}x{height}+{x}+{y}')

        common_bg_frame = Frame(results_window, bg="#1c1c1c", bd=2, relief=SOLID)
        common_bg_frame.place(relwidth=1, relheight=1)

        style = Style()
        style.configure("Treeview", background="#f0f0f0", foreground="#000000", rowheight=50, fieldbackground="#f0f0f0")
        style.map("Treeview", background=[('selected', '#61afef')])

        tree = Treeview(common_bg_frame, columns=("Match", "Score", "Summary"), show='headings')
        tree.heading("Match", text="Match")
        tree.heading("Score", text="Score")
        tree.heading("Summary", text="Summary")

        tree.column("Match", width=250, anchor="center")
        tree.column("Score", width=180, anchor="center")
        tree.column("Summary", width=530, anchor="center")

        for match, details in self.matches.items():
            tree.insert("", "end", values=(match, details['score_card'], details['summary']))

        scrollbar = Scrollbar(common_bg_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)