import happybase as hb

connection = hb.Connection()
connection.open()

column_names = {"personal" : dict(), "professional": dict(), "custom": dict()}
powers = connection.create_table("powers", column_names)

column_names = {"nutrition": dict(), "taste": dict()}
food = connection.create_table("food", column_names)

connection.close()
