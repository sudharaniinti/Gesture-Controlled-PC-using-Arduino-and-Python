import serial #For Serial communication
import time #For Delay functions
import pyautogui #Python for GUI Automation
ArduinoSerial = serial.Serial('com3',9600) #Port-COM3 with Baudrate-9600
time.sleep(2) #Wait 2 seconds for the communication establishment
while 1:
  incoming = str (ArduinoSerial.readline()) #Reading the serial data
  print (incoming)
  if 'Play/Pause' in incoming:
    pyautogui.typewrite(['space'], 0.2)
  if 'Rewind' in incoming:
    pyautogui.hotkey('ctrl', 'left')
  if 'Forward' in incoming:
    pyautogui.hotkey('ctrl', 'right')
  if 'Vup' in incoming:
    pyautogui.hotkey('ctrl', 'down')
  if 'Vdown' in incoming:
    pyautogui.hotkey('ctrl', 'up')
  incoming = "";
