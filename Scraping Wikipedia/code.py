import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
import requests
from bs4 import BeautifulSoup

response=requests.get("https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods")
print response.status_code


soup=BeautifulSoup(response.content , 'html.parser')
tsoup= soup.find_all('div' , class_='mw-body-content')[2].find_all('table')[1]
row_count=1
for tr in tsoup.find_all('tr'):
	row_count+=1
	col_count=0
	i=0
	for td in tr.find_all('td'):
		col_count+=1
		
		if col_count in [1,4,5,8,11]:
			i+=1
			ans=td.get_text()
			sheet1.write(row_count,i,ans)
		else:
			continue
wb.save('data1.xls')
			
			
			

			
		
		
