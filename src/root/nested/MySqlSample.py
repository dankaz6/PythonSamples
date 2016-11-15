'''
Created on Sep 20, 2016

@author: kazsoft
'''

import mysql.connector

def main():
    cnx = mysql.connector.connect(user='kazdb', password='kazdb',
                              host='192.168.0.13',
                              database='kaztest')
    cursor = cnx.cursor()
    
    query = "SELECT ColorId, ColorName FROM KazTestColors WHERE ColorId = 'R'"
    
    cursor.execute(query)
    
    for (ColorId, ColorName) in cursor:
        print("One color is {} with id={}".format(ColorName , ColorId))

    cursor.close()
    cnx.close()

def try2():
    cnx = mysql.connector.connect(user='kazdb', password='kazdb',
                              host='192.168.0.13',
                              database='kaztest')
    cursor = cnx.cursor()
    
    query = "SELECT OrderId, ColorId, SizeId FROM KazTestViewOrders WHERE State = 'MN' and SizeId='X'"
    
    cursor.execute(query)
    
    for (OrderId, ColorId, SizeId) in cursor:
        print("One order is {} {} {}".format(OrderId , ColorId, SizeId))

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()
    try2()
    
    
    