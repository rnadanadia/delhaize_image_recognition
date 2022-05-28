import re
import datetime

#change the date with the real dataset
date = ["20.09.2022", "31-08-23", "04/12/2030", "B01/20/25", "010325", "08092030"]



def date_recognition (x: list):
    
    pattern = re.compile('(?:0[1-9]|[12][0-9]|3[01])[-/.]?(?:0[1-9]|1[012])[-/.]?(?:20[22-55]|[22-25])')
    newlist = list(filter(pattern.match, x))
    
    new_date = [a.replace("/", ".").replace("-", ".") for a in newlist]
    return new_date

date_recognition = date_recognition(date)
#print(date_recognition)

'''
The func is for 8 digit date, for ex : 08092030 
it will strip the 20 (from 2030) and give the 
result 08.09.30
'''

def date_adjustment(date_recognition: list):
    string_date = ','.join(str(elem) for elem in date_recognition)
    find_date = re.findall(r'\d{8}', string_date)
    new_string_date = ''.join(find_date)
    new_date= '.'.join(new_string_date[i:i+2] for i in range(0, len(new_string_date), 2))
    replace_date = re.sub('.20', '', new_date)

    for i in range(len(date_recognition)):
        if date_recognition[i] == new_string_date:
            date_recognition[i] = replace_date
            return date_recognition

date_adjustment = date_adjustment(date_recognition)
#print(date_adjustment)
'''
The func is for 6 digit date, for ex : 010325 
it will give the result 01.03.25. If we directly 
replace the 6 digit before 8 digit, the function will 
also read the 8 digit therefore it's inaccurate.
'''
def date_final(date_adjustment: list):
    string_date_2 = ','.join(str(elem) for elem in date_adjustment)
    find_date_2 = re.findall(r'\d{6}', string_date_2)
    new_string_date_2 = ''.join(find_date_2)
    new_date_2= '.'.join(new_string_date_2[i:i+2] for i in range(0, len(new_string_date_2), 2))

    for i in range(len(date_adjustment)):
        if date_adjustment[i] == new_string_date_2:
            date_adjustment[i] = new_date_2
            return date_adjustment
    
date_final = date_final(date_adjustment)
print(date_final)
        
