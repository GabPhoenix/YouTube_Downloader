import tkinter as tk
from tkinter import *
from pytube import YouTube

class MyWindow:
    def __init__(self):
        light_grey = "#2b2b2b"
        dark_grey = "#1b1b1b"
        font1 = "-family {Seoge UI} -size 16 -weight bold"
        font2 = "-family {Seoge UI} -size 10 -weight bold"

        self.root = tk.Tk()
        self.root.geometry("400x120+200+100")
        self.root.resizable(0, 0)
        self.root.configure(
            background = light_grey
        )

        self.label = tk.Label()
        self.label.place(relx=0.123, rely=0.001, width=300, height=50)
        self.label.configure(
            background = light_grey,
            foreground = "#ffffff",
            text = "YouTube Downloader",
            font = font1
        )

        self.entry = tk.Entry()
        self.entry.place(relx=0.025, rely=0.37, width=380, height=30)
        self.entry.configure(
            background = dark_grey,
            foreground = "#ffffff",
            relief = "flat"
        )

        self.button = tk.Button()
        self.button.place(relx=0.32, rely=0.65, width=150, height=30)
        self.button.configure(
            background = dark_grey,
            foreground = "#ffffff",
            relief = "flat",
            text = "Download Video",
            font = font2,
            activeforeground = "#ffffff",
            activebackground = light_grey,
            cursor = "hand2",
            command = self.donwloader
        )

        self.root.mainloop()

    def donwloader(self):
        link = self.entry.get()
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        ys.download()

if __name__ == "__main__":
    MyWindow()