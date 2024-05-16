import csv
import sqlite3

con = sqlite3.connect('tg1base.db')
cur = con.cursor()

with open('Student.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] and row['f'] and row['i'] and row['o'] and row['groupa'] :
            cur.execute("INSERT INTO Student(id,f,i,o,groupa) VALUES (?,?,?,?,?)", (row['id'],row['f'],row['i'],row['o'],row['groupa']))


con.commit()
con.close()