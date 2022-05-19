import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Dhes\Downloads\Database01.accdb;')
    print("Database is Connected")

    user_id = 1
    FullName = 'Gerald Christian Balindan'
    database = connect.cursor()
    database.execute('update Table1 set FullName=? where id=?', (FullName, user_id))
    database.commit()
    print("Data is updated")

    user_id = 1
    Birthdate = '12/18/2002'
    database = connect.cursor()
    database.execute('update Table1 set Birthdate=? where id=?', (Birthdate, user_id))
    database.commit()
    print("Data is updated")

    user_id = 1
    Address = 'Carmona, Cavite'
    database = connect.cursor()
    database.execute('update Table1 set Address=? where id=?', (Address, user_id))
    database.commit()
    print("Data is updated")

    user_id = 1
    SemGrade = '89'
    database = connect.cursor()
    database.execute('update Table1 set SemGrade=? where id=?', (SemGrade, user_id))
    database.commit()
    print("Data is updated")

    user_id = 1
    Age = '19'
    database = connect.cursor()
    database.execute('update Table1 set Age=? where id=?', (Age, user_id))
    database.commit()
    print("Data is updated")


except pyodbc.Error:
    print("Error in Connection")