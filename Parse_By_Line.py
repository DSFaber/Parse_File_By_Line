##This script looks at a path for a dated file, then parses it by row into two different files/folders based on fields being blank within each row.

import os.path
from datetime import date

##sets date variables/format
today = date.today()
todayFormatted = today.strftime("%m%d%Y")
print(todayFormatted)

##Sets variable for the base file name 
basefilename = "PartOfFileNameYouAreLookingFor"


basepath = '\\\\Test/Path/Base/'
type1_path = '\\\\Test/Path/Base/Type1'
type2_path = '\\\\Test/Path/Base/Type2'

filename = basefilename + todayFormatted + '.txt'

os.chdir(basepath)
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        content = f.read().splitlines()

def parse():
    for line in content:
        if line[40:60] != "                    ":  ##This usecase looks for a specific field/position in a file row to be blank
##            print(line[40:60])
            os.chdir(type1_path)
            open('Type1Results.txt', 'a').write(line + '\n')
        elif line[40:60] == "                    ":
            os.chdir(type2_path)
            open('Type2Results.txt', 'a').write(line + '\n')    

parse()
