import yaml
import json
import os
import sys


if os.path.isfile('Additional_VLANs.yml'):
    vlanfile = open("Additional_VLANs.yml")
    parsed_vlanfile = yaml.load(vlanfile, Loader=yaml.FullLoader)
    # need to see if we have to close this - could be the dump but looks like an additional way to parse the yaml file further.
    # need to find out how to close this file since we now have it within the parsed_vlanfile variable.
else:
    # if this is true I want to stop the script bc the script will error out.
    #print('There is an issue with locating the Additional_VLANs.yml file!')
    sys.exit('There is an issue with locating the Additional_VLANS.yml file!')

# Define YAML Values
# for loop would probably be ideal here. this will work for now.
FirstVLANname = (parsed_vlanfile.get('V1name'))  # - this worked.

# DTECH JSON Begin
if os.path.isfile('C:\\TACLAN\\Config\\JSONs\\dtconfig.init.json'):
    #print('Parsing the dtconfig json file')
    json_file = open("dtconfig.init.json")
    dtconfig = json.load(json_file)
    json_file.close()
else:
    #print('There is an issue with locating the dtconfig.json file!')
    sys.exit('There is an issue with locating the dtconfig.json file!')

switchusername = (dtconfig['setup']['Network']['SwitchUser'])
switchpassword = (dtconfig['setup']['Network']['SwitchPW'])
switchip = (dtconfig['setup']['Network']['SwitchServerVLANIP'])

print('The following switch with an IP of ' + switchip + ' has a username of ' +
      switchusername + ' with the password of ' + switchpassword + ' will be configured with a new VLAN called ' + FirstVLANname + '.')
