import os
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

os.system("clear")

def get_last_page():
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup("a", class_ = "s-pagination--item")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("h2").find("a")["title"]
  subtitle = html.find("h3").find_all("span")
  company = subtitle[0].get_text(strip=True)
  location = subtitle[1].get_text(strip=True)
  job_id = html['data-jobid']
  return {
    'title':title, 
    'company': company, 
    'location': location,
    'link': f"https://stackoverflow.com/jobs/{job_id}"
  }

def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(f"Scrapping STACKOF page {page}")
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", class_ = "-job")
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  last_page = 0
  jobs = extract_jobs(last_page)
  return jobs