import sqlite3

connect = sqlite3.connect('agolo.db')

cur = connect.cursor()


# Create Vehicle Table

cur.execute('''CREATE TABLE IF NOT EXISTS vehicle (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vtype TEXT,
                plate_number TEXT,
                vin TEXT
                )''')

# Create Driver Table
cur.execute('''CREATE TABLE IF NOT EXISTS driver (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT,
                address TEXT,
                vid INTEGER,
                FOREIGN KEY (vid) REFERENCES vehicle(id)
                )''')

connect.commit()
connect.close()