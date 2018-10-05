#this app can block web service for a certain time

#time module is used to find the working hour
import time
from datetime import datetime as dt

##we use the tmp host file for
## for the testing purpose

#temp_host="tmp_hosts"
temp_host="/etc/hosts"
host_real_path_windows="C:\windows\System32\drivers\etc\hosts"

##we will redirect all the url in the localhost
redirect = "127.0.0.1"


def get_url():
	url_list=[]
	data=open('sites','r+')
	data=data.readlines()
	
	for item in data:
		item=item.replace("\n","") ## removing the \n character from the line
		url_list.append(item)
	return url_list

#url_list=get_url()

def append_url():
	websites=get_url()
	data1=open(temp_host,"r+")
	content = data1.read()
	
	for website in websites:
		if website in content:
			pass
		else:
			##append the line to redirect
			data1.write(redirect+" "+ website+"\n")

# we get the url now redirecting it by writing 
# in the host file


def total_replace():
	websites=get_url()
####################### total replace method #######
# suppose the working hour is over 
# so now there is some entry at the end of the file
# so this are the extra item that is added 
# so we first read the whole file and then wirte the 
#the same thing in this file again but until the extra item
# the extra website that is on the list come on the file 
# we stop writing ..thats how create the original file
 
	file1=open(temp_host,"r+")
	content=file1.readlines()
	file2=open(temp_host,"w")
	file1.seek(0)
	for line in content:
		if not any(website in line for website in websites):
			file2.write(line)


while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt(dt.now().year,dt.now().month,dt.now().day,16):
		print "working hours"
		append_url()
	else:
		print "fun hours"
		total_replace()
	time.sleep(5)

