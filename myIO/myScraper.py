# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import datetime
from langconv import *
import sys
from urllib2 import urlopen

class MyScraper:

	@staticmethod
	def scrape_content(url, name, contentMajor, majorCondition, contentMinor, convert = False, link = None, linkCondition = None):
		if url == None:
			return

		if not url.startswith("http://"):
			url = "http://" + url

		soup = BeautifulSoup(urlopen(url).read())

		if name == None:
			name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		with open(name + ".txt", "w") as outputFile:
			# assume content is in one div, identifiable by id
			div = soup.find(contentMajor, majorCondition)
			for tag in div.findChildren(contentMinor, recursive=True):
				next = tag.nextSibling
				while (next and isinstance(next, NavigableString)):
					if len(next.strip()) == 0:
						text = tag.getText().encode('utf-8')
					else:
						text = next.strip().encode('utf-8')
					
					# if convert:
					# 	text = Converter('zh-hans').convert(text)

					outputFile.write(text)
					outputFile.write('\n\n')
					next = next.nextSibling

		if link != None and linkCondition != None:
			nextDiv = soup.find(link, linkCondition)
			nextUl = nextDiv.find("ul")
			nextLi = nextUl.find("li", {"class": "next-post"})
			if nextLi == None:
				return None
			nextSpan = nextLi.find("span", {"class": "link"})
			nextAnchor = nextSpan.find("a", href=True)
			nextLink = nextAnchor['href']
			return nextLink
		# 	MyScraper.scrape_content(nextLink, "", "div", {"id": "content"}, \
		# "p", True, "div", {"class": "next-prev-post-arrow"})

if __name__ == "__main__":
	# FC2 test entry
	# MyScraper.scrape_content("http://skdusk.blog126.fc2blog.us/blog-entry-2681.html", "崇北关 by 生为红蓝", \
	# 	"div", {"id": "more"}, "br")

	# Seba blog test entry
	link = "http://seba.tw/the-fates-start/"
	index = 1
	while link != None:
		link = MyScraper.scrape_content(link, "司命书 " + str(index), "div", {"id": "content"}, \
		"p", True, "div", {"class": "next-prev-post-arrow"})
		index += 1