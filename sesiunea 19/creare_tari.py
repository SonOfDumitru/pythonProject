import sqlite3

from sesiunea_19 import constants
#from.import constants

# -> 3
conn = sqlite3.connect(constants.DATABASE)
cursor=conn.cursor()
script = '''
CREATE TABLE IF NOT EXISTS Countries(
code CHAR(2) PRIMARY KEY,
name TEXT,
continent_id INTEGER,
population INTEGER,
FOREIGN KEY (continent_id) references continents (continent_id));
'''

cursor.execute(script)
conn.commit()
conn.close()
