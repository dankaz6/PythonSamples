'''
Created on Sep 12, 2016

@author: kazsoft
'''

import json
from pandas import DataFrame, Series

def Ex1():
    path = '/home/kazsoft/PythonProjects/PythonSamples/src/root/nested/pydata/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    records = [json.loads(line) for line in open(path)]
    print records[0]
    print records[0]['tz']
    
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print time_zones[:10]
    
    
    
    
    
    
if (__name__ == "__main__"):
    # main()
    Ex1()
    
    
    
    