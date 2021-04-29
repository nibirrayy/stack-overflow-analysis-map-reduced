"""
Corresponding Reducer code : age_first_code.py

This program is written to find the following:
- average age at which people start coding.
- at what age a person is likely to get into coding

"""

import sys
import re

age_wise_distribution = {
    "youger than 10" : 0,
    "10 to 11 years old" : 0,
    "12 to 13 years old" : 0,
    "14 to 15 years old" : 0,
    "16 to 17 years old" : 0,
    "18 to 19 years old" : 0,
    "20 to 21 years old" : 0,
    "22 to 23 years old" : 0,
    "24 to 25 years old" : 0,
    "26 to 27 years old" : 0,
    "28 to 29 years old" : 0,
    "30 years old or older" : 0
}

number_of_people=0
total_of_age=0

# regular expressions
young_regex = "(y|Y)oung.{0,}[0-9].{0,}"
old_regex = "(O|o)ld.{0,}[0-9].{0,}"

# function that takes a string and return the number in that string
def extract_number(string):
    temp = re.findall('\d+',string)[0]
    return temp

# This function checks whetather the data sys older or younger
def young_old_check(string):
    
    
    check = False 
    bit = False # True means younger and false mean old
    temp = 0
    
    if re.search(young_regex,age):
        check = True
        bit = True
        temp = extract_number(age)

    elif re.search(old_regex,age):
        check = True
        bit = False
        temp = extract_number(age)

    return  check,bit,temp

def assign_to_grp(number):

    if (number<10):
        age_wise_distribution["youger than 10"]+=1

    elif (number>=10 and number <=11):
        age_wise_distribution["10 to 11 years old"]+=1
    
    elif (number>=12 and number <=13):
        age_wise_distribution["12 to 13 years old"]+=1

    elif (number>=14 and number <=15):
        age_wise_distribution["14 to 15 years old"]+=1

    elif (number>=16 and number <=17):
        age_wise_distribution["16 to 17 years old"]+=1

    elif (number>=18 and number <=19):
        age_wise_distribution["18 to 19 years old"]+=1

    elif (number>=20 and number <=21):
        age_wise_distribution["20 to 21 years old"]+=1

    elif (number>=22 and number <=23):
        age_wise_distribution["22 to 23 years old"]+=1

    elif (number>=24 and number <=25):
        age_wise_distribution["24 to 25 years old"]+=1

    elif (number>=26 and number <=27):
        age_wise_distribution["26 to 27 years old"]+=1

    elif (number>=28 and number <=29):
        age_wise_distribution["28 to 29 years old"]+=1

    elif(number>=30):
        age_wise_distribution["30 years old or older"]+=1



for age in sys.stdin:
    age = age.replace("\n", "")

    if (age =="NA"):
        continue

    x,y,z = young_old_check(age)
    if x:
        total_of_age+=int(z)
        number_of_people+=1

        if y:
            assign_to_grp(int(z))
        else:
            z = int(z) + 1
            assign_to_grp(z)
    else:
        total_of_age = int(age)
        number_of_people+=1
        assign_to_grp(int(age))


# this hold the average age
# average = total_of_age / number_of_people
# print (average)

print("-"*100)
print ("{:<30} | {:<30}".format('AGE','COUNT')) # This is used to print the table headers
print("-"*100)

for age, count in age_wise_distribution.items():
    print ("{:<30} | {:<30}".format(age,count)) 


print("-"*100)

