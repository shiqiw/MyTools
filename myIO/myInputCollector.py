"""
Use dir(module_name) to print all module, variable and function available.

The __init__.py files are required 
to make Python treat the directories as containing packages.

If the Python interpreter is running that module (the source file) as the main program, 
it sets the special __name__ variable to have a value "__main__". 
If this file is being imported from another module, 
__name__ will be set to the module's name.
"""

import json
from myPrinter import MyPrinter

class MyInputCollector:
	@staticmethod
	def multiple_choice(item):
		MyPrinter.print_multiple(item)
		choice = ord(input().upper()[:1]) - ord('A')

		if choice < 0 or choice >= len(item["options"]):
			return None
		else:
			(k, v), = item["options"][choice].items()
			return v

	@staticmethod
	def single_question(item):
		MyPrinter.print_single(item)

		lines = []
		while True:
			line = input()
			if line == ":q!":
				lines = []
				break
			elif line == ":wq":
				break
			else:
				lines.append(line)
		return '\n'.join(lines)


if __name__ == "__main__":
	with open("sample.json") as config:
		configDict = json.load(config)

	index = "1"
	while True:
		if not index in configDict:
			MyPrinter.print_black_background("Test finished")
			MyPrinter.print_newline()
			break;

		item = configDict[index]
		if item["type"] == "multiple":
			index = MyInputCollector.multiple_choice(item)
		elif item["type"] == "single":
			content = MyInputCollector.single_question(item)
			print(content)
			index = item["previous"]
		else:
			MyPrinter.print_description(item)
			index = "Finished"