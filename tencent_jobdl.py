import requests
from bs4 import BeautifulSoup 
import time

def get_job_dl(each_url):
	headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36','Host':'hr.tencent.com'}
	result_lst = []
	ul_lst = []
	link = each_url.strip() 
	r = requests.get(link,headers=headers,timeout = 10)
	print("status:",r.status_code)
	soup  = BeautifulSoup(r.text,"lxml")
# position name
	ps_name = soup.find(id='sharetitle').text.strip()
	result_lst.append(ps_name)
# requirements
	ul_lst = soup.find_all('ul',class_='squareli')
	li_lst = []
	for each_ul in ul_lst:
		li_lst = each_ul.find_all('li')
		for each_li in li_lst:
			li = each_li.text.strip()
			result_lst.append(li)
#			print(li.encode('utf-8'))
	time.sleep(10)
	result_lst.append('***')
	return result_lst

file_url = open('jobs_url.txt','r')
url_lines = file_url.readlines()
with open('/Users/Juan/Documents/data_analysis/webscraping/qq/jobs_dtl.txt',"w+") as f:
	for each_url in url_lines:
		dtls = get_job_dl(each_url)
		for j in dtls:
			f.write(j.encode('utf-8')+"\n")
	f.close()
