"""
Corresponding Reducer code : age_first_code.py

This program is written to find the following:
- average age at which people start coding.
- at what age a person is likely to get into coding

"""
import sys

next (sys.stdin)

for line in sys.stdin:
    line=line.strip()
    line=line.split(',')
    print (line[4])