import yaml
import os
import sys


if os.path.isfile('Additional_VLANs.yml'):
    vlanfile = open("Additional_VLANs.yml")
    parsed_vlanfile = yaml.load(vlanfile, Loader=yaml.FullLoader)

else:
    print('There is an issue with locating the Additional_VLANs.yml file!')
