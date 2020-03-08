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

    def create_widgets(self):
        self.s = ttk.Style(self)
        # s.configure("TFrame", background="green")
        # s.configure("A.TFrame", background="blue")
        self.s.configure("A.TLabel", font=('Helvetica',20), background="red")
        self.master.title(u"all")

        # titleのラベル
        self.title_label = ttk.Label(self, text=u"List", style="A.TLabel")
        self.title_label.pack(pady=5)

        self.btn = ttk.Button(
                self,
                text="open",
                command=lambda: self.sub_window()
            )
        self.btn.pack()

    def sub_window(self):
        self.sub_w = tk.Toplevel(self)
        self.sub_w.title = "select"
        self.sub_w.geometry("300x300")

        self.delbtn = ttk.Button(self.sub_w, text="delete", command=self.sub_w.destroy)
        self.delbtn.pack()

        self.sub_w.grab_set()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x650")

    all_frame = All(root)
    all_d_frame = AllDummy(root)
    all_frame.pack()
    all_d_frame.pack()


    root.mainloop()

        # comboboxに選手名の一覧を表示
        # self.name_combo["values"] = players_db
