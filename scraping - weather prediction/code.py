import requests
from bs4 import BeautifulSoup

response=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XAkSNGgzZPY")
print response.status_code
 
soup=BeautifulSoup(response.content, 'html.parser' )

seven_day=soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

print forecast_items

'period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp-high").get_text()

print(period)
print(short_desc)
print(temp)

img = tonight.find("img")
print img.prettify()
desc = img['title']
print(desc)
