from bs4 import BeautifulSoup
import requests

url = "https://www.calendarr.com/united-states/how-many-days/christmas-day/"

response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')

xmas = soup.find('div', class_ = 'day-counter--detail-text').text.replace('Now that you know how many days are left until   Christmas Day, share it with your friends.', ' ').replace('   ',' ').replace('Day!', '')
print(xmas)
input()
