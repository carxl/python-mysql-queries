import mysql.connector
from decouple import config
from random import randint


dataBase = mysql.connector.connect(
  host=config('DATABASE_HOST'),
  user=config('DATABASE_USER'),
  password=config('DATABASE_PASS'),
  database=config('DATABASE_NAME')
)

# line to dummie data, can be removed
random = randint(1, 1000)

# preparing a cursor object
cursorObject = dataBase.cursor()

sql = "INSERT INTO tasks (title, description, status)\
VALUES (%s, %s, %s)"
val = (f"taks to do {random}", f"description task {random}", "new")

cursorObject.execute(sql, val)
dataBase.commit()

query = "SELECT * FROM tasks;"
cursorObject.execute(query)

myResult = cursorObject.fetchall()

for row in myResult:
    print(row)

# disconnecting from server
dataBase.close()
