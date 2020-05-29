import yaml
import json

vlanfile = open("Additional_VLANs.yml")

parsed_vlanfile = yaml.load(vlanfile, Loader=yaml.FullLoader)

# need to find out how to close this file since we now have it within the parsed_vlanfile variable.


# for loop would probably be ideal here. this will work for now.

FirstVLANname = (parsed_vlanfile.get('V1name'))  # - this worked.
FirstVLANname = (parsed_vlanfile.get('V1name'))


json_file = open("dtconfig.init.json")

dtconfig = json.load(json_file)
json_file.close()

switchusername = (dtconfig['setup']['Network']['SwitchUser'])
switchpassword = (dtconfig['setup']['Network']['SwitchPW'])
switchip = (dtconfig['setup']['Network']['SwitchServerVLANIP'])

print('The following switch with an IP of ' + switchip + ' has a username of ' +
      switchusername + ' with the password of ' + switchpassword + '.')


# print(var)

# print("vlan name", (parsed_vlanfile.get('V1name'))) # - this worked

# print(var)
# print(parsed_vlanfile)
# print(parsed_creds)

# print(parsed_yaml_file.get("a_list"))
