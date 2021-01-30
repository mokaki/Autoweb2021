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
	global a0json
	print ('\n\n歡迎您使用 AutoWeb')
	a0json = '0.json'
	if os.path.isfile(a0json):					#如0檔在
		_SeeDate()
	else:									#0檔不在入名
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
		_MakeDate()
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
		print ('\n\n您可以將文件命名為 0.json 即可自動執行')
		Jonsinput00 = input('\n\n\n\n\n\n\n\n\n\n\n\n\n請輸入存檔名')
		_SeeMyDate = (str(Jonsinput00+'.json'))
		if os.path.isfile(_SeeMyDate):		#如檔在
			a0json = _SeeMyDate
			_SeeDate()
		else:									#檔不入存檔位
			dateurl0 = input('存檔位置,如..date\\')
			DataURL = str(dateurl0)+str(Jonsinput00)+'.json'
			_SeeMyDate = (str(DataURL))
			if not os.path.isfile(_SeeMyDate):	#入名檔都不在
				print ("\n\n\n\n\n\n\n帳號文件不存在\n開新存檔\n\n")
				_MakeDate()
			else:
				a0json = _SeeMyDate
				_SeeDate()



		
#############################################_StarEND







#############################################_SeeDate
a0json = '0.json'
def _SeeDate():
	with open(a0json, 'r', encoding="utf-8") as ha0ha:
		data = json.load(ha0ha)
		Jonsinput00 = data['Date'][0]['存檔時間']
		Jonsinput0 = data['Date'][0]['Whatsapp號']
		Jonsinput1 = data['Date'][0]['姓']
		Jonsinput2 = data['Date'][0]['名']
		Jonsinput3 = data['Date'][0]['出生年']
		Jonsinput4 = data['Date'][0]['月']
		Jonsinput5 = data['Date'][0]['日']
		Jonsinput6 = data['Date'][0]['GAC']
		Jonsinput7 = data['Date'][0]['GPS']
		print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',a0json,'        ',Jonsinput00,'\n')
		print ("\nWhatsapp號 ",Jonsinput0)
		print ("\n姓",Jonsinput1)
		print ("\n名",Jonsinput2)
		print ("\n出生年 ",Jonsinput3)
		print ("\n月",Jonsinput4)
		print ("\n日",Jonsinput5)
		print ("\nGAC",Jonsinput6)
		print ("\nGPS",Jonsinput7)
		print ("\n+++",a0json,"+++\n")

		os.system("pause"),_Star()

#############################################_SeeDateEND




#############################################_printDate
Jonsinput0 = 0
Jonsinput1 = 0
Jonsinput2 = 0
Jonsinput3 = 0
Jonsinput4 = 0
Jonsinput5 = 0
Jonsinput6 = 0
Jonsinput7 = 0
def _printDate():
	print ('\n查文件 _printDate _printDate')
	print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print ("\nWhatsapp號 ",Jonsinput0)
	print ("\n姓",Jonsinput1)
	print ("\n名",Jonsinput2)
	print ("\n出生年 ",Jonsinput3)
	print ("\n月",Jonsinput4)
	print ("\n日",Jonsinput5)
	print ("\nGAC",Jonsinput6)
	print ("\nGPS",Jonsinput7)
	print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#############################################_printDateEND




#############################################_SaveDate
def _SaveDate():
	global a0json
	print ('開始存檔')
	JonsinputAll = {
		'Date': [
			{
			#############################################
				'存檔時間': time.strftime('%Y%m%d|%H%M%S'),
				'Whatsapp號': Jonsinput0,
				'姓': Jonsinput1,
				'名': Jonsinput2,
				'出生年': Jonsinput3,
				'月': Jonsinput4,
				'日': Jonsinput5,
				'GAC': Jonsinput6,
				'GPS': Jonsinput7
			#############################################
			}
		]
	}
	path = Jonsinput0+"_"+time.strftime('%Y%m%d%H%M%S')+'.json'
	json_str = json.dumps(JonsinputAll, ensure_ascii=False, indent=4) # 缩进4字符
	with open(path, 'w', encoding="utf-8") as json_file:
		json_file.write(json_str)
	print ('已保存\n'+str(JonsinputAll))
	a0json = path
	_SeeDate()
#############################################_SaveDateEND




