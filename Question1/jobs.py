'''
Created on Apr 16, 2014

In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. Download the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length) or decreasing order of the ratio (weight/length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

@author: J.Wang
'''
f = open("jobs.txt")
linenum = f.readline()
arr = [(0,0)]*int(linenum)
index = 0
for line in f:
    arr[index]  = tuple([int(x) for x in line.split()])  
    index+=1
 
# decreasing order of the difference    
# sorted_arr = sorted(arr, key=lambda tup: (tup[0]-tup[1],tup[0]) , reverse = True)
# decreasing order of the ratio
sorted_arr = sorted(arr, key=lambda tup: (float(tup[0])/tup[1],tup[0]) , reverse = True)
#print sorted_arr
sum = 0
current_time = 0
for elem in sorted_arr:
    current_time += elem[1]
    sum += elem[0] * current_time
print sum
 
