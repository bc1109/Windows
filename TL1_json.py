import json

json_file = open("dtconfig.init.json")

dtconfig = json.load(json_file)
json_file.close()

switchusername = (dtconfig['setup']['Network']['SwitchUser'])
switchpassword = (dtconfig['setup']['Network']['SwitchPW'])
switchip = (dtconfig['setup']['Network']['SwitchServerVLANIP'])

print('The following switch with an IP of ' + switchip + ' has a username of ' +
      switchusername + ' with the password of ' + switchpassword + '.')

# with open('dtconfig.init.json') as f:
#creds = json.load(f)
# for value in creds['setup']:
# print(value('Network'))

# ['Network']

# print(dtconfig['setup']['Network']['SwitchUser'])
