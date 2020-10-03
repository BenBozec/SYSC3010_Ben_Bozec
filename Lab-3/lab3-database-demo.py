import sqlite3

date = "2020-10-01";
time = "14:00:00";
zone = "garage";
temperature = 0.0;

dbconnect = sqlite3.connect("mydatabase.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

for i in range(10):
    temperature += 1.1;
    cursor.execute('insert into temps values (?, ?, ?, ?)',
                   (date, time, zone,temperature));
dbconnect.commit();

cursor.execute('SELECT * FROM temps');

for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );

cursor.execute('CREATE TABLE sensors (sensorID NUMERIC, type TEXT, zone TEXT)');
cursor.execute('INSERT INTO sensors values(1, "door", "kitchen")');
cursor.execute('INSERT INTO sensors values(2, "temperature", "kitchen")');
cursor.execute('INSERT INTO sensors values(3, "door", "garage")');
cursor.execute('INSERT INTO sensors values(4, "motion", "garage")');
cursor.execute('INSERT INTO sensors values(5, "temperature", "garage")');
dbconnect.commit();

cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');

for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

cursor.execute('SELECT * FROM sensors WHERE type="door"');

for row in cursor:
        print(row['sensorID'],row['type'],row['zone']);


dbconnect.close();
