#in the simplest case of 2 webpages pointing to eachother
#calculate the page rank of each webpage

from array import *

matrix = [[1, 0], [0, 1]]
pr_a = 1
pr_b = 1
d = 0.85
cnt_a = 1
cnt_b = 1

while (pr_a + pr_b) / 2 != 1:
    pr_a = (1 - d) + d * pr_b / cnt_b
    pr_b = (1 - d) + d * pr_a / cnt_a

print('PageRank of page a is ', pr_a, 'PageRank of webpage b is ', pr_b)

numPages = input('Enter the number of webpages: ')
print("there are", numPages)

matrix = []
i=0
while i < int(numPages):
    matrix.append(0)
    i += 1

print (matrix)
