import sqlite3
class DBEntity:
    pass

class Genre(DBEntity):
    def __init__(self, name):
        self._name(name)

    def _name(self, name):
        if name.strip():
            self._name = name
        else:
            raise ValueError("Название жанра не может быть пустым")

    def save_db(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("INSERT INTO Genres (name) VALUES (?)", (self._name,))
            conn.commit()
            conn.close()
            print("Жанр сохранен")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении жанра в базу данных: {e}")

    def update(self, new_name):
        try:
            self._name(new_name)
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("UPDATE Genres SET name=? WHERE name=?", (self._name, self._name))
            conn.commit()
            conn.close()
            print("Данные жанра обновлены")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении данных жанра: {e}")

    def delete(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("DELETE FROM Genres WHERE name=?", (self._name,))
            conn.commit()
            conn.close()
            print("Жанр удален")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении жанра: {e}")

    def display_info(self):
        return f"Жанр"