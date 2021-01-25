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
	print ('\n開始AutoWeb _Star')
	a0json = '0.json'
	if os.path.isfile(a0json):					#如0檔在
		_SeeDate()
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
			a0json = _SeeMyDate
			_SeeDate()
#############################################_StarEND





#############################################_SeeDate
a0json = '0.json'
def _SeeDate():
	print ('\n查文件 _SeeDate 202101202244\n',a0json)
	with open(a0json, 'r', encoding="utf-8") as ha0ha:
		data = json.load(ha0ha)
		Jonsinput0 = data['Date'][0]['Whatsapp號']
		Jonsinput1 = data['Date'][0]['姓']
		Jonsinput2 = data['Date'][0]['名']
		Jonsinput3 = data['Date'][0]['出生年']
		Jonsinput4 = data['Date'][0]['月']
		Jonsinput5 = data['Date'][0]['日']
		Jonsinput6 = data['Date'][0]['GAC']
		Jonsinput7 = data['Date'][0]['GPS']
		print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print ("\nWhatsapp號 ",Jonsinput0)
		print ("\n姓",Jonsinput1)
		print ("\n名",Jonsinput2)
		print ("\n出生年 ",Jonsinput3)
		print ("\n月",Jonsinput4)
		print ("\n日",Jonsinput5)
		print ("\nGAC",Jonsinput6)
		print ("\nGPS",Jonsinput7)
		print ("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$_SeeDate$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		os.system("pause")
#############################################_SeeDateEND








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

	Jonsinput0 = input('''
		*******自動整網系統 歡迎您*******\n
		請依次輸入\n
		Whatsapp號>姓>名>出生年>Gmail名>Gmail密碼>\n
		謝謝\n
		*******************************\n\n
請輸入Whatsapp號...\n''')

	Jonsinput1a = input('姓...\n*不填寫會用隨機3個英文字\n\n單獨輸入一個字符,將全使用隨樹')

	if (len(Jonsinput1a) == 1 ):	#單獨輸入一個字符,將全使用隨樹
	
		Jonsinput1 = _GenRandomTxt(3)	#3字英文姓
		Jonsinput2 = _GenRandomTxt(6)	#6字英文名
		Jonsinput3 = str('19'+str(random.randint(79,99)))	#隨機年2個數字
		Jonsinput4 = str(random.randint(1,12))	#隨機月2個數字
		Jonsinput5 = str(random.randint(1,28))	#隨機日2個數字
		Jonsinput6 = str(Jonsinput1+Jonsinput2)	#1+2=英文姓
		Jonsinput7 = _GenPassword(15)	#15字密碼
		_printDate(),_SaveDate()
	else:
		if (len(Jonsinput1a) == 0 ):
			Jonsinput1 = _GenRandomTxt(3)	#3字英文姓
		else:
			Jonsinput1 = Jonsinput1a	#客入的姓
		Jonsinput2a = input('名...\n*不填寫會用隨機6個英文字')
		if (len(Jonsinput2a) == 0 ):
			Jonsinput2 = _GenRandomTxt(6)	#6字英文名
		else:
			Jonsinput2 = Jonsinput2a	#客入的名

		Jonsinput3a = input('出生年後2位...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput3a) == 0 ):
			Jonsinput3 = str('19'+str(random.randint(79,99)))	#隨機2個數字
		else:
			Jonsinput3 = str('19'+Jonsinput3a)	#客入的2個數字

		Jonsinput4a = input('月...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput4a) == 0 ):
			Jonsinput4 = str(random.randint(1,12))	#隨機2個數字
		else:
			Jonsinput4 = Jonsinput4a	#客入的2個數字

		Jonsinput5a = input('日...\n*不填寫會用隨機2個數字')
		if (len(Jonsinput5a) == 0 ):
			Jonsinput5 = str(random.randint(1,28))	#隨機2個數字
		else:
			Jonsinput5 = Jonsinput5a	#客入的2個數字

		Jonsinput6a = input('GAC...\n*不填寫會用隨機生成的英文姓名組成')
		if (len(Jonsinput6a) == 0 ):
			Jonsinput6 = str(Jonsinput1+Jonsinput2)	#隨機2個數字
		else:
			Jonsinput6 = Jonsinput6a	#客入的2個數字

		Jonsinput7a = input('GPS...\n*不填寫會用隨機15個英文數字')
		if (len(Jonsinput7a) == 0 ):
			Jonsinput7 = _GenPassword(15)	#15字密碼
		else:
			Jonsinput7 = Jonsinput7a	#客入的2個數字
		_printDate(),_SaveDate()
#############################################_MakeDateEND












#############################################_SaveDate
def _SaveDate():
	global a0json
	print ('開始存檔')
	JonsinputAll = {
		'Date': [
			{
			#############################################
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






















#開Gmail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def _MakeGoogleAC():
	global GmailPS
	print ('\n_MakeGoogleAC 自動開ac 202101230510')
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













#生成随机密码
import random
import string
GmailPS = 0
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







