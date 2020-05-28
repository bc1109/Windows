import yaml


a_yaml_file = open("example.yaml")


parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

print(parsed_yaml_file["a_dictionary"])
print(parsed_yaml_file.get("a_list"))
