#######################
#######################
# DateTime Extraction #
#######################
#######################

# Python3 code to demonstrate working of
# Detect date in String
# Using re.search() + strptime()
import re
from datetime import datetime

# initializing string
test_str = "gfg at 2021-01-04"

# printing original string
print("The original string is : " + str(test_str))

# searching string
match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)

# computed date
# feeding format
res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()

# printing result
print("Computed date : " + str(res))


# Python3 code to demonstrate working of
# Detect date in String
# Using python-dateutil()
from dateutil import parser

# initializing string
test_str = "gfg at 2021-01-04"

# printing original string
print("The original string is : " + str(test_str))

# extracting date using inbuilt func.
res = parser.parse(test_str, fuzzy=True)

# printing result
print("Computed date : " + str(res)[:10])


test_str = "gfg at 2021-01-04"

# Split the input string into words and iterate through them
words = test_str.split()
for word in words:
    if len(word) == 10 and word[4] == "-" and word[7] == "-":
        print(word)
        break
    
    
string = 'gfg at 2021-01-04'
date = "-".join(string.split()[-1].split("-"))
print("Computed date:", date)


import re

string = 'gfg at 2021-01-04'

date = re.findall('\d{4}-\d{2}-\d{2}', string)[0]

print("Computed date:", date)
