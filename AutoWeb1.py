#-*- coding:utf-8 -*-
'''
自動開ac
202101230510
'''




import os















#開Gmail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def _MakeGoogleAC():
	print ('\n_MakeGoogleAC 自動開ac 202101230510')


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
GmailPS = 0
def _GenPasswordGmail():
	global GmailPS
	#生成10个随机密码   
	for i in range(1):
		#密码的长度为15
		#print (GenPassword(15))
		GmailPS = _GenPassword(15)
		print ('*****************生成随机密码*****************\n',GmailPS,'\n*****************\n')

def _GenPassword(length):
	chars=string.ascii_letters+string.digits
	return ''.join([random.choice(chars) for i in range(length)])#得出的结果中字符会有重复的
#生成随机密码END












_GenPasswordGmail(),_MakeGoogleAC()







