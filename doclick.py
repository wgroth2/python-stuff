import pyautogui
import time
import sys

#
# note py3 required
#
def doclick(num):
  for x in range(num):
    pyautogui.click()
    time.sleep(2)
 
# Defining main function 
def main(): 
  num = int(sys.argv[1])
  print("num is " , num)
  doclick(num)
  print("Done.")

# Using the special variable  
# __name__ 
if __name__=="__main__": 
  main() 
