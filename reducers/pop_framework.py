import sys

frameworks = {

}

popular_framework = ""
counter = 0

for framework in sys.stdin:

    framework = framework.replace("\n","")
    framework = framework.split(";")

    for item in framework:
        item = item.strip() # just removing whitespaces
        if (item in frameworks.keys()):
            frameworks[item]+=1
        else:
            frameworks[item]=1

# {:<10} --> gives padding to the right. Check this link for reference 
# https://mkaz.blog/code/python-string-format-cookbook/

print("-"*100)
print ("{:<30} | {:<30}".format('FRAMEWORK','COUNT')) # This is used to print the table headers
print("-"*100)
for framework, count in frameworks.items():
    print ("{:<30} | {:<30}".format(framework,count)) 
    if count>counter:
        counter=count
        popular_framework = framework

print("-"*100)

## Print inteseting stats
print(f'Most used framework is {popular_framework}')