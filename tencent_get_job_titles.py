import requests
from bs4 import BeautifulSoup
import time 

def get_jobs():
	headers = {'Host': 'hr.tencent.com',
	 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
	job_list = []
	for i in range(0,33):
#		link = 'https://hr.tencent.com/position.php?keywords=%E6%95%B0%E6%8D%AE&lid=2218&tid=87&start=' + str(i*10)
		link = 'https://hr.tencent.com/position.php?keywords=%E6%95%B0%E6%8D%AE&lid=2218&tid=82&start=' + str(i*10)
		r = requests.get(link,headers=headers,timeout = 10)
		print(str(i+1),"status:",r.status_code)
		soup  = BeautifulSoup(r.text,"lxml")
		ps_list = soup.find_all('td', class_='l square')
		for each in ps_list:
			job = each.a.text.strip()
			job_list.append(job)
		time.sleep(5)
	return job_list

jobs = get_jobs()
with open('/Users/Juan/Documents/data_analysis/webscraping/qq/jobs_titles_prod.txt',"w+") as f:
	for j in jobs:
		f.write(j.encode('utf-8')+"\n")
	f.close()
#print(jobs)

