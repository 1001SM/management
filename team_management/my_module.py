import main
import tkinter as tk
import openpyxl
import copy
import os
import datetime
import sqlite3

from tkinter import messagebox
from tkinter import ttk


def change_page(create_frame, *del_frames):

    for frame in del_frames:
        frame.pack_forget()

    create_frame.pack()

def refresh(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()
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

    self.name_combo["values"] = players_db
    self.position_combo["values"] = positions_db
    self.injury_kind_combo["values"] = injury_kind_db
    self.injury_part_combo["values"] = injury_part_db

    con.close()

def register(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    name = self.name_combo.get()
    position = self.position_combo.get()
    injury_kind = self.injury_kind_combo.get()
    injury_part = self.injury_part_combo.get()

    # name_idを取得
    sql = "select player_id from players where player_name=?"
    name_id = [i for i in c.execute(sql, (name,))]
    list_name_id = list(name_id[0])
    name = list_name_id[0]

    # injury_idを取得
    sql = "select injury_id from injuries where injury_name=?"
    if injury_kind:
        injury_id = [i for i in c.execute(sql, (injury_kind,))]
        list_injury_id = list(injury_id[0])
        injury_kind = list_injury_id[0]
    # injury_part_idを取得
    sql = "select injury_part_id from injuries_parts where injury_part_name=?"
    if injury_part:
        injury_part_id = [i for i in c.execute(sql, (injury_part,))]
        list_injury_part_id = injury_part_id[0]
        injury_part = list_injury_part_id[0]
    # potision_idを取得
    sql = "select position_id from positions where position=?"
    if position:
        position_id = [i for i in c.execute(sql, (position,))]
        list_position_id = list(position_id[0])
        position = list_position_id[0]

    symptom = self.injury_name_text.get("1.0", "end -1c")
    injury_date = self.injury_date_entry.get()
    cure_date = self.cure_date_entry.get()
    riha = self.riha_entry.get()
    how = self.how_text.get("1.0", "end -1c")
    injury_place = self.injury_place_entry.get()
    other = self.other_text.get("1.0", "end -1c")

    flag = 0

    # delete
    self.name_combo.set("")
    self.position_combo.set("")
    self.injury_kind_combo.set("")
    self.injury_part_combo.set("")
    self.injury_name_text.delete("1.0", "end")
    self.injury_date_entry.delete("0", tk.END)
    self.cure_date_entry.delete("0", tk.END)
    self.riha_entry.delete("0", tk.END)
    self.how_text.delete("1.0", "end")
    self.injury_place_entry.delete("0", tk.END)
    self.other_text.delete("1.0", "end")



    player_info_all = (
        name,
        position,
        injury_kind,
        injury_part,
        symptom,
        injury_date,
        cure_date,
        riha,
        how,
        injury_place,
        other,
        flag
        )
    # print(player_info_all)
    insert_sql = """
        insert into players_info(
            player_id,
            position_id,
            injury_id,
            injury_part_id,
            symptom,
            injury_date,
            cure_date,
            riha_date,
            injury_reason,
            injury_place,
            note,
            delete_flag
        ) values(
            ?,?,?,?,?,?,
            ?,?,?,?,?,?
        )
        """

    c.execute(insert_sql, player_info_all)
    # for i in c.execute("select * from players_info"):
    #     print(i)
    con.commit()
    con.close()

def set_player_info(self, p_name):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    # Entry削除処理
    self.sex_entry.delete(0, tk.END)
    self.age_entry.delete(0, tk.END)
    self.team_entry.delete(0, tk.END)

    name = p_name.get()

    if name == "":
        messagebox.showerror("error", "select name")
        return

    # sql = "select * from players where player_name = ? "
    # for i in c.execute(sql, (name,)):
    #     print(i)

    sql = "select * from players where player_name = ?"
    player_info_tuple = [i for i in c.execute(sql, (name,))]
    player_info_list = list(player_info_tuple[0])

    #情報が入っていないindexを抽出
    #情報が入っていないindexを抽出
    try:
        index = [i for i, x in enumerate(player_info_list) if x is None]
        #Noneを""に書き換え
        for i in index:
            player_info_list[i] = ""
    except TypeError:
        pass

    self.sex_entry.insert(tk.END, player_info_list[2])
    self.age_entry.insert(tk.END, player_info_list[3])
    self.team_entry.insert(tk.END, player_info_list[4])

    con.close()

def refresh_edit(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()
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

    self.name_combo["values"] = players_db
    self.position_combo["values"] = positions_db
    self.injury_kind_combo["values"] = injury_kind_db
    self.injury_part_combo["values"] = injury_part_db

    con.close()

def edit_info(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    name = self.name_combo.get()
    position = self.position_combo.get()
    injury_kind = self.injury_kind_combo.get()
    injury_part = self.injury_part_combo.get()

    # name_idを取得
    sql = "select player_id from players where player_name=?"
    name_id = [i for i in c.execute(sql, (name,))]
    list_name_id = list(name_id[0])
    name = list_name_id[0]

    # injury_idを取得
    sql = "select injury_id from injuries where injury_name=?"
    if injury_kind:
        injury_id = [i for i in c.execute(sql, (injury_kind,))]
        list_injury_id = list(injury_id[0])
        injury_kind = list_injury_id[0]
    # injury_part_idを取得
    sql = "select injury_part_id from injuries_parts where injury_part_name=?"
    if injury_part:
        injury_part_id = [i for i in c.execute(sql, (injury_part,))]
        list_injury_part_id = injury_part_id[0]
        injury_part = list_injury_part_id[0]
    # potision_idを取得
    sql = "select position_id from positions where position=?"
    if position:
        position_id = [i for i in c.execute(sql, (position,))]
        list_position_id = list(position_id[0])
        position = list_position_id[0]

    symptom = self.injury_name_text.get("1.0", "end -1c")
    injury_date = self.injury_date_entry.get()
    cure_date = self.cure_date_entry.get()
    riha = self.riha_entry.get()
    how = self.how_text.get("1.0", "end -1c")
    injury_place = self.injury_place_entry.get()
    other = self.other_text.get("1.0", "end -1c")

    flag = 0

    player_info_id = self.player_info_id

    player_info_all = (
        name,
        position,
        injury_kind,
        injury_part,
        symptom,
        injury_date,
        cure_date,
        riha,
        how,
        injury_place,
        other,
        flag,
        player_info_id
        )
    # print(player_info_all)
    update_sql = """
        update players_info set
            player_id = ?,
            position_id = ?,
            injury_id = ?,
            injury_part_id = ?,
            symptom = ?,
            injury_date = ?,
            cure_date = ?,
            riha_date = ?,
            injury_reason = ?,
            injury_place = ?,
            note = ?,
            delete_flag = ?
            where player_info_id = ?
        """

    c.execute(update_sql, player_info_all)
    print(c.execute("select * from players_info").fetchall())
    con.close()

def set_info_all(self, p_name):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    name = p_name.get()
    print(name)

    # 全Entryの値を削除
    self.sex_entry.delete(0, tk.END)
    self.age_entry.delete(0, tk.END)
    self.team_entry.delete(0, tk.END)
    self.injury_date_entry.delete(0, tk.END)
    self.cure_date_entry.delete(0, tk.END)
    self.riha_entry.delete(0, tk.END)
    self.injury_place_entry.delete(0, tk.END)

    # 全comboboxの値を削除
    self.position_combo.set("")
    self.injury_kind_combo.set("")
    self.injury_part_combo.set("")

    # 全textの値を削除
    self.injury_name_text.delete("1.0", "end")
    self.how_text.delete("1.0", "end")
    self.other_text.delete("1.0", "end")

    if name == "":
        messagebox.showerror("error", "select name")
        return

    sql = "select player_id from players where player_name = ?"
    player_id_tuple = [i for i in c.execute(sql, (name,))]
    player_id = list(player_id_tuple[0])[0]

    sql = """
    select
    player_name, sex, age,
    team, position, injury_name,
    symptom, injury_part_name, injury_date,
    cure_date, riha_date, injury_reason,
    injury_place, note, player_info_id,
    delete_flag, created_datetime
    from(((
        players_info
        inner join players on
        players_info.player_id = players.player_id
        and players_info.player_id = {}
        )
        inner join positions on
        players_info.position_id = positions.position_id
        )
        inner join injuries on
        players_info.injury_id = injuries.injury_id
    )
    inner join injuries_parts on
    players_info.injury_part_id = injuries_parts.injury_part_id
    where players_info.delete_flag = 0
    """

    # listに変換
    player_info_all_list = list(c.execute(sql.format(player_id)).fetchall()[0])
    print(player_info_all_list)

    #情報が入っていないindexを抽出
    try:
        index = [i for i, x in enumerate(player_info_all_list) if x is None]
        #Noneを""に書き換え
        for i in index:
            player_info_all_list[i] = ""
    except TypeError:
        pass


    self.sex_entry.insert(tk.END, player_info_all_list[1])
    self.age_entry.insert(tk.END, player_info_all_list[2])
    self.team_entry.insert(tk.END, player_info_all_list[3])
    self.position_combo.set(player_info_all_list[4])
    self.injury_kind_combo.set(player_info_all_list[5])
    self.injury_name_text.insert("1.0", player_info_all_list[6])
    self.injury_part_combo.set(player_info_all_list[7])
    self.injury_date_entry.insert(tk.END, player_info_all_list[8])
    self.cure_date_entry.insert(tk.END, player_info_all_list[9])
    self.riha_entry.insert(tk.END, player_info_all_list[10])
    self.how_text.insert("1.0", player_info_all_list[11])
    self.injury_place_entry.insert(tk.END, player_info_all_list[12])
    self.other_text.insert("1.0", player_info_all_list[13])

    # plyaer_info_idを渡す。
    self.player_info_id = player_info_all_list[14]
    con.close()

# all frame
def show_all(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    sql = """
    select
    player_name, sex, age,
    team, position, injury_name,
    symptom, injury_part_name, injury_date,
    cure_date, riha_date, injury_reason,
    injury_place, note, "player_info_id"
    from(((
        players_info
        inner join players on
        players_info.player_id = players.player_id
        )
        inner join positions on
        players_info.position_id = positions.position_id
        )
        inner join injuries on
        players_info.injury_id = injuries.injury_id
    )
    inner join injuries_parts on
    players_info.injury_part_id = injuries_parts.injury_part_id
    where players_info.delete_flag = 0
    """

    # for r in range(len(self.columns_id)):
    for i in self.tree.get_children():
        self.tree.delete(i)

    # players_info = list(c.execute(sql).fetchall())
    # print(players_info)
    for i,r in enumerate(c.execute(sql)):
        self.tree.insert("", "end", tags=i, values=r)
        if i & 1:
            self.tree.tag_configure(i,background="#CCFFFF")


    con.close()

# regiter Masters

def getValue(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    selected_items = self.tree.selection()
    if not selected_items:
        # Itemが選択されていない・・・
        return
    values = self.tree.item(selected_items[0])['values']
    print(values)

    value  = {"id":values[-1]}

    sql = """
        update players_info set
            delete_flag = 1
        where player_info_id = :id
        """

    c.execute(sql,value)

    print(c.execute("select * from players_info"))
    con.commit()
    con.close()


def register_m_player(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    name = self.player_name_entry.get()
    sex = self.player_sex_entry.get()
    age = self.player_age_entry.get()
    team = self.player_team_entry.get()

    # entry delete
    self.player_name_entry.delete(0, tk.END)
    self.player_sex_entry.delete(0, tk.END)
    self.player_age_entry.delete(0, tk.END)
    self.player_team_entry.delete(0, tk.END)

    insert_data = (name, sex, age, team)

    sql = """
        insert into players(
            player_name,
            sex,
            age,
            team
        ) values(
            ?,?,?,?
        )"""

    c.execute(sql,insert_data)

    print(c.execute("select * from players").fetchall())

    con.commit()
    con.close()

def register_m_others(self, m_name):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    name = self.injury_name_entry.get()

    # entry delete
    self.injury_name_entry.delete(0, tk.END)

    columns_name ={"injuries":"injury_name", "injuries_parts":"injury_part_name", "positions":"position"}
    print(m_name,columns_name[m_name])
    sql = """
        insert into '{}'(
            '{}'
        ) values(
            ?
        )""".format(m_name, columns_name[m_name])

    c.execute(sql,(name,))

    print(c.execute("select * from {}".format(m_name)).fetchall())

    con.commit()
    con.close()

# edit Masters
def edit_player_master(self):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    p_name = self.player_name_combo.get()
    new_name = self.player_new_entry.get()

    p_sex = self.sex_entry.get()
    p_age = self.age_entry.get()
    p_team = self.team_entry.get()

    self.player_new_entry.delete(0, tk.END)
    self.sex_entry.delete(0, tk.END)
    self.age_entry.delete(0, tk.END)
    self.team_entry.delete(0, tk.END)


    values = {"new_name": new_name, "p_name": p_name, "p_sex": p_sex, "p_age": p_age, "p_team": p_team}

    sql = """
        update players set
            player_name = :new_name,
            sex = :p_sex,
            age = :p_age,
            team = :p_team
        where player_name = :p_name
        """

    c.execute(sql, values)

    con.commit()
    con.close()

def edit_master(self, m_name):
    # db接続
    con = sqlite3.connect("manage.db")
    c = con.cursor()

    previousdata = self.injury_name_combo.get()
    new_name = self.new_entry.get()

    # combobox entry delete
    self.injury_name_combo.set("")
    self.new_entry.delete(0, tk.END)

    columns_name ={"injuries":"injury_name", "injuries_parts":"injury_part_name", "positions":"position"}
    print(m_name,columns_name[m_name])
    sql = "update {} set {} = '{}' where {} = '{}'".format(m_name, columns_name[m_name], new_name, columns_name[m_name], previousdata)

    c.execute(sql)

    print(c.execute("select * from {}".format(m_name)).fetchall())

    con.commit()
    con.close()


def output():
    pass
