#! /usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hw")
args = parser.parse_args()

line = sys.stdin.readline()
while line:
    if "hw{0}_grades".format(args.hw) in line:
    	reader_grades = line
    	line = sys.stdin.readline()
    elif "hw{0}".format(args.hw) in line:
    	self_grades = line
    	line = sys.stdin.readline()
    else:
    	line =  sys.stdin.readline()

reader_grades= reader_grades.strip()
reader_grades = reader_grades.split('cs70 ')[1]
reader_grades = reader_grades.split(';')

feedback = reader_grades[-1]
reader_grades.remove(feedback)

self_grades= self_grades.strip()
self_grades = self_grades.split('cs70 ')[1]
self_grades = self_grades.split(';')

corresponding_self_grades = []
for reader_grade in reader_grades:
    for self_grade in self_grades:
    	if reader_grade[0:6] in self_grade:
    		corresponding_self_grades.append(self_grade)
print("\n Here are your released reader grades for Homework {0} and your self grades for comparison.\n".format(args.hw))

for i in range(len(reader_grades)):
    print("Reader grade: " + reader_grades[i])
    print("Your self grade: " + corresponding_self_grades[i] + "\n")
    	
print(feedback[1:])
