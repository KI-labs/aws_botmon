#!/usr/bin/python
import psycopg2
from config import dbconfig


class DBHelper:

    def __init__(self):
        self.conn = self.connect()
        self.cursor = None

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # read connection parameters
            params = dbconfig()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            self.cursor = conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                return conn
                # conn.close()
                # print('Database connection closed.')

    def execute(self, query):
        # execute a statement
        print('executing query:', query)
        self.cursor.execute(query)

    def close(self):
        """ Disconnect from the PostgreSQL database server """
        self.conn.close()
        print('Database connection closed.')





