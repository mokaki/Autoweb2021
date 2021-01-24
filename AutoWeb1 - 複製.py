#-*- coding:utf-8 -*-
'''
自動開ac
202101230510
'''




import os
import json
import time













#############################################_Star
def _Star():
	print ('\n開始AutoWeb _Star 202101232044')
	a0json = '0.json'
	if os.path.isfile(a0json):					#如0檔在
		with open(a0json, 'r', encoding="utf-8") as ha0ha:
			data = json.load(ha0ha)
			Jonsinput0 = data['Date'][0]['Whatsapp號']
			Jonsinput1 = data['Date'][0]['姓']
			Jonsinput2 = data['Date'][0]['名']
			Jonsinput3 = data['Date'][0]['出生年']
			Jonsinput4 = data['Date'][0]['GAC']
			Jonsinput5 = data['Date'][0]['GPS']
			Jonsinput6 = data['Date'][0]['FBAC']
			Jonsinput7 = data['Date'][0]['FBPS']
			Jonsinput8 = data['Date'][0]['MWAC']
			Jonsinput9 = data['Date'][0]['MEWEPS']
			Jonsinput10 = data['Date'][0]['WIKIAC']
			Jonsinput11 = data['Date'][0]['WIKIPS']
			Jonsinput12 = data['Date'][0]['taobaoAC']
			Jonsinput13 = data['Date'][0]['taobaoPS']
			print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			print ("\nWhatsapp號 ",Jonsinput0)
			print ("\n姓",Jonsinput1)
			print ("\n名",Jonsinput2)
			print ("\n出生年 ",Jonsinput3)
			print ("\nGAC",Jonsinput4)
			print ("\nGPS",Jonsinput5)
			print ("\nFBAC",Jonsinput6)
			print ("\nFBPS",Jonsinput7)
			print ("\nMWAC",Jonsinput8)
			print ("\nMEWEPS",Jonsinput9)
			print ("\nWIKIAC",Jonsinput10)
			print ("\nWIKIPS",Jonsinput11)
			print ("\ntaobaoAC",Jonsinput12)
			print ("\ntaobaoPS",Jonsinput13)
			print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			os.system("pause")
	else:									#0檔不在入名
		print ('\n您可以將文件命名為 0.json 即可自動執行')
		Jonsinput00 = input('請輸入存檔名')
		dateurl0 = input('存檔位置,如..\\date\\*可沒有')
		DataURL = str(dateurl0)+str(Jonsinput00)+'.json'
		_SeeMyDate = (str(DataURL))

		if not os.path.isfile(_SeeMyDate):	#入名檔都不在
			print ("帳號文件不存在\n轉去創新文件")
			_MakeDate()
		else:
			with open(_SeeMyDate, 'r', encoding="utf-8") as ha1ha:
				data = json.load(ha1ha)
				Jonsinput0 = data['Date'][0]['存檔名']
				Jonsinput1 = data['Date'][0]['存檔內容1']
				Jonsinput2 = data['Date'][0]['存檔內容2']
				print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print ("\n存檔名 ",Jonsinput0)
				print ("\n存檔內容1 ",Jonsinput1)
				print ("\n存檔內容2 ",Jonsinput2)
				print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				os.system("pause")


#############################################_SeeDateEND



















#開Gmail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def _MakeGoogleAC():
	global GmailPS
	global PSSel
	print ('\n_MakeGoogleAC 自動開ac 202101230510')

	PSSel = 1
	#密码的长度为15
	GmailPS = _GenPassword(15)
	print ('*****************生成随机密码*****************\n',GmailPS,'\n*****************\n')


	#selenium基本
	options = webdriver.ChromeOptions()		#禁彈窗
	prefs = {'profile.default_content_setting_values':{'notifications' : 2}}  
	options.add_experimental_option('prefs',prefs)
	#options.add_argument('--headless')		#冇頭
	#options.add_argument('--no-sandbox')	#冇頭
	options.add_argument("--log-level=3")	
	browser = webdriver.Chrome('../.exe/chromedriver' ,chrome_options=options)
	browser.set_window_size(480, 600)


	
	browser.get('https://accounts.google.com/signup')
	#等有email位
	element = WebDriverWait(browser, 10, 0.5).until(		
		EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')),'\n!!!找不到這個網頁原素!!!\nGmail位\n' + '//*[@id="username"]\n'
	)
	#姓
	browser.find_element_by_xpath('//*[@id="lastName"]').send_keys("name_entry")
	#名	
	browser.find_element_by_xpath('//*[@id="firstName"]').send_keys("圬荏")		
	#Gmail	
	browser.find_element_by_xpath('//*[@id="username"]').send_keys("gofidfqfe")		
	#PS
	browser.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(GmailPS)			
	#PS2
	browser.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(GmailPS)	

	browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div/div/input').click()



	print ('\n未禁鍵')
	os.system("pause")

















#生成随机密码
import random
import string
PSSel = 0
GmailPS = 0
def _GenPassword(length):
	if PSSel == 0:	#随机英數文字
		chars=string.ascii_letters+string.digits
		return ''.join([random.choice(chars) for i in range(length)])
	if PSSel == 1:	#随机英文字
		chars=string.ascii_letters
		return ''.join([random.choice(chars) for i in range(length)])
#生成随机密码END







_MakeGoogleAC()







