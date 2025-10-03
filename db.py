'''Module to interact with SingleStore Cloud database and export query results to CSV'''
import os
import csv
import singlestoredb as s2
from dotenv import load_dotenv

load_dotenv(override=True)

def connect(connection_string: str):
    '''Setting up the connection with SingleStore database'''
    conn = s2.connect(connection_string)
    cursor = conn.cursor()
    return conn, cursor


def main():
    connection_string = os.environ['CONNECTION_STRING']

    connection, cursor = connect(connection_string)

    query = "SELECT * FROM events"
    cursor.execute(query)

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in cursor.description])  # write headers
        writer.writerows(cursor)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
