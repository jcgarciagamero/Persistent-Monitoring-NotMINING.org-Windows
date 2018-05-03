Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\absolut path\persistentMonitoring.bat" & Chr(34), 0
Set WshShell = Nothing
