import psycopg2
import sys
import pprint

CLEANUP_DAYS = 30
def main():
	conn_string = "host='localhost' dbname='avacat' user='postgres' password='passw0rd'"

	conn = psycopg2.connect(conn_string)

	cursor = conn.cursor()

	query = "DELETE FROM avacatapp_resource WHERE DATE_PART('day', now() - last_viewed_date ) >= %s" % (CLEANUP_DAYS)
	print(query)
	cursor.execute(query)

	rowcount = cursor.rowcount

	print("%s resources have beed deleted." % (rowcount))

	conn.commit()
	cursor.close()
	conn.close()

if __name__ == "__main__":
	main()
