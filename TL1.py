import yaml
import json
import os
import sys

# Begin TACLAN YAML
if os.path.isfile('Additional_VLANs.yml'):
    vlanfile = open("Additional_VLANs.yml")
    parsed_vlanfile = yaml.load(vlanfile, Loader=yaml.FullLoader)
    vlanfile.close()
else:
    sys.exit('There is an issue with locating the Additional_VLANS.yml file!')

# Begin define YAML Values
# for loop would probably be ideal here. this will work for now.


FirstVLANname = (parsed_vlanfile.get('V1name'))  # - this worked.


# for value in parsed_vlanfile
# if parsed_vlanfile.get('') == ('')
# then don't do shit
# else


# Begin DTECH JSON
if os.path.isfile('C:\\TACLAN\\Config\\JSONs\\dtconfig.init.json'):
    #print('Parsing the dtconfig json file')
    json_file = open("dtconfig.init.json")
    dtconfig = json.load(json_file)
    json_file.close()
else:
    sys.exit('There is an issue with locating the dtconfig.json file!')

# Begin define JSON Values
switchusername = (dtconfig['setup']['Network']['SwitchUser'])
switchpassword = (dtconfig['setup']['Network']['SwitchPW'])
switchip = (dtconfig['setup']['Network']['SwitchServerVLANIP'])

# Print to confirm values are present in the python script. Remove later
print('The following switch with an IP of ' + switchip + ' has a username of ' +
      switchusername + ' with the password of ' + switchpassword + ' will be configured with a new VLAN called ' + FirstVLANname + '.')
