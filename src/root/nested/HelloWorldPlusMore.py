'''
Created on Sep 8, 2016

@author: dan
'''

import random
from random import choice
from datetime import time
from datetime import datetime
from Shapes import Triangle
from Shapes import Rectangle
import os
import json

def main():
    print "Hello World!"
    
    x = 5
    y = 3
    plus = x + y
    
    if (plus < 7):
        print "sum is less than 7"
    elif (plus > 7):
        print "sum is greater than 7"
    else:
        print "sum is equal to 7"
        
    print "end of the math test"
    
    s = "Hello "
    s5 = s * 5
    
    print s5
    
    prompt_user = False
    
    if (prompt_user):
        name = raw_input("Please enter your name:")
    else:
        name = "Timmy Tester"
        
    print "Hello " + name + "!"
    
    template1 = "the values are {0}, {1} and {2}"
    print template1.format("one", "two", "three")

    template2 = "the meat is {meat}, the vegetable is {veggie}, the dessert is {dessert}"
    print template2.format(veggie="green beans", dessert="apple pie", meat="chicken")
    
    color_list = ["red", "green", "blue", "purple"]
    print "Number of colors: ", len(color_list)
    print "Number of blue items: ", color_list.count("blue")
    print "Red in color list: ", "red" in color_list
    
    color_list.append("yellow")
    color_list.append("white")
    more_colors = ["black", "brown", "aqua"]
    color_list.extend(more_colors)
    print "Number of colors: ", len(color_list)
    color_list.sort()
    print "First color: ", color_list[0]
    
    for c in color_list:
        print "One color is: ", c
        
    for i in range(3):
        print i 
        
    j = 0    
    while (j < 4):
        print j, square(j)
        j += 1    
        
    my_players = {"Ryan":"tight end", "Joe":"halfback", "Troy":"guard"}
    print "Joe plays: ", my_players["Joe"]
    print "Ryan plays: ", my_players["Ryan"]
    print "Troy plays: ", my_players["Troy"]
    print "Check Herbie: ", my_players.has_key("Herbie")
    
    food1 = Food("apple", "fruit")
    food2 = Food("chicken", "meat")
       
    print "name of food1: ", food1.name  
    print "name of food2: ", food2  # use __str__ method
        
    for i in range(10):
        print random.randint(1, 100), random.random(), random.uniform(1, 100)    

    print "One of the colors is: ", choice(color_list)
    lunch = time(11, 30)
    print "Lunch is at: ", lunch
    print "The current time is: ", datetime.now()
    
# test the objects from the other class file    
    tri = Triangle()
    print "My ", tri , " has this many sides: ", tri.number_sides
    rect = Rectangle()
    print "My ", rect , " has this many sides: ", rect.number_sides
    
    help(tri)
    
    file_name_text = "/home/kazsoft/Documents/test1.txt" 
    file_name_json = "/home/kazsoft/Documents/test1.json" 
    
    f = open(file_name_text, "w")
    f.write("Hello World!\n")
    f.write("second line\n")
    f.close()
    
    stats = os.stat(file_name_text)
    print datetime.fromtimestamp(stats.st_atime)
    
    f = open(file_name_text, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        print "Line in file: ", line
        
    
    f = open(file_name_json, "w")
    json.dump(vars(food1),f)
    f.close()
    

def square(x):
    return x * x

class Food(object):

        name = ""
        food_group = ""

        def __init__(self, name, food_group):
            self.name = name
            self.food_group = food_group
        
        def __str__(self):
            return self.name
    

if (__name__ == "__main__"):
    main()
