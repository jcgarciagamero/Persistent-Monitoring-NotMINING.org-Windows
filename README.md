# Persistent-Monitoring-NotMINING.org-Windows
Detect cryptocurrency mining patterns in your CPU and network.</br>
Requeriments:</br>
Python 2.7.15: https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi </br>
PyQt-Py2.7-x86-gpl-4.9.5-1:https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.9.5/PyQt-Py2.7-x86-gpl-4.9.5-1.exe/download </br>
PSUTIL Library: </br>
  Open CMD:</br>
  C:\Python27\python.exe -m pip install psutil</br>
Netstat python script: https://github.com/giampaolo/psutil/blob/master/scripts/netstat.py </br>

1º Edit start.bat:</br>

Change this line: Absolut path\persistentMonitoring.vbs</br>
for the absolut path where you put persistentMonitoring.vbs</br>

2º Copy start.bat on C:\Users\"YOUR USER"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup</br>

3º Edit persistentMonitoring.bat</br>

Change this line: cd absolute path</br>
for the absolute path where you put persistentMonitoring.bat</br>

4º Edit persistentMonitoring.vbs</br>
Change this line: </br>
WshShell.Run chr(34) & "absolut path\persistentMonitoring.bat" & Chr(34), 0</br>
for the abtolute path where you put persistentMonitoring.bat</br>

