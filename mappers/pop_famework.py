import sys
import csv

next(sys.stdin)

for line in csv.reader(sys.stdin):

    line = line[24].strip()
    line = line.split(',')
    for framework in line:
        print(framework)
    