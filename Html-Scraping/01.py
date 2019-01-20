from lxml import html
import requests

#get to retrieve the web page with our data

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#We need to use page.content rather than page.text because html.fromstring implicitly expects bytes as input.

'''tree now contains the whole HTML file in a nice tree structure which we can go over two different ways: XPath and CSSSelect. 
In this example, we will focus on the former.
XPath is a way of locating information in structured documents such as HTML or XML documents.'''

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print "buyers:",buyers
print "prices:",prices

