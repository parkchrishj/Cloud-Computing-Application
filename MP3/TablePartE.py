import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()

table = connection.table("powers")

for key, data in table.scan(include_timestamp = True):
    # if key in (b"row1", b"row10", b"row11", b"row12", b"row13"):
    print('Found: {}, {}'.format(key, data))

connection.close()