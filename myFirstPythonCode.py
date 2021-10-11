#! /usr bin/python
# -*- coding: utf-8 -*-
#
# How to RUN: 
# 1) Right-click anywhere in the editor window and select Run Python File in Terminal / "Python Datei im Terminal ausführen" 
# 2) mark lines, shift + enter
#    Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. 
#    This command is convenient for testing just a part of a file.
# 3) From the Command Palette (Ctrl+Shift+P), select the Python: Start REPL command to open a REPL terminal for the currently selected Python interpreter. 
#    In the REPL, you can then enter and run lines of code one at a time.

# String experiments
from re import match, search


msg = "Hello Daniel"
print(msg[-3:]+msg)

# Given the variables s and t defined as:
# s = 'Accelerate'
# t =  'Adventure'
# Write Python code that prints out 'Accenture' without using any quote 
# character in your code.
s = 'Accelerate'
t =  'Adventure'

print(s[:3]+t[3:])

# Assume text is a variable that holds a string. Write Python code that 
# prints out the position of the second occurrence of 'zip' in text, 
# or -1 if it does not occur at least twice.
# For example,
#   text = 'all zip files are zipped' -> 18
#   text = 'all zip files are compressed' -> -1
import re

text = 'all zip files are zigpped test zip zigpper'
strgToFind = 'zip'
nrOfPos = 2

countedStrToFind = text.count(strgToFind)
startPos = int(0)
endPos = len(text)-1

if countedStrToFind < nrOfPos: res = -1
else:
    for x in range(countedStrToFind):
        pos = re.search(strgToFind, text[startPos:endPos])
        startPos += pos.end()            
        if x == nrOfPos-1: 
            res = startPos-len(strgToFind)
print(res)
        

import re

text = 'all zip files are zipped test zip zipper'
strgToFind = 'zip'
pos = re.findall(strgToFind,text)  
print(pos)

#################
text = 'all zip zgip files zip are zipped test zip zigpper'
strgToFind = 'zip'
nrOfPos = 2

countedStrToFind = text.count(strgToFind)
startPos = int(-1)

if countedStrToFind < nrOfPos: res = -1
else:
    for x in range(countedStrToFind):
        startPos = text.find(strgToFind, startPos+1)  
        print(startPos)      
        if x == nrOfPos-1: res = startPos
print(strgToFind,' zum ',nrOfPos,'ten Mal geunden an Postion ',res)

##################     
text = 'all zip zgip files zip are zipped test zip zigpper'
strgToFind = 'zip'
nrOfPos = 3

res = text.split(strgToFind)
if len(res) > 1: 
    print( strgToFind,'zum',nrOfPos,'ten Mal geunden an Postion ',text.find(res[nrOfPos]) - len(strgToFind) )
else: print( -1 ) 

######################
text = 'all zip zgip files zip are zipped test zip zigpper'
strgToFind = 'zip'
nrOfPos = 3


if strgToFind in text: 
    print( strgToFind,'zum',nrOfPos,'ten Mal geunden an Postion ',res[nrOfPos-1])
else: print( -1 ) 

#####################
a = input('Bitte etwas eingeben')
print(a)

##############
# Given a variable, x, that stores the value of any decimal number, write 
# Python code that prints out the nearest whole number to x. Do not use 
# round() etc. 
# You can assume x is not negative.
# x = 3.14159 3 (not 3.0)
# x = 13.5 13 (not 13.0)
# x = 27.63 28 (not 28.0)

d = input('Bitte Dezimalzahl eingeben: ')
# d = "50.6665"
d = "0" + d + "0"
parts = d.split('.')
i = int(parts[0])
r = int(parts[1][0])
if r >= 5:
    i = i + 1
print(i) 

##################
"""
Define a procedure median, that takes three numbers as an input and 
returns the median!
print(median(11,310,21))
# ‐‐>21
"""
a = [11, 310, 21, 55, 200]
def median(list):
    list.sort()
    return list[int(len(list)/2)]
print(median(a))

##################
# Print out the list of countries and its capitals
countries = (
{'country':"United States",'capital':"Washington"}, 
{'country':"Germany", 'capital': "Berlin"}, 
{'country':"France", 'capital': "Paris", 'language': "French"}, 
{'country':"Spain", 'capital': "Madrid"}, 
)
for country in countries:
    print(f'{country.items()}') #country {'country'} capital {'capital'})

##################
# Print out the list of countries and its capitals
countries = (
{'country':"United States",'capital':"Washington"}, 
{'country':"Germany", 'capital': "Berlin"}, 
{'country':"France", 'capital': "Paris", 'language': "French"}, 
{'country':"Spain", 'capital': "Madrid"}, 
)
for country in countries:
    s = f"{country['country']}: {country['capital']}".center(35,' ')
    
    print(s) 

