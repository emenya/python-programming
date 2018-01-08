from random import *
import math
marks = []
	for i in range(0,99):
		marks.append(round(uniform(1,99),2))
		print(marks)
mean = round((marks[math.floor(len(marks)/2)]+marks[math.floor((len(marks)+1)/2)])/2,2)
marks.sort()
median =(marks[math.floor(len(marks)/2)]+marks[math.floor((len(marks)+1)/2)])/2
sqrmarks=[]
	for value in marks:
		newvalue=(value-mean)**2
		sqrmarks.append(round(newvalue,2))
	variance = sum(sqrmarks)/(len(marks)-1)
	sd = (sum(sqrmarks)/(len(marks)-1))**(1/2)