import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()
table = connection.table("powers")

row1 = table.row("row1")

hero = row1[b"personal:hero"]
power = row1[b"personal:power"]
name = row1[b"professional:name"]
xp = row1[b"professional:xp"]
color = row1[b"custom:color"]

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

row19 = table.row("row19")

hero = row19[b"personal:hero"]
color = row19[b"custom:color"]

print('hero: {}, color: {}'.format(hero, color))

hero = row1[b"personal:hero"]
name = row1[b"professional:name"]
color = row1[b"custom:color"]
print('hero: {}, name: {}, color: {}'.format(hero, name, color))