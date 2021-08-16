import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode = "w")
  writing = csv.writer(file)
  writing.writerow(["title", "company", "location", "link"])
  for job in jobs:
    
  return