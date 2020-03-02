import sqlite3

con = sqlite3.connect("manage.db")

c = con.cursor()
c.execute("PRAGMA foreign_keys = 1")

# 選手マスタテーブル作成
create_table = """
create table players
(
    player_id integer primary key,
    player_name text not null,
    sex text,
    age integer,
    team text
);
"""

# SQLの発行
c.execute(create_table)


# けが名マスタテーブル作成
create_table = """
create table injuries
(
    injury_id integer primary key,
    injury_name text not null
);
"""

# SQLの発行
c.execute(create_table)

# けが部位マスタテーブル作成
create_table = """
create table injuries_parts
(
    injury_part_id integer primary key,
    injury_part_name text not null
);
"""

# SQLの発行
c.execute(create_table)

# ポジションマスタテーブル作成
create_table = """
create table positions
(
    position_id integer primary key,
    position text not null
);
"""

# SQLの発行
c.execute(create_table)

# 選手情報一覧マスタテーブル作成
create_table = """
create table players_info
(
    player_info_id integer primary key autoincrement,
    player_id integer not null,
    position_id integer,
    injury_id integer,
    injury_part_id integer,
    symptom text,
    injury_date text,
    cure_date text,
    riha_date text,
    injury_reason text,
    injury_place text,
    note text,
    delete_flag integer,
    created_datetime timestamp default (datetime(current_timestamp,'localtime')),
    foreign key(player_id) references players(player_id),
    foreign key(position_id) references positions(position_id),
    foreign key(injury_id) references injuries(injury_id),
    foreign key(injury_part_id) references injuries_parts(injury_part_id)
);
"""

# SQLの発行
c.execute(create_table)

select_sql = "select * from players"


con.commit()

con.close()
