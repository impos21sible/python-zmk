import sqlite3
import telebot

bot = telebot.TeleBot("6786834594:AAFcsb-dKClQL_X0B3R5sbAY0ZedWQRH1lA")

# Создание базы данных SQLite и таблицы
def create_database():
    conn = sqlite3.connect('tg1base.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Groupa(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
                )
                ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        f TEXT,
        i TEXT,
        o TEXT,
        groupa INTEGER REFERENCES Groupa(id)
        )
        ''')

    conn.commit()
    conn.close()

def find_student(surname):
    conn = sqlite3.connect('tg1base.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student WHERE f=?", (surname,))
    student = cur.fetchall()
    conn.close()
    return student

# Вызываем функцию создания базы данных при старте
create_database()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Введите фамиллию: ")

@bot.message_handler(func=lambda message: True)
def handle_surname(message):
    surname = message.text.split()[0]  # Получаем только первое слово сообщения как фамилию
    students = find_student(surname)

    found = False
    for student in students:
        if student[1] == surname:
            bot.send_message(message.chat.id, f"Студент с фамилией {surname} учится в змк.")
            found = True
            break

    if found == False :
        bot.send_message(message.chat.id, f"Студент с фамилией {surname} не учится в змк.")




bot.polling()
