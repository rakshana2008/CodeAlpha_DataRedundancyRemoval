import sqlite3

DB = "data.db"

def setup():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)

def add_data(name, email):
    name = name.strip()
    email = email.strip().lower()

    if not name or "@" not in email or "." not in email:
        print("Invalid data: rejected")
        return

    with sqlite3.connect(DB) as conn:
        existing = conn.execute(
            "SELECT 1 FROM records WHERE name = ? OR email = ?",
            (name, email)
        ).fetchone()

        if existing:
            print("Redundant data: duplicate detected")
            return

        conn.execute(
            "INSERT INTO records (name, email) VALUES (?, ?)",
            (name, email)
        )
        print("Unique and verified data added successfully")

def view_data():
    with sqlite3.connect(DB) as conn:
        rows = conn.execute(
            "SELECT id, name, email FROM records"
        ).fetchall()

        print("\nStored Records:")
        for row in rows:
            print(row)

def main():
    setup()

    while True:
        print("\n--- Data Redundancy Removal System ---")
        print("1. Add Data")
        print("2. View Data")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_data(name, email)

        elif choice == "2":
            view_data()

        elif choice == "3":
            print("System closed")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
