import statistics
import numpy as np

aList = []

n = int(input("Enter number of values : "))

for i in range(0, n):
	val = int(input())

	aList.append(val)
	
print(aList)


#returns the sum of the values in the list
def sum(aList):
    total = 0
    for n in range(0, len(aList)):
        total = total + aList[n]
    return total
print ("The sum is: " + str(sum(aList)))
# returns the average of the values in the list
def mean(aList):
    average = sum(aList) / len(aList)
    return average
print ("The mean is: " + str(mean(aList)))
# returns the variance of the values in the list
def variance(aList):
    vari = statistics.variance(aList)
    return vari
print ("The variance is: " + str(variance(aList)))
# returns the standard deviation of the values in the list
def stdev(aList):
    standardDev = statistics.pstdev(aList)
    return standardDev
print ("The standard deviation is " + str(stdev(aList)))
#returns the value of the median
def median(aList):
    med = statistics.median(aList)
    return med
print ("The median is: " + str(median(aList)))
# returns the value of the first quartile
def quartile1(aList):
    q1 = np.quantile(aList, .25)
    return q1
print ("The 1st quartile is " + str(quartile1(aList)))
#returns the value of the third quartile 
def quartile3(aList):
    q3 = np.quantile(aList, .75)
    return q3
print ("The 3rd quartile is " + str(quartile3(aList)))
