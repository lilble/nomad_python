import os
from indeed import get_jobs as get_indeed_jobs
from stackof import get_jobs as get_stackof_jobs
from save import save_to_file

os.system("clear")

indeed_jobs = get_indeed_jobs()
stackof_jobs = get_stackof_jobs()
jobs =  indeed_jobs + stackof_jobs

save_to_file(jobs)

# for i in jobs:
#   print(i['title'])

