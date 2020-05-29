import yaml
import json
import os
import sys


if os.path.isfile('Additional_VLANs.yml'):
    vlanfile = open("Additional_VLANs.yml")
    parsed_vlanfile = yaml.load(vlanfile, Loader=yaml.FullLoader)
    vlanfile.close()
