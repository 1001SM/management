import my_module as mod
import tkinter as tk
import openpyxl
import copy
import os
import datetime
import sqlite3

from tkinter import messagebox
from tkinter import ttk

#
# path_teamdata = os.path.abspath("excel/teamdata.xlsx")
# path_db = os.path.abspath("db.xlsx")

# class Menu(tk.Menu):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.create_file_menu()
#
#     def create_file_menu(self):
#         """Fileメニューの作成"""
#         menu_file = tk.Menu(self)
#         self.add_cascade(menu=menu_file, label='File')
#         menu_file.add_command(label="register", command=lambda:mod.change_page(self.widget.master, register_frame))
#         menu_file.add_command(label="edit")
#         menu_file.add_command(label="all", command=lambda:mod.change_page(self.widget.master, all_frame))



# wb_teamdata = openpyxl.load_workbook(path_teamdata)

class All(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        mod.show_all(self)

        sub_w = None

    def create_widgets(self):
        self.s = ttk.Style()
        # s.configure("TFrame", background="green")
        # s.configure("A.TFrame", background="blue")
        self.s.configure('A.TLabel', font=('Helvetica',18))
        self.s.configure('All.Label', font=('Helvetica',12))
        self.master.title(u"all")

        # titleのラベル
        self.title_label = ttk.Label(self, text=u"List", style="A.TLabel")
        self.title_label.pack(pady=5)

        # columns_idの初期化
        columns_id = [i for i in range(12)]

        columns_title = [
            "name", "geschlecht", "alt", "position",
            "verletzungsart", "korperteil", "verletzungsdatum",
            "der geheiligte tag", "wie", "sonstig", "verletzter ort",
            "diagnose"
            ]

        # topcontentsのframe
        self.top_frame = ttk.Frame(self, width="1100", height="30")

        self.top_frame.pack_propagate(False)
        self.top_frame.pack(expand=True)

        self.name_label = ttk.Label(self.top_frame, text="name:", style="All.Label")
        self.name_combo = ttk.Combobox(
            self.top_frame,
            state="readonly"
            )
        # comboboxに選手名の一覧を表示
        # self.name_combo["values"] = players_db

        self.sex_label = ttk.Label(self.top_frame, text="geschlecht:", style="All.Label")
        self.player_sex = tk.StringVar()
        self.sex_entry = ttk.Entry(
            self.top_frame,
            textvariable=self.player_sex
            )


        self.age_label = ttk.Label(self.top_frame, text="alter:", style="All.Label")
        self.player_age = tk.StringVar()
        self.age_entry = ttk.Entry(
            self.top_frame,
            textvariable=self.player_age
            )

        self.position_label = ttk.Label(self.top_frame, text="position:", style="All.Label")
        self.position_combo = ttk.Combobox(
            self.top_frame,
            state="readonly",
            )
        # self.position_combo["values"] = positions_db

        self.name_label.pack(side="left")
        self.name_combo.pack(side="left", padx=4)

        self.sex_label.pack(side="left")
        self.sex_entry.pack(side="left", padx=4)

        self.age_label.pack(side="left")
        self.age_entry.pack(side="left", padx=4)

        self.position_label.pack(side="left")
        self.position_combo.pack(side="left", padx=4)

        self.top2_frame = ttk.Frame(self, width="1100", height="50")
        self.top2_frame.pack_propagate(False)
        self.top2_frame.pack(expand=True)

        self.team_label = ttk.Label(self.top2_frame, text="mannschaft:", style="All.Label")
        self.player_team = tk.StringVar()
        self.team_entry = ttk.Entry(
            self.top2_frame,
            textvariable=self.player_team
            )

        self.injury_name_label = ttk.Label(self.top2_frame, text="diagnose:", style="All.Label")
        self.injury_name_text = tk.Text(
            self.top2_frame,
            width="30",
            height="2"
            )

        self.injury_kind_label = ttk.Label(self.top2_frame, text="verletzungsart:", style="All.Label")
        self.injury_kind_combo = ttk.Combobox(
            self.top2_frame,
            state="readonly"
            )
        # self.injury_kind_combo["values"] = injury_kind_db


        self.injury_part_label = ttk.Label(self.top2_frame, text="korperteil:", style="All.Label")
        self.injury_part_combo = ttk.Combobox(
            self.top2_frame,
            state="readonly"
            )
        # self.injury_part_combo["values"] = injury_part_db

        self.top3_frame = ttk.Frame(self, width="1100", height="30")
        self.top3_frame.pack_propagate(False)
        self.top3_frame.pack(expand=True)

        self.injury_date_label = ttk.Label(self.top3_frame, text="verletzungszeit:", style="All.Label")
        self.injury_date_entry = ttk.Entry(
            self.top3_frame,
            )

        self.cure_date_label = ttk.Label(self.top3_frame, text="vollstandige Heilung:", style="All.Label")
        self.cure_date_entry = ttk.Entry(
            self.top3_frame,
            )

        self.riha_label = ttk.Label(self.top3_frame, text="dauern reha:", style="All.Label")
        self.riha_entry = ttk.Entry(
            self.top3_frame,
            )

        self.top4_frame = ttk.Frame(self, width="1100", height="50")
        self.top4_frame.pack_propagate(False)
        self.top4_frame.pack(expand=True)

        self.how_label = ttk.Label(self.top4_frame, text="wie:", style="All.Label")
        self.how_text = tk.Text(
            self.top4_frame,
            width="30",
            height="3"
            )

        self.injury_place_label = ttk.Label(self.top4_frame, text="verletzter ort:", style="All.Label")
        self.injury_place_entry = ttk.Entry(
            self.top4_frame,
            )

        self.other_label = ttk.Label(self.top4_frame, text="sonstig:", style="All.Label")
        self.other_text = tk.Text(
            self.top4_frame,
            width="30",
            height="3"
            )

        self.team_label.pack(side="left")
        self.team_entry.pack(side="left", padx=4)

        self.injury_name_label.pack(side="left")
        self.injury_name_text.pack(side="left", padx=4)

        self.injury_kind_label.pack(side="left")
        self.injury_kind_combo.pack(side="left", padx=4)

        self.injury_part_label.pack(side="left")
        self.injury_part_combo.pack(side="left", padx=4)

        self.injury_date_label.pack(side="left")
        self.injury_date_entry.pack(side="left", padx=4)

        self.cure_date_label.pack(side="left")
        self.cure_date_entry.pack(side="left", padx=4)

        self.riha_label.pack(side="left")
        self.riha_entry.pack(side="left", padx=4)

        self.how_label.pack(side="left")
        self.how_text.pack(side="left", padx=4)

        self.injury_place_label.pack(side="left")
        self.injury_place_entry.pack(side="left", padx=4)

        self.other_label.pack(side="left")
        self.other_text.pack(side="left", padx=4)

        self.show_all_btn = ttk.Button(
                                self.top4_frame,
                                text="show all",
                                command=lambda: mod.show_all(self)
                            )
        self.complete_btn = ttk.Button(
                                self.top4_frame,
                                text="complete",
                                command=lambda: mod.getValue(self)
                            )


        self.show_all_btn.pack(side=tk.RIGHT)
        self.complete_btn.pack(padx=12,side=tk.RIGHT)





        # contentsのframe
        self.contents_frame = ttk.Frame(self, width="1100", height="500")
        # self.contents_frame.pack_propagate(False)
        self.contents_frame.pack(expand=True)

        # treeview用のframeを作成
        self.treeview_frame = ttk.Frame(self.contents_frame, width="1085", height="450", style="A.TFrame")
        self.treeview_frame.pack_propagate(False)
        self.treeview_frame.pack(side=tk.LEFT, expand=True)

        # treeviewの設定
        self.tree = ttk.Treeview(self.treeview_frame)
        self.tree.configure(height="20")

        # titleの設定
        columns_title = [
            "name", "geschlecht","alter","position","mannschaft","diagnose","verletzungsart",
            "korperteil","verletzungszeit","vollstandige Heilung","dauern reha",
            "wie","verletzter ort","sonstig","player_info_id"
            ]

        # columns_idの初期化
        self.columns_id = [i for i in range(len(columns_title))]
        del_int = [len(columns_title) - 1]

        self.tree["columns"] = self.columns_id
        self.tree["displaycolumns"] = list(set(self.columns_id) - set(del_int))
        # 一番最初のcolumnを非表示
        self.tree["show"] = "headings"

        # treeviewの列名設定
        for i in range(len(self.columns_id)):
            self.tree.heading(i, text = columns_title[i])

        # 行の追加
        # for i in  range(50):
        #     self.tree.insert("", index="end", values=i)

        self.tree.pack(pady=12,expand=True)

        # y scrollbarを設定
        self.scrollbar = ttk.Scrollbar(
            self.contents_frame,
            orient = tk.VERTICAL,
            command = self.tree.yview
            )
        self.tree['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=tk.RIGHT,fill="y")

        # x scrollbarを設定
        self.xscrollbar = ttk.Scrollbar(
            self.treeview_frame,
            orient = tk.HORIZONTAL,
            command = self.tree.xview
            )
        self.tree["xscrollcommand"] = self.xscrollbar.set
        self.xscrollbar.pack(side=tk.BOTTOM,fill="x")

    def sub_window(self):
        global sub_w
        if sub_w is None or not sub_w.winfo_exists():
            sub_w = Toplevel()
            sub_w.title = "select"


class Register(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

        # resiterボタン
        self.btn = ttk.Button(self,
            text="register",
            command=lambda :mod.register(self)
            )
        self.btn.pack(pady=5)

    def create_widgets(self):
        # db接続
        con = sqlite3.connect("manage.db")
        c = con.cursor()
        # 選手情報取得
        players_db = []
        append_players = players_db.append
        for i in c.execute("select player_name from players"):
            append_players(i)

        # position情報取得
        positions_db = []
        append_position = positions_db.append
        for i in c.execute("select position from positions"):
            append_position(i)

        # injury_name情報取得
        injury_kind_db = []
        append_injury_kind = injury_kind_db.append
        for i in c.execute("select injury_name from injuries"):
            append_injury_kind(i)

        # injury_part情報取得
        injury_part_db = []
        append_injury_part = injury_part_db.append
        for i in c.execute("select injury_part_name from injuries_parts"):
            append_injury_part(i)

        s = ttk.Style()
        # s.configure("TFrame", background="red")
        s.configure("TLabel", font=('Helvetica',16))
        s.configure("A.TLabel", font=('Helvetica',18))
        self.master.title(u"register")

        self.title_label = ttk.Label(self, text="Register", style="A.TLabel")
        self.title_label.pack(pady=5)

        self.refresh_btn = ttk.Button(self, text="refresh", command=lambda:mod.refresh(self))
        self.refresh_btn.pack(pady=5)

        self.frame1 = ttk.Frame(self, width=300)
        self.frame2 = ttk.Frame(self, width=300)
        self.frame3 = ttk.Frame(self, width=300)
        self.frame4 = ttk.Frame(self, width=300)
        self.frame5 = ttk.Frame(self, width=300)
        self.frame6 = ttk.Frame(self, width=300)
        self.frame7 = ttk.Frame(self, width=300)
        self.frame8 = ttk.Frame(self, width=300)
        self.frame9 = ttk.Frame(self, width=300)
        self.frame10 = ttk.Frame(self, width=300)
        self.frame11 = ttk.Frame(self, width=300)
        self.frame12 = ttk.Frame(self, width=300)
        self.frame13 = ttk.Frame(self, width=300)
        self.frame14 = ttk.Frame(self, width=300)

        self.name_label = ttk.Label(self.frame1, text="name:")
        self.name_combo = ttk.Combobox(
            self.frame1,
            state="readonly"
            )
        # comboboxに選手名の一覧を表示
        self.name_combo["values"] = players_db

        self.set_player_info_btn = ttk.Button(
            self.frame1,
            text="show info",
            command=lambda: mod.set_player_info(self, self.name_combo)
            )


        self.sex_label = ttk.Label(self.frame2, text="geschlecht:")
        self.player_sex = tk.StringVar()
        self.sex_entry = ttk.Entry(
            self.frame2,
            textvariable=self.player_sex
            )


        self.age_label = ttk.Label(self.frame3, text="alter:")
        self.player_age = tk.StringVar()
        self.age_entry = ttk.Entry(
            self.frame3,
            textvariable=self.player_age
            )


        self.position_label = ttk.Label(self.frame4, text="position:")
        self.position_combo = ttk.Combobox(
            self.frame4,
            state="readonly",
            )
        self.position_combo["values"] = positions_db


        self.frame1.pack(fill="x", pady=2)
        self.name_label.pack(side="left")
        self.name_combo.pack(side="left")
        self.set_player_info_btn.pack(side="right")

        self.frame2.pack(fill="x", pady=2)
        self.sex_label.pack(side="left")
        self.sex_entry.pack(side="left")

        self.frame3.pack(fill="x", pady=2)
        self.age_label.pack(side="left")
        self.age_entry.pack(side="left")

        self.frame4.pack(fill="x", pady=2)
        self.position_label.pack(side="left")
        self.position_combo.pack(side="left")

        # 選手情報
        self.team_label = ttk.Label(self.frame5, text="mannschaft:")
        self.player_team = tk.StringVar()
        self.team_entry = ttk.Entry(
            self.frame5,
            textvariable=self.player_team
            )

        self.injury_name_label = ttk.Label(self.frame6, text="diagnose:")
        self.injury_name_text = tk.Text(
            self.frame6,
            width="50",
            height="2"
            )

        self.injury_kind_label = ttk.Label(self.frame7, text="verletzungsart:")
        self.injury_kind_combo = ttk.Combobox(
            self.frame7,
            state="readonly"
            )
        self.injury_kind_combo["values"] = injury_kind_db


        self.injury_part_label = ttk.Label(self.frame8, text="korperteil:")
        self.injury_part_combo = ttk.Combobox(
            self.frame8,
            state="readonly"
            )
        self.injury_part_combo["values"] = injury_part_db

        self.injury_date_label = ttk.Label(self.frame9, text="verletzungszeit:")
        self.injury_date_entry = ttk.Entry(
            self.frame9,
            )

        self.cure_date_label = ttk.Label(self.frame10, text="vollstandige Heilung:")
        self.cure_date_entry = ttk.Entry(
            self.frame10,
            )

        self.riha_label = ttk.Label(self.frame11, text="dauern reha:")
        self.riha_entry = ttk.Entry(
            self.frame11,
            )

        self.how_label = ttk.Label(self.frame12, text="wie:")
        self.how_text = tk.Text(
            self.frame12,
            width="50",
            height="4"
            )

        self.injury_place_label = ttk.Label(self.frame13, text="verletzter ort:")
        self.injury_place_entry = ttk.Entry(
            self.frame13,
            )

        self.other_label = ttk.Label(self.frame14, text="sonstig:")
        self.other_text = tk.Text(
            self.frame14,
            width="50",
            height="4"
            )

        self.frame5.pack(fill="x", pady=2)
        self.team_label.pack(side="left")
        self.team_entry.pack(side="left")

        self.frame6.pack(fill="x", pady=2)
        self.injury_name_label.pack(side="left")
        self.injury_name_text.pack(side="left")

        self.frame7.pack(fill="x", pady=2)
        self.injury_kind_label.pack(side="left")
        self.injury_kind_combo.pack(side="left")

        self.frame8.pack(fill="x", pady=2)
        self.injury_part_label.pack(side="left")
        self.injury_part_combo.pack(side="left")

        self.frame9.pack(fill="x", pady=2)
        self.injury_date_label.pack(side="left")
        self.injury_date_entry.pack(side="left")

        self.frame10.pack(fill="x", pady=2)
        self.cure_date_label.pack(side="left")
        self.cure_date_entry.pack(side="left")

        self.frame11.pack(fill="x", pady=2)
        self.riha_label.pack(side="left")
        self.riha_entry.pack(side="left")

        self.frame12.pack(fill="x", pady=2)
        self.how_label.pack(side="left")
        self.how_text.pack(side="left")

        self.frame13.pack(fill="x", pady=2)
        self.injury_place_label.pack(side="left")
        self.injury_place_entry.pack(side="left")

        self.frame14.pack(fill="x", pady=2)
        self.other_label.pack(side="left")
        self.other_text.pack(side="left")

class Edit(Register):
    def __init__(self, master=None):
        super().__init__(master)

        con = sqlite3.connect("manage.db")
        c = con.cursor()

        self.btn["text"] = u"edit"
        self.btn["command"] = lambda: mod.edit_info(self)
        self.title_label["text"] = "Edit"

        self.set_player_info_btn["text"] = "show all"
        self.set_player_info_btn["command"] = lambda: mod.set_info_all(self, self.name_combo)
        # プレイヤーidの初期化
        self.player_info_id = 0

        self.refresh_btn["command"] = lambda:mod.refresh_edit(self)

        players_db = []
        append_players = players_db.append

        sql ="""
                select player_name from players_info
                inner join players on
                players_info.player_id = players.player_id
                where players_info.delete_flag = 0
            """

        for i in c.execute(sql):
            append_players(i)

        self.name_combo["values"] = players_db

        con.close()

class MasterPlayer(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        s = ttk.Style()

        s.configure("A.TLabel", font=('Helvetica',18))

        self.title_label = ttk.Label(self, text="Master_player", style="A.TLabel")
        self.title_label.pack(pady=5)

        self.frame1 = ttk.Frame(self, width=300)
        self.frame2 = ttk.Frame(self, width=300)
        self.frame3 = ttk.Frame(self, width=300)
        self.frame4 = ttk.Frame(self, width=300)

        self.player_name_label = ttk.Label(self.frame1, text="name:", style="L.TLabel")
        self.player_name_entry = ttk.Entry(self.frame1)

        self.player_sex_label = ttk.Label(self.frame2, text="geschlecht:")
        self.player_sex_entry = ttk.Entry(self.frame2)

        self.player_age_label = ttk.Label(self.frame3, text="alter:")
        self.player_age_entry = ttk.Entry(self.frame3)

        self.player_team_label = ttk.Label(self.frame4, text="mannschaft:")
        self.player_team_entry = ttk.Entry(self.frame4)

        self.frame1.pack(fill="x", pady=2)
        self.player_name_label.pack(side="left")
        self.player_name_entry.pack(side="left")

        self.frame2.pack(fill="x", pady=2)
        self.player_sex_label.pack(side="left")
        self.player_sex_entry.pack(side="left")

        self.frame3.pack(fill="x", pady=2)
        self.player_age_label.pack(side="left")
        self.player_age_entry.pack(side="left")

        self.frame4.pack(fill="x", pady=2)
        self.player_team_label.pack(side="left")
        self.player_team_entry.pack(side="left")

        self.btn = ttk.Button(
            self,
            text="register",
            command=lambda:mod.register_m_player(self)
        )
        self.btn.pack()

class MasterInjury(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        s = ttk.Style()

        s.configure("A.TLabel", font=('Helvetica',18))

        self.title_label = ttk.Label(self, text="Master_injury", style="A.TLabel")
        self.title_label.pack(pady=5)

        self.frame1 = ttk.Frame(self, width=300, height=400)

        self.injury_name_label = ttk.Label(self.frame1, text="verletzungsart:")
        self.injury_name_entry = ttk.Entry(self.frame1)

        self.frame1.pack(fill="x", pady=10)
        self.injury_name_label.pack(side="left")
        self.injury_name_entry.pack(side="left")
        self.btn = ttk.Button(
            self,
            text="register",
            command=lambda: mod.register_m_others(self,"injuries")
        )
        self.btn.pack()

class MasterInjuryPart(MasterInjury):
    def __init__(self, master=None):
        super().__init__(master)

        self.title_label["text"] = "Master injury part"
        self.injury_name_label["text"] = "korperteil:"
        self.btn["command"] = lambda: mod.register_m_others(self,"injuries_parts")

class MasterPosition(MasterInjury):
    def __init__(self, master=None):
        super().__init__(master)

        self.title_label["text"] = "Master position"
        self.injury_name_label["text"] = "position:"
        self.btn["command"] = lambda: mod.register_m_others(self,"positions")

class MasterPlayerE(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # db接続
        con = sqlite3.connect("manage.db")
        c = con.cursor()

        s = ttk.Style()

        s.configure("A.TLabel", font=('Helvetica',18))

        self.title_label = ttk.Label(self, text="Master_player", style="A.TLabel")
        self.title_label.pack(pady=8)

        self.frame1 = ttk.Frame(self, width=300)
        self.frame2 = ttk.Frame(self, width=300)
        self.frame3 = ttk.Frame(self, width=300)
        self.frame4 = ttk.Frame(self, width=300)
        self.frame5 = ttk.Frame(self, width=300)

        sql = "select player_name from players"
        players_name = list(c.execute(sql).fetchall())

        sql = "select player_id from players"
        players_id = list(c.execute(sql).fetchall())


        self.player_name_label = ttk.Label(self.frame1, text="name:")
        self.player_name_combo = ttk.Combobox(
            self.frame1,
            state="readonly"
            )
        # comboboxに選手名の一覧を表示
        self.player_name_combo["values"] = players_name

        self.select_btn = ttk.Button(
            self.frame1,
            text="select",
            command=lambda: mod.set_player_info(self, self.player_name_combo)
            )

        self.player_new_label = ttk.Label(self.frame2, text="new name:")
        self.player_new_entry = ttk.Entry(self.frame2)

        self.sex_label = ttk.Label(self.frame3, text="geschlecht:")
        self.sex_entry = ttk.Entry(self.frame3)

        self.age_label = ttk.Label(self.frame4, text="alter:")
        self.age_entry = ttk.Entry(self.frame4)

        self.team_label = ttk.Label(self.frame5, text="mannschaft:")
        self.team_entry = ttk.Entry(self.frame5)

        self.frame1.pack(fill="x", pady=12)
        self.player_name_label.pack(side="left")
        self.player_name_combo.pack(side="left")
        self.select_btn.pack()

        self.frame2.pack(fill="x", pady=2)
        self.player_new_label.pack(side="left")
        self.player_new_entry.pack(side="left")

        self.frame3.pack(fill="x", pady=2)
        self.sex_label.pack(side="left")
        self.sex_entry.pack(side="left")

        self.frame4.pack(fill="x", pady=2)
        self.age_label.pack(side="left")
        self.age_entry.pack(side="left")

        self.frame5.pack(fill="x", pady=2)
        self.team_label.pack(side="left")
        self.team_entry.pack(side="left")

        self.btn = ttk.Button(
            self,
            text="edit",
            command=lambda:mod.edit_player_master(self)
        )
        self.btn.pack()

class MasterInjuryE(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        s = ttk.Style()

        s.configure("A.TLabel", font=('Helvetica',18))

        # db接続
        con = sqlite3.connect("manage.db")
        c = con.cursor()

        sql = "select injury_name from injuries"
        injuries_name = list(c.execute(sql).fetchall())

        self.title_label = ttk.Label(self, text="Master_injury", style="A.TLabel")
        self.title_label.pack(pady=8)

        self.frame1 = ttk.Frame(self, width=300)
        self.frame2 = ttk.Frame(self, width=300)

        self.injury_name_label = ttk.Label(self.frame1, text="verletzungsart:")
        self.injury_name_combo = ttk.Combobox(
            self.frame1,
            state="readonly"
            )
        self.injury_name_combo["values"] = injuries_name

        self.new_label = ttk.Label(self.frame2, text="new verletzungsart:")
        self.new_entry = ttk.Entry(self.frame2)

        self.frame1.pack(fill="x", pady=8)
        self.injury_name_label.pack(side="left")
        self.injury_name_combo.pack(side="left")

        self.frame2.pack(fill="x", pady=8)
        self.new_label.pack(side="left")
        self.new_entry.pack(side="left")

        self.btn = ttk.Button(
            self,
            text="edit",
            command=lambda: mod.edit_master(self,"injuries")
        )
        self.btn.pack()

        con.close()

class MasterInjuryPartE(MasterInjuryE):
    def __init__(self, master=None):
        super().__init__(master)

        self.title_label["text"] = "Master injury part"
        self.injury_name_label["text"] = "korperteil:"
        self.btn["command"] = lambda: mod.edit_master(self,"injuries_parts")

        # db接続
        con = sqlite3.connect("manage.db")
        c = con.cursor()

        sql = "select injury_part_name from injuries_parts"
        injuries_name = list(c.execute(sql).fetchall())

        self.injury_name_combo["values"] = injuries_name

class MasterPositionE(MasterInjuryE):
    def __init__(self, master=None):
        super().__init__(master)

        self.title_label["text"] = "Master position"
        self.injury_name_label["text"] = "position:"
        self.btn["command"] = lambda: mod.edit_master(self,"positions")

        # db接続
        con = sqlite3.connect("manage.db")
        c = con.cursor()

        sql = "select position from positions"
        injuries_name = list(c.execute(sql).fetchall())

        self.injury_name_combo["values"] = injuries_name


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x700")

    # メニュー
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    menu_file = tk.Menu(root)
    menu_master = tk.Menu(root)
    menu_master_edit = tk.Menu(root)

    # フレーム
    all_frame = All(root)
    register_frame = Register(root)
    edit_frame = Edit(root)

    m_player_frame = MasterPlayer(root)
    m_injury_frame = MasterInjury(root)
    m_injury_part_frame = MasterInjuryPart(root)
    m_position_frame = MasterPosition(root)

    m_e_player_frame = MasterPlayerE(root)
    m_e_injury_frame = MasterInjuryE(root)
    m_e_injury_part_frame = MasterInjuryPartE(root)
    m_e_position_frame = MasterPositionE(root)

    # menubar file設定
    menubar.add_cascade(label="File", menu=menu_file)
    menu_file.add_command(label="register", command=lambda:mod.change_page(register_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_file.add_command(label="edit", command=lambda:mod.change_page(edit_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_file.add_command(label="all", command=lambda:mod.change_page(all_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    # menubar master 設定
    menubar.add_cascade(label="Master", menu=menu_master)
    menu_master.add_command(label="player", command=lambda:mod.change_page(m_player_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master.add_command(label="injury", command=lambda:mod.change_page(m_injury_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master.add_command(label="injury_part", command=lambda:mod.change_page(m_injury_part_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master.add_command(label="position", command=lambda:mod.change_page(m_position_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    # menubar master 設定
    menubar.add_cascade(label="Master_Edit", menu=menu_master_edit)
    menu_master_edit.add_command(label="player", command=lambda:mod.change_page(m_e_player_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master_edit.add_command(label="injury", command=lambda:mod.change_page(m_e_injury_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master_edit.add_command(label="injury_part", command=lambda:mod.change_page(m_e_injury_part_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))
    menu_master_edit.add_command(label="position", command=lambda:mod.change_page(m_e_position_frame, all_frame, register_frame, edit_frame,
        m_player_frame, m_injury_frame, m_injury_part_frame, m_position_frame,m_e_player_frame,m_e_injury_frame,m_e_injury_part_frame,m_e_position_frame
        ))

    # top_frame.tkraise()
    all_frame.pack()
    # register_frame.pack()
    root.mainloop()
