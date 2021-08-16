import requests
import os
from bs4 import BeautifulSoup

url = "https://kr.indeed.com/jobs?q=python"
os.system("clear")

def extract_indeed_pages():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("ul", {"class": "pagination-list"})
  page_li = pages.find_all("li")
  page_span = []
  for li in page_li[1:-1]:
      tmp = li.find("span").string
      page_span.append(int(tmp))
  max_page = page_span[-1]
  return max_page

def extract_job(soup):
  title = soup.select_one('.jobTitle > span').string
  company = soup.select_one('.companyName').string
  location = soup.select_one('.companyLocation').string
  job_id = soup.parent['data-jk']
  return {
    'title':title, 
    'company': company, 
    'location': location,
    'link': f"https://kr.indeed.com/viewjob?jk={job_id}"
  }

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping INDEED page {page}")
    result = requests.get(f"{url}&start={page*10}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup("div", class_ = "slider_container" )
    for res in results:
      job = extract_job(res)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = extract_indeed_pages()
  jobs = extract_indeed_jobs(last_page)
  return jobs