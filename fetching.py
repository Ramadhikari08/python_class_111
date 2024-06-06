import requests
from bs4 import BeautifulSoup 
import sqlite3 

conn = sqlite3.connect('broadway.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS syllabus
          (id INTEGER PRIMARY KEY,
           title TEXT,
           content TEXT
          )""")

url = "https://broadwayinfosys.com/php/php-training-in-nepal"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser") 
print(soup)
syllabus_section = soup.find('ul', class_="course-accordion")
print(syllabus_section)

syllabus_items = syllabus_section.find_all("li")

print("Syllabus:")
for item in syllabus_items: 
    title = "Broadway-Analysis-Training in Nepal"
    content = item.get_text(strip=True)
    print("-", content)
    c.execute('''INSERT INTO syllabus (title, content) VALUES (?, ?)''', (title, content))

conn.commit()
conn.close()