#############################################_MakeDate
def _MakeDate():
	global Jonsinput0
	global Jonsinput1
	global Jonsinput2
	global Jonsinput3
	global Jonsinput4
	global Jonsinput5
	global Jonsinput6
	global Jonsinput7
	#print ('\n創新文件 _MakeDate 202101241519')

###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
	Jonsinput0 = input('\n\n\n*******自動整網系統 歡迎您*******\n請輸入Whatsapp號...')
	Jonsinput1 = _GenRandomTxt(3)	#3字英文姓
	Jonsinput2 = _GenRandomTxt(6)	#6字英文名
	Jonsinput3 = str('19'+str(random.randint(79,99)))	#隨機年2個數字
	Jonsinput4 = str(random.randint(1,12))	#隨機月2個數字
	Jonsinput5 = str(random.randint(1,28))	#隨機日2個數字
	Jonsinput6 = str(Jonsinput1+Jonsinput2+Jonsinput3+Jonsinput4+Jonsinput5)	#1+2=英文姓
	Jonsinput7 = _GenPassword(15)	#15字密碼
	_printDate(),_MakeGoogleAC()
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********
###***********###***********###***********###***********

	Jonsinput0 = input('''\n\n\n
		*******自動整網系統 歡迎您*******\n
		請依次輸入\n
		Whatsapp號>姓>名>出生年>Gmail名>Gmail密碼>\n
		謝謝\n
		*******************************\n\n\n\n\n\n\n\n\n
請輸入Whatsapp號...''')
	Jonsinput1a = input('\n\n\n姓...\n*不填寫會用隨機3個英文字\n\n單獨輸入一個字符,將全使用隨樹')
	if (len(Jonsinput1a) == 1 ):	#單獨輸入一個字符,將全使用隨樹
		Jonsinput1 = _GenRandomTxt(3)	#3字英文姓
		Jonsinput2 = _GenRandomTxt(6)	#6字英文名
		Jonsinput3 = str('19'+str(random.randint(79,99)))	#隨機年2個數字
		Jonsinput4 = str(random.randint(1,12))	#隨機月2個數字
		Jonsinput5 = str(random.randint(1,28))	#隨機日2個數字
		Jonsinput6 = str(Jonsinput1+Jonsinput2+Jonsinput3+Jonsinput4+Jonsinput5)	#1+2=英文姓
		Jonsinput7 = _GenPassword(15)	#15字密碼
		_printDate(),_MakeGoogleAC()
	else:
		if (len(Jonsinput1a) == 0 ):
			Jonsinput1 = _GenRandomTxt(3)	#3字英文姓
		else:
			Jonsinput1 = Jonsinput1a	#客入的姓
		Jonsinput2a = input('\n\n\n名...\n*不填寫會用隨機6個英文字')
		if (len(Jonsinput2a) == 0 ):
			Jonsinput2 = _GenRandomTxt(6)	#6字英文名
		else:
			Jonsinput2 = Jonsinput2a	#客入的名
		Jonsinput3a = input('\n\n\n出生年後2位...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput3a) == 0 ):
			Jonsinput3 = str('19'+str(random.randint(79,99)))	#隨機2個數字
		else:
			Jonsinput3 = str('19'+Jonsinput3a)	#客入的2個數字
		Jonsinput4a = input('\n\n\n月...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput4a) == 0 ):
			Jonsinput4 = str(random.randint(1,12))	#隨機2個數字
		else:
			Jonsinput4 = Jonsinput4a	#客入的2個數字
		Jonsinput5a = input('\n\n\n日...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput5a) == 0 ):
			Jonsinput5 = str(random.randint(1,28))	#隨機2個數字
		else:
			Jonsinput5 = Jonsinput5a	#客入的2個數字
		Jonsinput6a = input('\n\n\nGAC...\n*不填寫會用隨機生成的英文姓名組成')
		if (len(Jonsinput6a) == 0 ):
			Jonsinput6 = str(Jonsinput1+Jonsinput2+Jonsinput3+Jonsinput4+Jonsinput5)	#隨機2個數字
		else:
			Jonsinput6 = Jonsinput6a	#客入的2個數字
		Jonsinput7a = input('\n\n\nGPS...\n*不填寫會用隨機15個英文數字符號')
		if (len(Jonsinput7a) == 0 ):
			Jonsinput7 = _GenPassword(15)	#15字密碼
		else:
			Jonsinput7 = Jonsinput7a	#客入的2個數字
		_printDate(),_MakeGoogleAC()
#############################################_MakeDateEND

























#開Gmail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def _MakeGoogleAC():
	print ('\n_MakeGoogleAC 自動開Googleac 202101252326\n\n')
	#selenium基本
	options = webdriver.ChromeOptions()		#禁彈窗
	prefs = {'profile.default_content_setting_values':{'notifications' : 2}}  
	options.add_experimental_option('prefs',prefs)
	#options.add_argument('--headless')		#冇頭
	#options.add_argument('--no-sandbox')	#冇頭
	options.add_argument("--log-level=3")	
	browser = webdriver.Chrome('../.exe/chromedriver' ,chrome_options=options)
	browser.set_window_size(480, 600)


	#到申請AC頁
	browser.get('https://accounts.google.com/signup')
	#等有email位
	element = WebDriverWait(browser, 10, 0.5).until(		
		EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')),'\n!!!找不到這個網頁原素!!!\nGmail位\n' + '//*[@id="username"]\n'
	)
	#姓
	browser.find_element_by_xpath('//*[@id="lastName"]').send_keys(Jonsinput1)
	#名	
	browser.find_element_by_xpath('//*[@id="firstName"]').send_keys(Jonsinput2)		
	print ('\n等待3至11秒'),time.sleep(random.uniform(3, 11))
	#Gmail	
	browser.find_element_by_xpath('//*[@id="username"]').send_keys(Jonsinput6)		
	#PS
	browser.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(Jonsinput7)			
	#PS2
	browser.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(Jonsinput7)	
	#顯示密碼
	browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[3]/div/div[1]/div/div/div[1]/div/div/input').click()
	print ('\n等待3至11秒'),time.sleep(random.uniform(3, 11))
	#繼續
	browser.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/div[2]').click()
	

	#到驗證電話頁
	#等有電話號碼位
	element = WebDriverWait(browser, 10, 0.5).until(		
		EC.presence_of_element_located((By.XPATH,'//*[@id="phoneNumberId"]')),'\n!!!找不到這個網頁原素!!!\n電話號碼位\n' + '//*[@id="phoneNumberId"]\n'
	)
	#電話號碼
	browser.find_element_by_xpath('//*[@id="phoneNumberId"]').send_keys(Jonsinput0)
	print ('\n等待3至11秒'),time.sleep(random.uniform(3, 11))
	#繼續
	browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()

	#if 此電話號碼的格式無法
	a = browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div[2]/div').text
	print ('\n此電話號碼的格式無法\n',a)
	os.system("pause")




################################################
################################################
################################################
################################################
################################################
################################################
################################################

	











	#到驗證電話sms頁
	#等有驗證碼位
	element = WebDriverWait(browser, 10, 0.5).until(		
		EC.presence_of_element_located((By.XPATH,'//*[@id="code"]')),'\n!!!找不到這個網頁原素!!!\n驗證碼位\n' + '//*[@id="code"]\n'
	)
	print ('\n請查看簡訊驗證你的電話號碼')
	os.system("pause")
	a = input('驗證碼')
	#驗證碼
	browser.find_element_by_xpath('//*[@id="code"]').send_keys(a)
	#驗證
	browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]').click()



	#到詳細資料頁
	#等有年位
	element = WebDriverWait(browser, 10, 0.5).until(		
		EC.presence_of_element_located((By.XPATH,'//*[@id="year"]')),'\n!!!找不到這個網頁原素!!!\n年位\n' + '//*[@id="year"]\n'
	)
	#年
	browser.find_element_by_xpath('//*[@id="year"]').send_keys(Jonsinput3)
	#日
	browser.find_element_by_xpath('//*[@id="day"]').send_keys(Jonsinput5)
	#月
	m = str('//*[@id="month"]/option['+Jonsinput4+']')
	browser.find_element_by_xpath(m).click()
	#性
	s = str(random.randint(1,4))
	st = str('//*[@id="gender"]/option['+s+']')
	browser.find_element_by_xpath(st).click()


	print ('\n未K')
################################################
################################################
################################################
################################################
################################################
################################################
################################################


	_SaveDate()
	#os.system("pause")

























#生成随机密码
import random
import string
def _GenRandomTxt(length):
	#随机英文字
	chars=string.ascii_letters
	return ''.join([random.choice(chars) for i in range(length)])

def _GenPassword(length):
	#随机英數文字标点
	chars=string.ascii_letters+string.digits+string.punctuation
	return ''.join([random.choice(chars) for i in range(length)])
#生成随机密码END







_Star()







