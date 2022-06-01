import happybase as hb
import csv

connection = hb.Connection()
connection.open()

powers = connection.table("powers")
with open("input.csv") as file:
    for column in csv.reader(file):
        row = {
            "personal:hero" : column[1], "personal:power" : column[2], 
            "professional:name" : column[3], "professional:xp" : column[4], "custom:color" : column[5]
        }
        powers.put(column[0], row)
        
connection.close()
