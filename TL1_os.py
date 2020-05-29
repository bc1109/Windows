import os
import json
import sys


if os.path.isfile('C:\\TACLAN\\Config\\JSONs\\dtconfig.init.json'):
    #print('Parsing the dtconfig json file')
    json_file = open("dtconfig.init.json")
    dtconfig = json.load(json_file)
    json_file.close()
else:
    #print('There is an issue with locating the dtconfig.json file!')
    sys.exit('There is an issue with locating the dtconfig.json file!')
