# CodeAlpha_DataRedundancyRemoval
A Python-based data redundancy removal system that identifies and eliminates duplicate data to reduce storage usage, improve data quality, and enhance database efficiency
import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT UNIQUE
)
""")

def add_data(data):
    try:
        cur.execute("INSERT INTO records (data) VALUES (?)", (data,))
        conn.commit()
        print("Unique data added successfully!")
    except sqlite3.IntegrityError:
        print("Duplicate data detected! Not added.")

def view_data():
    cur.execute("SELECT * FROM records")
    for row in cur.fetchall():
        print(row)

while True:
    print("\n1. Add Data\n2. View Data\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        data = input("Enter data: ").strip()
        if data:
            add_data(data)
        else:
            print("Data cannot be empty.")
    elif choice == "2":
        view_data()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

conn.close()
