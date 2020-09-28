import pygame
import serial
import os

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)


L=[]

while 1 :
  variavel = comunicacaoSerial.readline()  
  variavel = variavel.replace(" ","")
  variavel = variavel.replace("\0","")
  variavel = variavel.replace("\n","")
  variavel = variavel.replace("\r","")

  for tecla in variavel:
    print(tecla)
    letra=""
    numero=""
    if tecla in ("A","C"):
        letra = tecla
    else:
        numero = tecla
    
    
    #print(letra)
    
    if "A" == letra:
        L=[]
        
        '''while x < len(L):
            x = numero
            L.append(x)
            print(L)'''
        
    
    
    if "C" == letra:
        print(L)
        reproduzir(L)
    
    
    
    if "1" == numero:
        pygame.init()
        pygame.mixer.music.load('A-Conga-Hi-Muted-1.mp3')
        pygame.mixer.music.play()
        L.append(numero)
            
    if "2" == numero:
        pygame.init()
        pygame.mixer.music.load('Clap.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "3" == numero:
        pygame.init()
        pygame.mixer.music.load('Bright-Ride.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "4" == numero:
        pygame.init()
        pygame.mixer.music.load('Crash.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "5" == numero:
        pygame.init()
        pygame.mixer.music.load('Kick-808-Thud.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "6" == numero:
        pygame.init()
        pygame.mixer.music.load('Kick-Smooth-Punt.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "7" == numero:
        pygame.init()
        pygame.mixer.music.load('Reverb Impact 5.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "8" == numero:
        pygame.init()
        pygame.mixer.music.load('Snare.mp3')
        pygame.mixer.music.play()
        L.append(numero)
        
    if "9" == numero:
        pygame.init()
        pygame.mixer.music.load('Snare.mp3')
        pygame.mixer.music.play()    
        L.append(numero)      
            
            
    def reproduzir(L):
        
        for numero in L:
                
            if "1" == numero:
                pygame.init()
                pygame.mixer.music.load('A-Conga-Hi-Muted-1.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                
            if "2" == numero:
                pygame.init()
                pygame.mixer.music.load('Clap.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                
           
            
            if "3" == numero:
                pygame.init()
                pygame.mixer.music.load('Bright-Ride.mp3')
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
                pygame.mixer.music.load('Kick-808-Thud.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                
            if "6" == numero:
                pygame.init()
                pygame.mixer.music.load('Kick-Smooth-Punt.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                
            if "7" == numero:
                pygame.init()
                pygame.mixer.music.load('Reverb Impact 5.mp3')
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
                pygame.mixer.music.load('Snare.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass
                   
            
            
