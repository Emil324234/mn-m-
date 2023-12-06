import sqlite3


class DBEntity:
    pass
class Movie(DBEntity):
    def __init__(self, title, duration, ticket_cost):
        self._title(title)
        self._duration(duration)
        self._ticketcost(ticket_cost)

    def title(self, title):
        if title.strip():
            self._title = title
        else:
            raise ValueError("Название фильма не может быть пустым")

    def _duration(self, duration):
        if duration >= 0:
            self._duration = duration
        else:
            raise ValueError("Продолжительность фильма должна быть неотрицательным числом")

    def _ticketcost(self, ticket_cost):
        if ticket_cost > 0:
            self._ticketcost = ticket_cost
        else:
            raise ValueError("Стоимость билета должна быть положительным числом")

    def save_db(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("INSERT INTO Movies (title, duration, ticket_cost) VALUES (?, ?, ?)", (self._title, self._duration, self._ticketcost))
            conn.commit()
            conn.close()
            print("Фильм сохранен")
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении фильма в базу данных: {e}")

    def update(self, new_title):
        try:
            self._title(new_title)
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("UPDATE Movies SET title=? WHERE title=?", (self._title, self._title))
            conn.commit()
            conn.close()
            print("Данные фильма обновлены")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении данных фильма: {e}")

    def delete(self):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("DELETE FROM Movies WHERE title=?", (self._title,))
            conn.commit()
            conn.close()
            print("Фильм удален")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении фильма: {e}")

    @staticmethod
    def filter_by_duration(min_duration):
        try:
            conn = sqlite3.connect('cinema.db')
            c = conn.cursor()
            c.execute("SELECT * FROM Movies WHERE duration >= ?", (min_duration,))
            result = c.fetchall()
            conn.close()
            return result
        except sqlite3.Error as e:
            print(f"Ошибка при фильтрации фильмов: {e}")

    def display_info(self):
        return f"Фильм: {self._title}, Продолжительность: {self._duration}, Стоимость билета: {self._ticketcost}"
