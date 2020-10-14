import pygame
import serial
import os
import time
import requests
import math
import random

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)


TOKEN = "BBFF-aDjIqCcCAAkgyIV11REhZbctl9ElJw"  # Put your TOKEN here
DEVICE_LABEL = "Pad"  # Put your device label here 
VARIABLE_LABEL_1 = "gravacao"  # Put your first variable label here
L=[]



def post_request(gravacao):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=gravacao)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True
            
def main():
    variavel = comunicacaoSerial.readline()  
    variavel = variavel.replace(" ","")
    variavel = variavel.replace("\0","")
    variavel = variavel.replace("\n","")
    variavel = variavel.replace("\r","")

    global L

    for tecla in variavel:
      print(tecla)
      letra=""
      numero=""
      if tecla in ("A","C"):
          letra = tecla
      else:
          numero = tecla
        

        
    if "A" == letra:
        L=[]
      
      
    if "C" == letra:
        print(L)
        print("[INFO] Attemping to send data")
        post_request({"gravacao":{"value":1, "context":{"sequencia":str(L)}}
                      ,"1":{"value": 1 if "1" in L else 0}
                      ,"2":{"value": 1 if "2" in L else 0}
                      ,"3":{"value": 1 if "3" in L else 0}
                      ,"4":{"value": 1 if "4" in L else 0}
                      ,"5":{"value": 1 if "5" in L else 0}
                      ,"6":{"value": 1 if "6" in L else 0}
                      ,"7":{"value": 1 if "7" in L else 0}
                      ,"8":{"value": 1 if "8" in L else 0}
                      ,"9":{"value": 1 if "9" in L else 0}})
        print("[INFO] finished")
        reproduzir(L)
    
    
    
    if "1" == numero:
        pygame.init()
        pygame.mixer.music.load('kick1.mp3')
        pygame.mixer.music.play()
        L.append(numero)
            
                
    if "2" == numero:
        pygame.init()
        pygame.mixer.music.load('kick2.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "3" == numero:
        pygame.init()
        pygame.mixer.music.load('kick3.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "4" == numero:
        pygame.init()
        pygame.mixer.music.load('Crash.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "5" == numero:
        pygame.init()
        pygame.mixer.music.load('Clap.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "6" == numero:
        pygame.init()
        pygame.mixer.music.load('cymbal.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "7" == numero:
        pygame.init()
        pygame.mixer.music.load('Reverb.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "8" == numero:
        pygame.init()
        pygame.mixer.music.load('Snare.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "9" == numero:
        pygame.init()
        pygame.mixer.music.load('sirene.mp3')
        pygame.mixer.music.play()    
        L.append(numero)      
                
            
def reproduzir(L):
    
    for numero in L:
            
        if "1" == numero:
            #print ("oi")
            pygame.init()
            pygame.mixer.music.load('kick1.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "2" == numero:
            pygame.init()
            pygame.mixer.music.load('kick2.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
       
        
        if "3" == numero:
            pygame.init()
            pygame.mixer.music.load('kick3.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "4" == numero:
            pygame.init()
            pygame.mixer.music.load('Crash.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "5" == numero:
            pygame.init()
            pygame.mixer.music.load('Clap.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "6" == numero:
            pygame.init()
            pygame.mixer.music.load('cymbal.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "7" == numero:
            pygame.init()
            pygame.mixer.music.load('Reverb.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "8" == numero:
            pygame.init()
            pygame.mixer.music.load('Snare.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            
        if "9" == numero:
            pygame.init()
            pygame.mixer.music.load('sirene.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
               
if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
