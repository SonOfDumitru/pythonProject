import sqlite3

from sesiunea_19 import constants
#from.import constants

#->1
conn = sqlite3.connect(constants.DATABASE)
cursor=conn.cursor()
script = '''
CREATE TABLE IF NOT EXISTS Continents(
continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
code CHAR(2));
'''

cursor.execute(script)
conn.commit()
conn.close()
