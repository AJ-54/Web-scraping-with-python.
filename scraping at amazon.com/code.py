import requests
import json
from bs4 import BeautifulSoup
book=raw_input("Enter the book name :")
print "........................Top results at amazon.com......................"

response=requests.get("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords="+book)
#print response.status_code 
#print response.content

soup=BeautifulSoup(response.content , "html.parser")

soup1=soup.find('div' , class_="a-row s-result-list-parent-container")
ulsoup=list(soup1.children)[0]
ansoup=ulsoup.find_all('div' , class_="a-row a-spacing-small")
count=1
for name in ansoup:

	try:
		print count,")"," ",name.find('a' , class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")['title']
		count+=1
	except:
		continue




	
	



