# FOZIA WARSAME 638928 Bin1-c

import tkinter
from tkinter import messagebox


class GUI:
    def __init__(self):
        # Maakt een main window aan en geeft een titel
        self.main_window = tkinter.Tk()
        self.main_window.title("Calculator")

        # Maakt twee frames aan
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak vier intvar objecten voor checkbuttons,
        # maakt van object een integer
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        # Zet de vier intvar objecten naar 0,
        # 0 is de default niet aangevinkt, 1 is wel aangevinkt
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)

        # Checkbuttons aanmaken
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text="+",
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text="-",
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text="x",
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text=":",
                                       variable=self.cb_var4)

        # Zorgt dat checkbuttons zichtbaar worden
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()

        # Maakt een label aan
        self.label = tkinter.Label(self.top_frame,
                                   text="Vul in: ")

        # Maakt een text vak
        self.getal1_entry = tkinter.Entry(self.top_frame,
                                          width=7)
        self.getal2_entry = tkinter.Entry(self.top_frame,
                                          width=7)

        # Maakt twee buttons
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="Bereken",
                                          command=self.berekening)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # Plaatst de buttons
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        # Plaats het textvak
        self.getal1_entry.pack(side="right")
        self.getal2_entry.pack(side="right")

        # Plaatst de label in de window
        self.label.pack()

        # Zorgt dat de frames zichtbaar zijn
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Zorgt dat de GUI zichtbaar is
        tkinter.mainloop()

    def berekening(self):
        """Berekent de som

        :return: de uitkomst van de som
        """

        # Haalt text uit het textvlak
        getal1 = float(self.getal1_entry.get())
        getal2 = float(self.getal2_entry.get())

        self.message = "De uitkomst is: \n"
        # De sommen die uitgevoerd moeten worden als de button is
        # aangevinkt(1)
        if self.cb_var1.get() == 1:
            som = getal1 + getal2

        if self.cb_var2.get() == 1:
            som = getal1 - getal2

        if self.cb_var3.get() == 1:
            som = getal1 * getal2

        if self.cb_var4.get() == 1:
            som = getal1 / getal2

        # Laat de uitkomst zien
        tkinter.messagebox.showinfo("Resultaat",
                                    self.message +
                                    str(som))


if __name__ == '__main__':
    myGUI = GUI()