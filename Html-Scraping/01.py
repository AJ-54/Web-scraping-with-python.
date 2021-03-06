from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

'''tree now contains the whole HTML file in a nice tree structure which we can go over two different ways: XPath and CSSSelect. 
In this example, we will focus on the former.
XPath is a way of locating information in structured documents such as HTML or XML documents.'''


buyers = tree.xpath('//div[@title="buyer-name"]/text()')

prices = tree.xpath('//span[@class="item-price"]/text()')

print "buyers:",buyers
print "prices:",prices

