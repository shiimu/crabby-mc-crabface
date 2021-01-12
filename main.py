import json
from subprocess import check_output

checking = "dir"

back = check_output(checking, shell=True, universal_newlines=True)
print(back)
with open('datadump.json', 'w')as json_file:
        json.dump(back, json_file)
    

