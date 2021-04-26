import sys

langs = {

}

popular_lang = ""
counter = 0

for lang in sys.stdin:

    lang = lang.replace("\n","")
    lang = lang.split(";")


    for item in lang:
        item = item.strip() # just removing whitespaces
        if (item in langs.keys()):
            langs[item]+=1
        else:
            langs[item]=1

# {:<10} --> gives padding to the right. Check this link for reference 
# https://mkaz.blog/code/python-string-format-cookbook/

print("-"*100)
print ("{:<30} | {:<30}".format('LANG','COUNT')) # This is used to print the table headers
print("-"*100)
for lang, count in langs.items():
    print ("{:<30} | {:<30}".format(lang,count)) 
    if count>counter:
        counter=count
        popular_lang = lang

print("-"*100)

## Print inteseting stats
print(f'Most loved language is {popular_lang}')