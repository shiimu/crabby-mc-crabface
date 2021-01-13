import json
from subprocess import check_output


checking = "dir"
docloc = "cd ~/Documents"
# copy directories
# cp -r Documents USB
def change():

        change_to = check_output(docloc, shell=True, universal_newlines=True)
        print(change_to)
        contents()

def contents():
        back = check_output(checking, shell=True, universal_newlines=True)
        with open('datadump.json', 'w')as json_file:
                json.dump(back, json_file)
                print(back)

#def getContents():
        #cop_command = "cp -r DOCUMENTS USB"
        #cop_do = check_output(cop_command, shell=True, universal_newlines=True)


def onExit():
        print('Done!')

change()
