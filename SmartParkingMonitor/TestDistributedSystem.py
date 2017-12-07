# @author Utkarsh Anand
import pymysql
import unittest, time
"""
connection = pymysql.connect(host = 'localhost', user='root',port=3306, password='')

try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE Parking')

finally:
    connection.close()

connection = pymysql.connect(host = 'localhost', user='root',port=3306, password='', db='parking')


try:
    with connection.cursor() as cursor:
        sqlQuery = 'CREATE TABLE IF NOT EXISTS spots(spotID INT, parked INT, overtime INT, tickets INT)'
        cursor.execute(sqlQuery)

finally:
    connection.close()

connection = pymysql.connect(host = 'localhost', user='root',port=3306, password='', db='parking')

try:
    with connection.cursor() as cursor:
        sqlQuery = 'INSERT INTO spots(spotID, parked, overtime, tickets) VALUES(%a,%a,%a,%a)'
        cursor.execute(sqlQuery,(int(1),int(0),int(0),int(0)))
        cursor.execute(sqlQuery,(int(2),int(0),int(0),int(0)))
        cursor.execute(sqlQuery,(int(3),int(0),int(0),int(0)))
        connection.commit()

finally:
    connection.close()
"""
connection = pymysql.connect(host = 'localhost', user='root',port=3306, password='', db='parking')
result = ''
parked1 =  ''
parked2 =  ''
parked3 =  ''

overtime1= ''
overtime2= ''
overtime3= ''
try:
    
    with connection.cursor() as cursor:
        sqlQuery1 = 'INSERT INTO spots(spotID, parked, overtime, tickets) VALUES(%a,%a,%a,%a)'
        sqlQuery = "SELECT * FROM spots"
        sqlQuery2 = "DELETE FROM spots WHERE spotID=%s"
        
        cursor.execute(sqlQuery1,(int(4),int(0),int(0),int(0)))
        cursor.execute(sqlQuery2,(int(4)))
        connection.commit()
        cursor.execute(sqlQuery)
        result = cursor.fetchall()
        #cararrived
        sqlQuery3= 'UPDATE spots SET parked= 1 WHERE spotID=%s'
        cursor.execute(sqlQuery3,(int(1)))
        sqlQuery4= 'SELECT parked FROM spots WHERE spotID=%s'
        parked1 = cursor.execute(sqlQuery4,int(1))
        
        cursor.execute(sqlQuery3,(int(2)))
        parked2 = cursor.execute(sqlQuery4,int(2))
        cursor.execute(sqlQuery3,(int(3)))
        parked3 = cursor.execute(sqlQuery4,int(3))

        #overtime
        sqlQuery5= 'UPDATE spots SET overtime= 1 WHERE spotID=%s'
        cursor.execute(sqlQuery5,(int(1)))
        sqlQuery6= 'SELECT overtime FROM spots WHERE spotID=%s'
        overtime1 = cursor.execute(sqlQuery6,int(1))
        
        cursor.execute(sqlQuery5,(int(2)))
        overtime2 = cursor.execute(sqlQuery6,int(2))
        cursor.execute(sqlQuery5,(int(3)))
        overtime3 = cursor.execute(sqlQuery6,int(3))
    

finally:
    connection.close()



class TestDistrubutedSystem(unittest.TestCase):
    
    def test_read(self):
        
        assert'((1, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (3, 0, 0, 0))',result

    def test_datastore(self): 
        assert'((1, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (3, 0, 0, 0), (4, 0, 0, 0))',result

    def test_carArrived1(self):
        assert'1',parked1
        
    def test_carArrived2(self):
        assert'1',parked2
        
    def test_carArrived3(self):
        assert'1',parked3
        
    def test_overLimit1(self):
        assert'1',overtime1
        
    def test_overLimit2(self):
        assert'1',overtime2
        
    def test_overLimit3(self):
        assert'1',overtime3
        
if __name__ == "__main__":
  unittest.main()
