import sqlite3

connection = sqlite3.connect('orders.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Couriers
(
    CourierID           INT PRIMARY KEY,
    Surname             TEXT,
    Name                TEXT,
    Patronymic          TEXT,
    PassportID          INT,
    DateOfBirth         DATE,
    DateOfEmployment    DATE,
    StartWorkDay        TIME,
    EndWorkDay          TIME,
    City                TEXT,
    Street              TEXT,
    House               TEXT,
    Flat                INT,
    Phone               TEXT
);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Transports
(
    CarNum              TEXT PRIMARY KEY,
    Brand               TEXT,
    DateOfRegistration  DATE,
    Color               TEXT
);
""")

connection.commit()

courier = (1, 'Dmitry', 'Yarisov', 'Alexandrovich', '4315894321', '2002-10-23', '2024-11-15', '09:00', '18:00', 'Kaliningrad', 'Repina Str.', '8', '17', '+7(938)651-31-29')
cursor.execute("INSERT INTO Couriers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", courier)
connection.commit()

car = ('A358CM', 'VolksWagen', '2020-02-10', 'Orange')
cursor.execute("INSERT INTO Transports VALUES (?,?,?,?);", car)
connection.commit()

car_update = ('BMW', 'B831HT')
cursor.execute("UPDATE Transports SET BRAND = ? WHERE CARNUM = ?;", car_update)
connection.commit()