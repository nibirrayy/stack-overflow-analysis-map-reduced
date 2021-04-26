import sys
import csv

next(sys.stdin)

for line in csv.reader(sys.stdin):

# line[22] is LnaguageWorkedWith and line[21] is languagedDesiredNExtYear

    line = line[22].strip()
    line = line.split(',')
    # print(line)
    for lang in line:
        print(lang)
    