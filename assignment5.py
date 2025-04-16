# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Enjie Jones
# Assignment Number: Assignment 5
# Due Date: 4/18/2025
# Purpose: What does the program do (in a few sentences)? This program takes a list of days and temperatures, and utilizes a sqlite connector in order to put these into a database. Then this stored database can be queried using SQL, like in this case with the average temperature.
# List Specific resources used to complete the assignment. https://www.sqlitetutorial.net/sqlite-python/creating-tables/ https://docs.python.org/3/library/sqlite3.html
import sqlite3

con = sqlite3.connect("input.db") #intialize sqlite database

cur = con.cursor()

#new table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Temp (
    id INTEGER PRIMARY KEY, 
    Day_Of_Week TEXT, 
    Temperature_Value REAL
    )
""")

with open ('Assignment5input.txt') as file:
    for line in file:
        day, temp = line.split() #split the text file into two parts called day and temp
        cur.execute('INSERT INTO Temp (Day_Of_Week, Temperature_Value) VALUES (?, ?)', (day, temp)) #insert our day and temp values into sql database
    con.commit()

for day in ['Sunday','Thursday']:
    cur.execute('SELECT AVG(Temperature_Value) FROM Temp WHERE Day_Of_Week = ?', (day,)) #select the average of all temperature values when the day of the week matches the value i selected
    avg = cur.fetchone()[0]
    print(f'Average temperature for {day}: {avg:.1f}') #print average temperature using f strings
con.close()

