import sqlite3

conn = sqlite3.connect("Кинотеатр.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cdays (
               cdaysID INTEGER PRIMARY KEY,
               cday DATE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cinemaaddress (
               cinemaaddressID INTEGER PRIMARY KEY,
               caddress VARCHAR(100) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cinemasession (
               cinemasessionID INTEGER PRIMARY KEY,
               duration TIME NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ticketcosts (
               ticketcostsID INTEGER PRIMARY KEY,
               cost FLOAT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS visitors (
               visitorID INTEGER PRIMARY KEY,
               firstname VARCHAR(30) NOT NULL,
               lastname VARCHAR(30) NOT NULL,
               middlename VARCHAR(30) NOT NULL,
               cdaysID INTEGER,
               FOREIGN KEY (cdaysID) REFERENCES cdays(cdaysID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cinemas (
               cinemasID INTEGER PRIMARY KEY,
               title VARCHAR(30) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS films (
               filmsID INTEGER PRIMARY KEY,
               title VARCHAR(30) NOT NULL,
               cinemasessionID INTEGER NOT NULL,
               ticketcostsID INTEGER NOT NULL,
               FOREIGN KEY (cinemasessionID) REFERENCES cinemasession(cinemasessionID),
               FOREIGN KEY (ticketcostsID) REFERENCES ticketcosts(ticketcostsID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS maintable (
               maintableID INTEGER PRIMARY KEY,
               rowline INT NOT NULL,
               visitorID INTEGER,
               cinemasessionID INTEGER,
               filmsID INTEGER,
               FOREIGN KEY (visitorID) REFERENCES visitors(visitorID),
               FOREIGN KEY (cinemasessionID) REFERENCES cinemasession(cinemasessionID),
               FOREIGN KEY (filmsID) REFERENCES films(filmsID)
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
)
''')

conn.commit()

def register_user():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
    conn.commit()
    print("Регистрация прошла!")

print("Добро пожаловать кинотеатр! Сначала вам необходимо зарегистрироваться.")
register_user()

print("Перейти на кассу регистрации?: (Да/Нет)")

while True:
    register = input()
    if register == "Да":
        print("\t Вы прошли на кассу регистрации и вам выдали билет. После чего вам нужно было подойти и пробить билет.")
        break
    elif register == "Нет":
        print("\t Вы решили не покупать билет и покинули кинотеатр.")
        exit()
    else:
        print("Неверный ввод. Введите 'Да', чтобы продолжить или 'Нет', чтобы покинуть кинотеатр.")

print("После регистрации, вас послали пробивать билет у работника кинотеатра. Пробить билет?: (Да/Нет)")

while True:
    bilet = input()
    if bilet == "Да":
        print("\t Вы успешно пробили билет и вас пустили в кинозал, где вы удобно расположились и приготовились к просмотру фильма.")
        break
    elif bilet == "Нет":
        print("\t Вы решили не смотреть фильм и покинули кинотеатр.")
        exit()
    else:
        print("Неверный ввод. Введите 'Да', чтобы пробить билет и пройти в зал, или 'Нет', чтобы покинуть кинотеатр.")


conn.close()