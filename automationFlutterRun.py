import os
import subprocess




adbTcp = "adb tcpip 55555"
# adbConnectOppo = "adb kill-server && adb connect 192.168.43.1:5555"
adbConnectS22 = "adb kill-server && adb connect 192.168.43.57:55555"
flutterRun = "flutter run"
openVsCode = "code ."
dirVsCode ="D:\\main\\ifmV2\\s3"


# cmd2 = "adb kill-server && adb tcpip 5555 &&adb connect 192.168.43.114:55555"
# returned_value = os.system(adbTcp)
# returned_value = os.system(adbConnectS22) 

os.chdir(dirVsCode)
returned_value = os.system(openVsCode) 
returned_value = os.system(flutterRun) 

