import re

date = "20/03/2022"
    
pattern = '(?:\d+)[-/.](?:\d+)[-/.](?:20\d+|\d+)'
result = re.match(pattern, date)

if result:
    new_pattern = re.findall('(?:\d+)[-/.](?:\d+)[-/.](?:20\d+|\d+)', date)
    new_pattern = str(new_pattern)
    new_date = new_pattern.replace("/", ".").replace("-", ".")
    print(new_date)

else:
    new_pattern = '.'.join(date[i:i+2] for i in range(0, len(date), 2))
    replace_pattern = re.sub('.20', '', new_pattern)
    print(replace_pattern)


