from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(html_text, 'lxml')
cases = soup.find_all('div', class_ = 'maincounter-number')[0].text
dead = soup.find_all('div', class_ = 'maincounter-number')[1].text
recov = soup.find_all('div', class_ = 'maincounter-number')[2].text

print(f'''
Cases: {cases.strip()}
Dead:  {dead.strip()}
Recovered: {recov.strip()}
''')

input()
