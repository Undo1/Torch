from BeautifulSoup import BeautifulSoup
import mysql.connector
import config #Where we keep our passwords and stuff

cnx = mysql.connector.connect(user=config.MySQLUsername(), password=config.MySQLPassword(), host=config.MySQLHost(), database=config.MySQLDatabase())
cursor = cnx.cursor()

query = ("SELECT Body, Score FROM Posts WHERE PostTypeId=2 LIMIT 10")

cursor.execute(query)

for (Body, Score) in cursor:
	soup = BeautifulSoup(Body)
	for link in soup.findAll('a'):
	    print(link.get('href'))

cursor.close()
cnx.close()