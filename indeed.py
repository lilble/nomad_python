import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.indeed.com/jobs?q=python&limit=50&vjk=bc2301f0ce427cfc"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

pages = soup.find("ul", {"class": "pagination-list"})
page_li = pages.find_all("li")

page_a = []

for li in page_li:
    tmp = li.find('a')
    print(tmp)
    print("-----------------------------------------------")
    page_a.append(tmp)

page_a = page_a[1:-1]

for a in page_a:
    span = a.find("span")
    print(span.string)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
