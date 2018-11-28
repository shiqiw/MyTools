"""
We generally use class method to create factory methods. 
Factory methods return class object ( similar to a constructor ) for different use cases.

We generally use static methods to create utility functions.

To use this as a package
python -m myIO.myPrinter
"""

import collections
import json

class MyPrinter:
	ENDC = '\033[0m'

	BOLD = '\033[1m' 
	UNDERLINE = '\033[4m'
	BLACK_BACKGROUND = '\033[7m'

	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'

	@staticmethod
	def print_bold(content):
		print(MyPrinter.BOLD + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_underline(content):
		print(MyPrinter.UNDERLINE + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_black_background(content):
		print(MyPrinter.BLACK_BACKGROUND + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_red(content):
		print(MyPrinter.RED + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_green(content):
		print(MyPrinter.GREEN + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_yellow(content):
		print(MyPrinter.YELLOW + str(content) + MyPrinter.ENDC, end="")

	@staticmethod
	def print_dynamic(content):
		"""
		This method breaks if the line wraps.
		Only works in Python 3.
		"""
		print(str(content), end="\r")

	@staticmethod
	def print_newline():
		print("\n", end="")

	@staticmethod
	def clear_console():
		# Put clear console here just for convenience
		# ctrl+K is the real clear history in mac
		clear = lambda: os.system("clear")
		clear()

	@staticmethod
	def print_multiple(content):
		if not isinstance(content, collections.Mapping):
			raise Exception("content type {} is not dictionary".format(type(content)))

		if content["type"] != "multiple":
			raise Exception("content type {} is not multiple choice".format(content["type"]))

		MyPrinter.print_bold(content["question"])
		MyPrinter.print_newline()

		index = 'A'
		for option in content["options"]:
			(k, v), = option.items()
			MyPrinter.print_bold(str(index) + ". ")
			print(k)
			index = chr(ord(index) + 1)

	@staticmethod
	def print_single(content):
		if not isinstance(content, collections.Mapping):
			raise Exception("content type {} is not dictionary".format(type(content)))

		if content["type"] != "single":
			raise Exception("content type {} is not single question".format(content["type"]))

		MyPrinter.print_bold(content["question"])
		MyPrinter.print_newline()

	@staticmethod
	def print_description(content):
		if not isinstance(content, collections.Mapping):
			raise Exception("content type {} is not dictionary".format(type(content)))

		if content["type"] != "description":
			raise Exception("content type {} is not description".format(content["type"]))

		MyPrinter.print_underline(content["description"])
		MyPrinter.print_newline()


if __name__ == "__main__":
	MyPrinter.print_black_background("Testing printer basics...")
	MyPrinter.print_newline()

	with open("sample.json") as config:
		configDict = json.load(config)
	MyPrinter.print_multiple(configDict["1"])
	MyPrinter.print_single(configDict["2"])
	MyPrinter.print_description(configDict["3"])

	MyPrinter.print_black_background("Test finished.")
	MyPrinter.print_newline()
