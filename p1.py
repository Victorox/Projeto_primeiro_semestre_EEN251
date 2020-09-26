import pygame
import serial
import os

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

        
while 1 :
  variavel = comunicacaoSerial.readline()  
  variavel = variavel.replace(" ","")
  variavel = variavel.replace("\0","")
  
  
  for letra in variavel:
    print(letra)
    if "1" == letra:
        pygame.init()
        pygame.mixer.music.load('A-Conga-Hi-Muted-1.mp3')
        pygame.mixer.music.play()
    if "2" == letra:
        pygame.init()
        pygame.mixer.music.load('Clap.mp3')
        pygame.mixer.music.play()
    if "3" == letra:
        pygame.init()
        pygame.mixer.music.load('Bright-Ride.mp3')
        pygame.mixer.music.play()
    if "4" == letra:
        pygame.init()
        pygame.mixer.music.load('Crash.mp3')
        pygame.mixer.music.play()
    if "5" == letra:
        pygame.init()
        pygame.mixer.music.load('Kick-808-Thud.mp3')
        pygame.mixer.music.play()
    if "6" == letra:
        pygame.init()
        pygame.mixer.music.load('Kick-Smooth-Punt.mp3')
        pygame.mixer.music.play()
    if "7" == letra:
        pygame.init()
        pygame.mixer.music.load('Reverb Impact 5.mp3')
        pygame.mixer.music.play()    
    if "8" == letra:
        pygame.init()
        pygame.mixer.music.load('Snare.mp3')
        pygame.mixer.music.play()
        #pygame.mixer.music.set_volume(1)

        #clock = pygame.time.Clock()
        #clock.tick(10)

        #while pygame.mixer.music.get_busy():
         #   pygame.event.poll()
          #  clock.tick(10)
            
