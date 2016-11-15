'''
Created on Sep 16, 2016

@author: kazsoft
'''

import numpy as np

def ex1():
    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1)
    print arr1, arr1.dtype
    
    data2 = [[1,2,3,4],[5,6,7,8]]
    arr2 = np.array(data2)
    print arr2, arr2.ndim, arr2.shape, arr2.dtype
    
    print np.zeros((3,6))
    
    print np.empty((1,3,2))
    
    print np.arange(15)
    
    print np.identity(3, np.int64)
    
    numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
    print numeric_strings.astype(np.float) 
    
    
def ex2(): 
    arr1 =  np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr3 = np.array([[7],[8],[9]])
    print arr1 + 5, arr1 * 5
    print arr1 + arr2
    print arr1 * arr2  # be careful with this notation - multiplies each element, not matrix multiplcation1
    print np.dot(arr1,arr3) # matrix multiplication
    
    arr9 = np.random.randn(8)
    print arr9
    arr9.sort()
    print arr9
    np.save("numpy_test.npy", arr9)
    arr9_in = np.load("numpy_test.npy")
    print arr9_in
    
    
      

if __name__ == '__main__':
    # ex1()
    ex2()