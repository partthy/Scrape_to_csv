import requests
from bs4 import BeautifulSoup
import csv
response = requests.get('https://www.aljazeera.com/')
if response.status_code ==  200:
     html_content = response.text
else:
    print(f'Request failed with staus code {response.status_code}')

soup = BeautifulSoup(html_content,'html.parser')

# Extracting headlines
headlines = soup.find_all('h3', class_="article-card__title")
headlines_count = len(headlines)
headline_text = [headline.text.strip() for headline in headlines]  # Stripping any extra whitespace

# Writing headlines to CSV in a single column
with open('headline.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])  # Adding a header row for clarity
    for headline in headline_text:
        writer.writerow([headline])  # Each headline in its own row

print(f"{headlines_count} headlines have been saved to 'headline.csv' ")