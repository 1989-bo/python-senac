

import pymysql

def conector():

    return pymysql.connect(

        host='localhost',
        user='root',
        password='',
        database='restaurante'
        
    )
