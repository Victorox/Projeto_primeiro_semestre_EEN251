import pygame
import serial
import os

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)



while 1 :
  variavel = comunicacaoSerial.readline()  
  variavel = variavel.replace(" ","")
  variavel = variavel.replace("\0","")
  variavel = variavel.replace("\n","")
  variavel = variavel.replace("\r","")

  for tecla in variavel:
    print(tecla)
    letra=0
    if tecla == ("A"):
        letra = tecla
    else:
        numero = tecla
    
    
    #print(letra)
    
    if "A" == letra:
        L=[]
        numero=0
        x=0
        while x < len(L):
            x = numero
            L.append(x)
            print(L)
        
    
    
    if "C" == letra:
        reproduzir(L)
    
    
    
    if "1" == numero:
        pygame.init()
        pygame.mixer.music.load('A-Conga-Hi-Muted-1.mp3')
        pygame.mixer.music.play()
    if "2" == numero:
        pygame.init()
        pygame.mixer.music.load('Clap.mp3')
        pygame.mixer.music.play()
    if "3" == numero:
        pygame.init()
        pygame.mixer.music.load('Bright-Ride.mp3')
        pygame.mixer.music.play()
    if "4" == numero:
        pygame.init()
        pygame.mixer.music.load('Crash.mp3')
        pygame.mixer.music.play()
    if "5" == numero:
        pygame.init()
        pygame.mixer.music.load('Kick-808-Thud.mp3')
        pygame.mixer.music.play()
    if "6" == numero:
        pygame.init()
        pygame.mixer.music.load('Kick-Smooth-Punt.mp3')
        pygame.mixer.music.play()
    if "7" == numero:
        pygame.init()
        pygame.mixer.music.load('Reverb Impact 5.mp3')
        pygame.mixer.music.play()    
    if "8" == numero:
        pygame.init()
        pygame.mixer.music.load('Snare.mp3')
        pygame.mixer.music.play()
    if "9" == numero:
                pygame.init()
                pygame.mixer.music.load('Snare.mp3')
                pygame.mixer.music.play()    
          
        
            
    def reproduzir(L):
        x=0
        while x < len(L):
            numero = L[x]
                
            if "1" == numero:
                pygame.init()
                pygame.mixer.music.load('A-Conga-Hi-Muted-1.mp3')
                pygame.mixer.music.play()
            if "2" == numero:
                pygame.init()
                pygame.mixer.music.load('Clap.mp3')
                pygame.mixer.music.play()
            if "3" == numero:
                pygame.init()
                pygame.mixer.music.load('Bright-Ride.mp3')
                pygame.mixer.music.play()
            if "4" == numero:
                pygame.init()
                pygame.mixer.music.load('Crash.mp3')
                pygame.mixer.music.play()
            if "5" == numero:
                pygame.init()
                pygame.mixer.music.load('Kick-808-Thud.mp3')
                pygame.mixer.music.play()
            if "6" == numero:
                pygame.init()
                pygame.mixer.music.load('Kick-Smooth-Punt.mp3')
                pygame.mixer.music.play()
            if "7" == numero:
                pygame.init()
                pygame.mixer.music.load('Reverb Impact 5.mp3')
                pygame.mixer.music.play()    
            if "8" == numero:
                pygame.init()
                pygame.mixer.music.load('Snare.mp3')
                pygame.mixer.music.play()
            if "9" == numero:
                pygame.init()
                pygame.mixer.music.load('Snare.mp3')
                pygame.mixer.music.play()
            
            
            x += 1
