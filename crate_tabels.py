import sqlite3
db=sqlite3.connect('base.db')
cur=db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user (
            First_name text, 
            Last_name text,
            Login text,
            Password text,
            Class_Number text,
            Role text,
            key int,
            key2 int
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS food (
            food_name text,
            Food_voites int
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS admin (
            admin_choose text
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS user_eat(
            Login text,
            eat int
)""")

"""cur.execute("INSERT INTO food VALUES ('blini',0)")
cur.execute("INSERT INTO food VALUES ('borch',0)")
cur.execute("INSERT INTO food VALUES ('grechka',0)")
cur.execute("INSERT INTO food VALUES ('kasha',0)")
cur.execute("INSERT INTO food VALUES ('kotletka_s_pureshkoy',0)")
cur.execute("INSERT INTO food VALUES ('makaroni',0)")
cur.execute("INSERT INTO food VALUES ('pelmeni',0)")
cur.execute("INSERT INTO food VALUES ('perlovka',0)")
cur.execute("INSERT INTO food VALUES ('sasuges',0)")
cur.execute("INSERT INTO food VALUES ('zapikanka',0)")
db.commit()"""

"""cur.execute("INSERT INTO admin VALUES ('Afasf,asf,asff')")
for value in cur.execute("SELECT admin_choose FROM admin"):
    stroka=str(value[0]).split()
    print(stroka)"""

#cur.execute("DELETE FROM food")
db.commit()
cur.execute("SELECT * FROM food")
print(cur.fetchall())


""""user_first_name=input()
cur.execute(f"SELECT First_name FROM user WHERE First_name='{user_first_name}'")
if cur.fetchone() is None:
    cur.execute(f"INSERT INTO user VALUES (?,?,?,?,?,?,?)",(user_first_name,'anton','asd@gmail.com','123','11A','Plat',123))
    db.commit()
else:
    print('Такая запись уже есть')"""

db.close()
