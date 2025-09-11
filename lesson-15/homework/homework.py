import sqlite3

# Connect to a new SQLite database (or open if it exists)
conn = sqlite3.connect('animals.db')
cursor = conn.cursor()

# Create the Roster table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT NOT NULL,
        Species TEXT NOT NULL,
        Age INTEGER
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

print("✅ Database and table 'Roster' created successfully.")


#Populate your new table with the following values:
import sqlite3

# Connect to the database
conn = sqlite3.connect('animals.db')
cursor = conn.cursor()

# Data to insert
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

# Insert data into Roster table
cursor.executemany('''
    INSERT INTO Roster (Name, Species, Age)
    VALUES (?, ?, ?)
''', roster_data)

# Commit and close the connection
conn.commit()
conn.close()

print("✅ Roster table populated successfully.")

#Update the Name of Jadzia Dax to be Ezri Dax
import sqlite3

# Connect to the database
conn = sqlite3.connect('animals.db')
cursor = conn.cursor()

# Update the Name
cursor.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ("Ezri Dax", "Jadzia Dax"))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("✅ Name updated successfully.")
