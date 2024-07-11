#!/usr/bin/env python
import yaml

class SpecParse:
	def __init__(self, name, num_args, args, output):
		self.name = name
		self.num_args = num_args
		self.args = args
		self.output = output
		self.address = None

	def __repr__(self):
		return (f"SpecParse(name={self.name}, num_args={self.num_args}, "
				f"args={self.args}, output={self.output},  address={self.address})")
	
	def setAddr(self, addr):
		self.address = addr

class Argument:
	def __init__(self, name, datatype, size, constraints):
		self.name = name
		self.datatype = datatype
		self.size = size
		self.constraints = constraints

	def __repr__(self):
		return (f"Argument(name={self.name}, type={self.datatype}, size={self.size}, "
				f"constraints={self.constraints})")

class Output:
	def __init__(self, type, size):
		self.type = type
		self.size = size

	def __repr__(self):
		return f"Output(type={self.type}, size={self.size})"

# Function to read YAML file
def read_yaml(file_path):
	with open(file_path, 'r') as file:
		try:
			return yaml.safe_load(file)
		except yaml.YAMLError as exc:
			print(f"Error parsing YAML file: {exc}")
			return None

# Function to create SpecParse objects from parsed YAML
def create_service_spec(yaml_data):
	functions = []
	for function_data in yaml_data['functions']:
		function_info = function_data['function']
		name = function_info['name']
		num_args = function_info['num_args']

		args = []
		for i in range(1, num_args + 1):
			arg_info = function_info[f'arg_{i}']
			args.append(Argument(arg_info['name'], arg_info['type'], arg_info['size'], arg_info['constraints']))

		output_info = function_info['output']
		output = Output(output_info['type'], output_info['size'])

		functions.append(SpecParse(name, num_args, args, output))

	return functions


