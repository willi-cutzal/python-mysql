from fastapi import FastAPI
import mysql.connector as myc

mydb = myc.connect(
    host='localhost',
    user='root',
    password='password'
)

mycursor = mydb.cursor()

app = FastAPI()

@app.get("/")
def welcome():
    return "todo marcha bien"

@app.get("/databases")
def mostrar_db():
    mycursor.execute("show databases;")
    for i in mycursor:
        return i
