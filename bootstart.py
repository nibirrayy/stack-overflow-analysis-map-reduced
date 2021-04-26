import os


def switch_case(argument):

    switch = {
            1:"os.system(\"cat data/survey_results_public.csv | python mappers/job_stats.py | python reducers/job_stats.py\")",
            2:"os.system(\"cat data/survey_results_public.csv | python mappers/loved_language.py | python reducers/loved_language.py\")",
            3:"os.system(\"cat data/survey_results_public.csv | python mappers/pop_famework.py | python reducers/pop_framework.py\")",
            4:"os.system(\"cat data/survey_results_public.csv | python mappers/popular_lang.py | python reducers/popular_lang.py\")",
            }

    return switch.get(argument,"print (\"Invaid Option selected\")")


# eval(switch_case(3))


def gui():
    
    #A list that contains all the options and will print auto
    options = [
        "1: Code to find job stats",
        "2: Code to find most loved language",
        "3: Code to find most popular framework",
        "4: Code to find the most used language in the industry",
              ]
    
    print ("-"*100)
    print("Select any option to run the corresponding mapper reducer program")
    for option in options:
        print(option)
    print ("-"*100)
    
    selection=int(input("Select a option: "))
    return selection




def main():
    selection = gui()
    while(selection!="print (\"Invaid Option selected\")"):
        eval(switch_case(selection))
        selection=gui()



main()