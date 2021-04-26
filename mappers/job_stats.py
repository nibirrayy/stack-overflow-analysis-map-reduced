""""

"""

import sys
import csv

next(sys.stdin)

data = sys.stdin.readlines()

for line in csv.reader(data):
    line = line[13].strip()
    line = line.split(',')
    # print(line)
    for jobs in line:
        print(jobs)
    
