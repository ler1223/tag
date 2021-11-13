import sqlite3
import hashlib


def entrance(login, new_password):
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()
    result = cursor.execute("""SELECT password FROM users
                WHERE login = ?""", (login,)).fetchall()
    cursor.close()
    DB.close()
    password = result[0][0]
    if password == new_password:
        return True
    else:
        return False


def registring(name, login, password):
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()

    # salt = os.urandom(32)
    # hashed_password = hash_password(password, salt)
    sql = """INSERT INTO users  (name, login, password) VALUES ("{}", "{}", "{}");""".format(name, login, password)
    cursor.execute(sql)
    DB.commit()
    result = cursor.execute("""SELECT id FROM users
                        WHERE login = ?""", (login,)).fetchall()
    id_user = int(result[0][0])
    cursor.execute("""INSERT INTO statistic (id_user) VALUES (?);""", (id_user,))
    DB.commit()
    if result:
        return True
    else:
        return False


def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode(), 100000)

    storage = salt + key.decode()

    return storage


def get_name(login):
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()
    result = cursor.execute("""SELECT name FROM users
                    WHERE login = ?""", (login,)).fetchall()
    return result[0][0]


def set_statistic(restart, win, game):
    id_user = get_id()
    lost_restart, lost_win, lost_game = get_statistic()
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()
    restart += lost_restart
    win += lost_win
    game += lost_game
    cursor.execute("""UPDATE statistic SET restart = ?, win = ?, game = ? WHERE id_user = ?;""",
                   (restart, win, game, id_user))
    DB.commit()


def get_statistic():
    id_user = get_id()
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()
    result = cursor.execute("""SELECT restart, win, game FROM statistic
                        WHERE id_user = ?""", (id_user,)).fetchall()
    restart = int(result[0][0])
    win = int(result[0][1])
    game = int(result[0][2])
    return restart, win, game


def get_id():
    login = get_login()
    DB = sqlite3.connect("DB.db")
    cursor = DB.cursor()
    result = cursor.execute("""SELECT id FROM users
                        WHERE login = ?""", (login,)).fetchall()
    return result[0][0]


def get_login():
    file = open("user.txt", mode="r")
    email = str(file.readlines()[1]).strip()
    return email
