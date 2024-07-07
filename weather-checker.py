import requests
import serial
import time


latitude = 35.078000
longitude = -106.663160 #example location
temperature_threshold = 15 
api_key = "IMPUT_API_KEY_HERE" # get one from https://api-ninjas.com/


arduino = serial.Serial(port="COM6", baudrate=9600)  

def get_temperature():
  base_url = f"https://api.api-ninjas.com/v1/weather?lat={latitude}&lon={longitude}"
  print(base_url)
  response = requests.get(base_url, headers={"X-Api-Key": api_key})
  temp = response.json()["temp"]
  return temp

def send_to_arduino(data):
  arduino.write(data)
  print(data)



current_temp = get_temperature()


while True:
  time.sleep(0.1)
  if current_temp > temperature_threshold:
    send_to_arduino(False) # IDK HOW THIS WORKS BUT IT DOES SO IM NOT CHANGING IT
  else:
    send_to_arduino(True)