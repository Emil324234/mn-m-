import sqlite3
class DBEntity:
    pass

class Polzovatel(DBEntity):
    def __init__(self, username, password):
        self._username = username
        self._password = password   

    @property
    def username (self):
        return self._username
    @username.setter
    def username(self, username):
        if len(username) >= 5:
            self._username = username
        else:
            raise ValueError("Имя должно быть")


    @property
    def password (self):
        return self._password
    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self._password = password
        else:
            raise ValueError("Пароль должен быть")

    def save_to_db(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("INSERT INTO Polzovatels (username, password) VALUES (?, ?)", (self._username, self._password))
            conn.commit()
            conn.close()
            print("Пользователь зарегистрирован")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении пользователя: {e}")

    def update(self, new_password):
        try:
            self.password = new_password
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("UPDATE Polzovatels SET password=? WHERE username=?", (self._password, self._username))
            conn.commit()
            conn.close()
            print("Пароль обновлен")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении пароля: {e}")

    def delete(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("DELETE FROM Polzovatels WHERE username=?", (self._username,))
            conn.commit()
            conn.close()
            print("Пользователь удален")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении пользователя: {e}")

    def display_info(self):
        return f"Пользователь: {self._username}"
