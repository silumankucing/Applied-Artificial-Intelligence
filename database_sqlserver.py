import pyodbc

com = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                     'SERVER=REACTIVEARMOUR/TEW_SQLEXPRESS;'
                     'Database=DataLab;'
                     'Trusted_Connection=yes;')

kur = com.cursor()
kur.execute('SELECT * FROM Datalab.dbo.datalab_table')

for row in kur:
    print(row)