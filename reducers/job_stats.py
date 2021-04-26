import sys

jobs = {

}

for job in sys.stdin:

    job = job.replace("\n","")
    job = job.split(";")


    for item in job:
        item = item.strip() # just removing whitespaces
        if (item in jobs.keys()):
            jobs[item]+=1
        else:
            jobs[item]=1

# {:<10} --> gives padding to the right. Check this link for reference 
# https://mkaz.blog/code/python-string-format-cookbook/

print("-"*100)
print ("{:<30} | {:<30}".format('JOB','COUNT')) # This is used to print the table headers
print("-"*100)
for job, count in jobs.items():
    print ("{:<30} | {:<30}".format(job,count)) 


print("-"*100)

## Print inteseting stats
