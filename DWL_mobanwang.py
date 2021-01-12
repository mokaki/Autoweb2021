
# -*- coding: utf-8 -*-
#AutoDWL_mobanwang
#202101121845
#!/usr/bin/python3
#!python*

# https://code.tutsplus.com/tutorials/how-to-download-files-in-python--cms-30099

import requests
import urllib


DwlNob = input('請問您想下載的網頁編號?')


url = 'http://www.mobanwang.com/mb/showsoftdown.asp?urlid=1&softid=' + DwlNob
rar = DwlNob + '.rar'


r = requests.get(url)
with open(rar, "wb") as code:
	code.write(r.content)

urllib.urlretrieve(url, rar)



os.system("pause")