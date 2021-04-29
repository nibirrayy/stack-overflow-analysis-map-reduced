""""
Corresponding Reducer code : job_stats.py

Problem statement: Which is the most common job according to stack overflow developer survey
"""

import sys
import csv # Importing the csc module because of the structure of the the dataset and the column that is required

next(sys.stdin)

for line in csv.reader(sys.stdin):
    line = line[13].strip()
    line = line.split(',')
    # print(line)
    for jobs in line:
        print(jobs)
    
