'''
Created on Sep 10, 2016

@author: kazsoft
'''

class BaseShape(object):
    ''' This is a base class for shapes that should not be instantiated directly
    '''
    
    number_sides = 0
    name = ""
    
    def __init__(self, number_sides, name):
        self.number_sides = number_sides
        self.name = name
        
    def __str__(self):
        return self.name

class Triangle(BaseShape):
    ''' This is a class for a triangle
    '''
    def __init__(self):
        super(Triangle, self).__init__(3, "triangle")
            
            
class Quadtralateral(BaseShape):
    def __init__(self, name):
        super(Quadtralateral, self).__init__(4, name)
    
    
class Rectangle(Quadtralateral):
    def __init__(self):
        super(Rectangle, self).__init__("rectangle")

