import sqlite3
from pprint import pprint
from sesiunea_19 import constants

conn = sqlite3.connect(constants.DATABASE)
cursor=conn.cursor()

# -> 5


select_all_countries = '''
select * from countries
order by name;

'''
cursor.execute(select_all_countries)
pprint(cursor.fetchall())

count_all_countries = '''
select count(*) from countries;
'''
cursor.execute(count_all_countries)
pprint(cursor.fetchone())

# -> 6
print (50 * '*')

countries_population_20m= '''
select * from countries where population > 20;
'''
cursor.execute(countries_population_20m)
pprint(cursor.fetchall())

# -> 7
print (50 * '*')

countrie_starting_with_c = '''
select * from countries where name like 'C%';   
'''
# % -> inseamna orice altceva vine dupa c de exemplul

cursor.execute(countrie_starting_with_c)
pprint(cursor.fetchall())


conn.close()
