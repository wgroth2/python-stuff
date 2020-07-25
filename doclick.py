import pyautogui
import time
import urllib.request
#
# note py3 required
#
def doclick(num):
  for x in range(num):
    pyautogui.click()
    time.sleep(2)
    contents = urllib.request.urlopen("192.168.86.19:81/count.php").read()
    
   
