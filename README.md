# Projeto EEN251

- Lucas Primati Menezes / 16.00683-6 / lprimati 

- Victoria Sumodjo / 16.01686-6 / vicsumodjo 

- Victor Rissato Duarte / 16.02961-5 / Victorox 

- Rodrigo Teixeira / 16.04031-7 / Rodrigotxs 

- Matheus Brandão Vasquez / 16.02052-9 / MatheusVasquez

-------------------------------------------------------------------

## Launch Pad

  Tem como objetivo reproduzir sons na ordem desejada.
  
### Raspberry PI com Arduino

####  Materiais: 
  
    -- Raspberry PI 3 Model B+
    
    -- Arduino UNO R3
    
    -- Teclado matrix 4x4 membrana
    
  Primeiramente programamos o *Arduino* para que ele fizesse a leitura do teclado de membrana quando clicassemos./n
  Com isso finalizado, conectamos o *Arduino* com o *Raspberry PI*, que recebia as informações do teclado em protocolo serial em formato *JSON*./n
  Através do progama em *Python* e da biblioteca *Pygame*, fizemos com que cada tecla reproduzisse um som. Além disso, deixamos uma tecla para gravar e uma para reproduzir.

#### Video do projeto
[![Programação em python](http://img.youtube.com/vi/HFNnqhk_Cmc/0.jpg)](http://www.youtube.com/watch?v=HFNnqhk_Cmc "Programação em python finalizada")

  Depois de tudo funcionando, fizemos uma interface no *Ubidots* para que sempre que apertassemos para reproduzir o que estava salvo, ele demonstrava o que estava salvo dentro da   lista de gravação e leds eram acesos mostrando que sons foram salvos.

#### Video de exemplo do Ubidots
[![Ubidots](http://img.youtube.com/vi/7rjObygRdwQ/0.jpg)](http://www.youtube.com/watch?v=7rjObygRdwQ "Ubitos finalizado")


