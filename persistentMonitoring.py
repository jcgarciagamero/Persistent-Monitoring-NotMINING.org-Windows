# -*- coding: utf-8 -*-ç
#Version: 0.0.4

import urllib
import psutil
import os
import time
import sys
from PyQt4 import QtGui  
from PyQt4.QtGui import QMessageBox  
aplicacion = QtGui.QApplication(sys.argv)


i = 0
while i == 0:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 30.0:
			
			cpu = psutil.cpu_percent()
			os.system('netstat.py > net.html')
			scan = "net.html"
			lines = urllib.urlopen(scan).read()
			search = lines.find('104.20.209.59')
			search1 = lines.find('185.170.115.65')
			search2 = lines.find('164.132.200.121')
			search3 = lines.find('104.25.6.31')
			search4 = lines.find('104.24.104.76')
			search5 = lines.find('104.18.55.211')
			search6 = lines.find('104.27.185.32')
			search7 = lines.find('158.69.252.241')
			search8 = lines.find('165.227.198.137')
			search9 = lines.find('85.17.26.66')
			search10 = lines.find('104.31.93.36')
			search11 = lines.find('104.31.92.36')
			search12 = lines.find('52.57.80.78')
			search13 = lines.find('5.255.86.116')
			search14 = lines.find('45.77.196.10')
			search15 = lines.find('45.63.109.36')
			search16 = lines.find('207.246.116.117')
			search17 = lines.find('45.77.192.104')
			search18 = lines.find('188.166.33.242')			
			search19 = lines.find('178.62.227.52')	 		
			search20 = lines.find('104.18.46.158')
			search21 = lines.find('104.27.152.155')
			search22 = lines.find('104.18.54.211')
			search23 = lines.find('185.183.156.241')
			search24 = lines.find('104.20.208.59')
			search25 = lines.find('217.182.164.14')
			search26 = lines.find('37.187.167.70')
			search27 = lines.find('37.187.165.17')
			search28 = lines.find('37.187.165.41')
			search29 = lines.find('37.187.165.207')
			search30 = lines.find('37.187.165.210')
			search31 = lines.find('37.187.166.108')
			search32 = lines.find('37.187.167.21')
			search33 = lines.find('37.187.167.30')
			search34 = lines.find('37.187.167.36')
			search35 = lines.find('37.187.167.47')
			search36 = lines.find('37.187.167.69')
			search37 = lines.find('37.187.167.70')
			search38 = lines.find('37.187.167.72')
			search39 = lines.find('37.187.167.83')
			search40 = lines.find('104.28.16.102')

			if search != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search1 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gustaver.ddns.net',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search2 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with pon.ewtuyytdf45.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search3 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search4 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with mepirtedic.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search5 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with aster18cdn.nl',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search6 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with cdn.whysoserius.club',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search7 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with gtg02.bestsecurepractice.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search8 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with beta00.cortacoin.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search9 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with freecontent.*',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search10 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypto-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search11 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with crypta-loot.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search12 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with webminerpool.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search13 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Proxy: wss://javascriptcdn.stream:8892/proxy , Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search14 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search15 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search16 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search17 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: herphemiste.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search18 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: web.stati.bid',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search19 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: g-content.bid',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search20 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: coin-have.com',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search21 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with: 1q2w3.website',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search22 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with aster18cdn.nl',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search23 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with eth-pocket.de',
				QMessageBox.Ok,
				QMessageBox.Ok)	
			elif search24 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search25 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search26 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search27 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search28 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search29 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search29 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search30 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search31 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search32 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search33 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search34 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search35 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search36 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search37 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search38 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search39 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with Coinhive',
				QMessageBox.Ok,
				QMessageBox.Ok)
			elif search40 != -1:
				QMessageBox.information(None, 'Persistent Monitoring (NotMINING.org)', u'Mining with tulip18.com/amo.js',
				QMessageBox.Ok,
				QMessageBox.Ok)
			os.system('del net.html')
			time.sleep( 10 )

