""""

"""

import sys
import csv

next(sys.stdin)

for line in csv.reader(sys.stdin):
    line = line[13].strip()
    line = line.split(',')
    # print(line)
    for jobs in line:
        print(jobs)
    
