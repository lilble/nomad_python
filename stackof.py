import os
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"
os.system("clear")

def get_last_page():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find_all("a",{"class":"s-pagination--item"})
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("h2").find("a")["title"]
  company_row = html.find("h3").find("span")
  print(title)

def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    return jobs

def get_jobs():
  last_page = get_last_page()
  extract_jobs(last_page)
  return []