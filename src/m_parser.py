import tkinter as tk
from tkinter import ttk


class Args:
    def __init__(self):
        self.algo = None
        self.len = None
        self.gif = None
        self.destroy = None

    def load(self):
        args = self.__getArgs()
        try:
            self.algo = args["algo"]
            self.len = int(args["len"])
            self.gif = args["gif"] == "Yes"
            self.destroy = args["destroy"]
        except:
            self.load()

    def __getArgs(self):
        args = {}

        def runApp():
            app = tk.Tk()
            app.geometry("190x200")
            app.title("Args Form")

            ################## algorithm ##################

            label_1 = tk.Label(app, text="Choose your algorithm")
            label_1.grid(column=0, row=0)

            algo_combobox = ttk.Combobox(
                app,
                values=[
                    "Insertion Sort",
                    "Quick Sort",
                    "Bubble Sort",
                ],  # , "Fusion Sort"],
                state="readonly",
            )
            algo_combobox.grid(column=0, row=1)
            algo_combobox.current(0)

            ################## lenght ##################

            label_2 = tk.Label(app, text="Size of the array")
            label_2.grid(column=0, row=2)

            lenght_entry = ttk.Entry(app)
            lenght_entry.insert(tk.END, "20")
            lenght_entry.grid(column=0, row=3)

            ################## gif ##################

            label_3 = tk.Label(app, text="Create .gif output")
            label_3.grid(column=0, row=4)

            gif_entry = ttk.Combobox(app, values=["No", "Yes"], state="readonly",)
            gif_entry.grid(column=0, row=5)
            gif_entry.current(0)

            ################## validation ##################
            def callBackFunc():
                args["algo"] = algo_combobox.get()
                args["len"] = lenght_entry.get()
                args["gif"] = gif_entry.get()
                args["destroy"] = False
                app.destroy()

            validate_button = ttk.Button(app, text="Run !", command=callBackFunc)
            validate_button.grid(column=0, row=6)

            ################## exit ##################
            def callBackFunc_exitV():
                args["algo"] = algo_combobox.get()
                args["len"] = lenght_entry.get()
                args["gif"] = gif_entry.get()
                args["destroy"] = True
                app.destroy()

            quit_button = ttk.Button(app, text="Exit", command=callBackFunc_exitV)
            quit_button.grid(column=0, row=7)

            app.mainloop()

        runApp()

        return args

    def __str__(self):
        return f"algo: {self.algo}"


args = Args()

