import json
from pymongo import MongoClient

# Use local absolute path, can break easily
import sys
sys.path.append('/Users/SW/GitHub/MyTools/myIO')
from myPrinter import MyPrinter

class MyMongo:
	collections = {}

	def __init__(self, fileName):
		with open(fileName) as config:
			configDict = json.load(config)

		# connect to database
		self.client = MongoClient(configDict["client"])
		self.database = self.client[configDict["database"]]

		collectionDict = dict((collection, self.database[collection]) \
			for collection in configDict["collection"])
		self.collections = collectionDict

	def insert(self, collection, post):
		posts = self.collections[collection]
		postId = posts.insert_one(post).inserted_id
		if __debug__:
			MyPrinter.print_green(postId)
			MyPrinter.print_newline()
		return postId

	def findOne(self, collection, key, value):
		posts = self.collections[collection]
		post = posts.find_one({key: value})
		if __debug__:
			MyPrinter.print_green(post)
			MyPrinter.print_newline()
		return post

	def deleteOne(self, collection, _id):
		self.collections[collection].delete_one({"_id": _id})
		if __debug__:
			self.database.drop_collection(collection)

if __name__ == "__main__":
	"""
	Test case.
	"""
	print("Use sample config to set up test...")
	tests = MyMongo("config.json")

	print("\nVerify none-existance of collection...")
	MyPrinter.print_green(tests.database.collection_names(include_system_collections=False))
	MyPrinter.print_newline()

	print("\nInsert sample post into collection...")
	_id = tests.insert("test", {"name": "Mike"})

	print("\nVerify existance of collection...")
	MyPrinter.print_green(tests.database.collection_names(include_system_collections=False))
	MyPrinter.print_newline()

	print("\nLooking for sample post in collection...")
	tests.findOne("test", "name", "Mike")

	print("\nDeleting sample post from collection...")
	tests.deleteOne("test", _id)

	print("\nVerify none-existance of collection...")
	MyPrinter.print_green(tests.database.collection_names(include_system_collections=False))
	MyPrinter.print_newline()

	print("\nTest finished.")
