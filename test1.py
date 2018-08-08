#import unittest
#from unittest import TestCase
#from mock import patch, Mock

import mysql.connector
import json,string



READER_CONFIG = json.loads(open('readers/database_connection.json').read()) # connection to database config  
READER_CONFIG1 = json.loads(open('readers/config_tests_tables.json').read())   # config of tables

READER_CONFIG2 = json.loads(open('readers/config_tests.json').read())   # config of tests




class Mysqldatabase(object):

    def __init__(self, host, port, user, password, dbname,
                query=None):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        

        self.query = query

        self.conn = None
        self.cursor = None

        #self.test_column = test_column
        #self.tablename = tablename


    def validate_tests(self, test_name=None, test_table_name=None, test_column=None , query=None):
        """
        """
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.dbname
        )
        
        self.test_name = test_name
        self.test_table_name = test_table_name
        self.test_column = test_column

        query = string.replace(query,'replace_table', self.test_table_name)
        query = string.replace(query,'replace_column', self.test_column)
        
        self.query = query
        print self.query

        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query)

        return self.cursor


reader = Mysqldatabase(**READER_CONFIG['green'])

New_config = dict ( READER_CONFIG1['test_table_1'][0].items() + READER_CONFIG2['column_unique_tests'].items() )
var = reader.validate_tests ( ** New_config )  # input two configs as a single config into validate_tests fuction

results = var.fetchall()
print results


