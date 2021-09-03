#!/usr/bin/python
from bs4 import BeautifulSoup
import os
import time

while True:
	open('./datastatus.txt','w').close()

	with open('./status.txt') as f:
	    content = f.read()
	    soup = BeautifulSoup(content, 'html.parser')
	    rango = soup.find_all("span",{"class":"htb_rank"})
	    rank = soup.find_all("span",{"class":"htb_ranking"})
	    points = soup.find_all("span",{"class":"htb_points"})
	    respect = soup.find_all("span",{"class":"htb_respect"})

	rang = rango[0].text
	ran = rank[0].text
	poi = points[0].text
	res = respect[0].text
	print (rang)
	print ("%{F#ff0000}%{F#ffffff}"+rang+"| %{F#ff0000} %{F#ffffff}"+ran+" | %{F#ff0000} %{F#ffffff}"+poi+" | %{F#ff0000} %{F#ffffff}"+res, file=open("./datastatus.txt","a"))
	time.sleep(60)
	os.system('bash ./htbstatus.sh')

