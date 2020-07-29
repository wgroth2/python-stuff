import pyautogui
import time
import urllib.request
from tkinter import * #required.
from tkinter import messagebox #for messagebox.

#
# note py3 required
#
def doclick(num):
  for x in range(num):
    pyautogui.click()
    time.sleep(2)
    contents = urllib.request.urlopen("192.168.86.19:81/count.php").read()
  App = Tk() #required.
  App.withdraw() #for hide window.
  messagebox.showinfo("Notification", "Done!") #msgbox
  App.mainloop() #required.    
