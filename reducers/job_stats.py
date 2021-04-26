import sys

jobs = {

}

most_popular_job = ""
counter = 0

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
    if count>counter:
        counter=count
        most_popular_job = job


print("-"*100)

## Print inteseting stats
print(f'Most common job is {most_popular_job}')