import tkinter as tk
from tkinter import ttk

class All(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.s = ttk.Style()
        # s.configure("TFrame", background="green")
        # s.configure("A.TFrame", background="blue")
        self.s.configure("A.TLabel", font=('Helvetica',10), background="red")
        self.master.title(u"all")

        # titleのラベル
        self.title_label = ttk.Label(self, text=u"List", style="A.TLabel")
        self.title_label.pack(pady=5)
class AllDummy(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        sub_w = None

    def create_widgets(self):
        self.s = ttk.Style(self)
        # s.configure("TFrame", background="green")
        # s.configure("A.TFrame", background="blue")
        self.s.configure("A.TLabel", font=('Helvetica',20), background="red")
        self.master.title(u"all")

        # titleのラベル
        self.title_label = ttk.Label(self, text=u"List", style="A.TLabel")
        self.title_label.pack(pady=5)

    def sub_window(self):
        global sub_w
        if sub_w is None or not sub_w.winfo_exists():
            sub_w = Toplevel()
            sub_w.title = "select"



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x650")

    all_frame = All(root)
    all_d_frame = AllDummy(root)
    all_frame.pack()
    all_d_frame.pack()


    root.mainloop()