##################
# Print out the list of countries and its capitals
countries = (
{'country':"United States",'capital':"Washington"}, 
{'country':"Germany", 'capital': "Berlin"}, 
{'country':"France", 'capital': "Paris", 'language': "French"}, 
{'country':"Spain", 'capital': "Madrid"}, 
)

max_sl = 0
for country in countries:
    s_len = len(country['country'])
    if  s_len > max_sl:
        max_sl = s_len
        print(max_sl)

for country in countries:
    sl = f"{country['country']}".rjust(max_sl, ' ')
    sr = f"{country['capital']}".ljust(20,' ')
    
    print(sl + " : " + sr) 

#########

countries = (
{'country':"United States",'capital':"Washington"}, 
{'country':"Germany", 'capital': "Berlin"}, 
{'country':"France", 'capital': "Paris", 'language': "French"}, 
{'country':"Spain", 'capital': "Madrid"}, 
)
l = []
for list in countries:
    for k, v in list.items(): 
        l.append(v)
        if len(l)%2 == 0:     
            print(l[-2:])

#########



##############
print('sudoku-uebung:')
testsudoku = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]
 
 
def check_sudoku(sudoku):
    print('checking all rows.')
    for row in sudoku:
        assert set(row).__len__() == 9
 
    print('checking all columns.')
    for col in range(9):
        column = set()
        for row in sudoku:
            column.add(row[col])
        assert column.__len__() == 9
 
    print('checking all sectors.')
    for row in (0, 3, 6):
        for col in (0, 3, 6):
            sector = set()
            for row_offset in range(3):
                for col_offset in range(3):
                    sector.add(sudoku[row+row_offset][col+col_offset])
            try:
                assert sector.__len__() == 9
            except ValueError:
                print(sector)
 

 ###################
""" Exercise:
Define a function sum() that returns the median and the average of all 
parameters. 
"""
L = ([i for i in range(7)])

def medav(L = list()):
    L.sort()
    median = L[int(len(L)/2)]
    average = sum(L) / len(L)
    return (median, average)
     

m, a = medav(L)
print('L:', L, 'Median: ', m, 'Average: ', a) 


###################
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i
##############################
class Student:    
    def __init__(self, name):
        self._name = name

st = Student('Horst Dietrich')
st._name

############
"""Exercise
Write a class Student, with the following methods:
• constructor
• get_details(self)
• enroll(self, course)
• get_no_of_students(self)
• get_course_participants(self, course)
• __str__()
Take care of class vs. Instance variables.

"""

class Course:
    _student = Student()

    instances = []
    
    def __init__(self, title):
        self._title = title
        self._participants = set()
        self.__class__.instances.append(self)
        print('created Course: ' + self._title + ' of Class ' + str(self.__class__))
    
    def get_instances(self):
        print(str(self.instances))
        return self.instances

    # def create(self, title):
    #     self.__init__(self, title)

    def add_participant(self, student):
        self._student = student
        self._participants.append(student)
        print('Participant', student, 'added to Set:', self._participants)
    
#     def get_no_of_students(self):
#         no_of_students = len(self._participants)
#         print('No. of Students: ', no_of_students)
#         return no_of_students
    
#     def get_course_participants(self): 
#         print('Course-Participants', self._participants)
#         return self._participants
    
    def __str__(self):
        return 'Course-Title = ' + str(self._title) + 'Participants:' + str(self._participants)


class Student:
    """A class Student with constructor, get_details(self), enroll(self, course), 
       get_no_of_students(self), get_course_participants(self, course), __str__()
    """
    
    _courses_of_student = set()

    def __init__(self, name):
        self._name = name
    
    def get_details(self):
        print(self.__str__())
        # print(str(self))
        return self.__str__()
    
    def __str__(self):
        return 'Sudentname = ' + str(self._name) + 'Courses: ' + str(self._courses_of_student)
         
    
    def enroll(self, *course_title):
        self._courses_of_student.add(course_title)
        for title in course_title:
            print('title = ',)
            new_course = self.create_course(title)  
            new_course.add_participant(self)
    
    def create_course(self, course_title):
        if isinstance(course_title, Course) == False: 
            # check if there is an instance of this course already
            # if not: create course
            return Course(course_title)
        else:
            # course already exists
            return course_title, 'already exists!'

 



s = Student('Martin Schmidt')
s._name
s.enroll('Musik', 'Mathe', 'Kunst')
s.get_details()
# s.create_courses('Deutsch', 'Philosophie', 'Biologie')

print(Course.instances) 
Course.get_instances('Musik')



#Course.get_course_participants





