import sys
from machine import Pin, I2C, ADC
from I2C_LCD import I2cLcd
from time import sleep

xV = ADC(28)
yV = ADC(27)
swV = Pin(26, Pin.IN, Pin.PULL_UP)

led_vert = Pin(17, Pin.OUT)
led_rouge = Pin(18, Pin.OUT)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def directions():
 
    val_sw = swV.value()
    val_x = xV.read_u16()
    val_y = yV.read_u16()
    etat_x = 0
    etat_y = 0
    etat_z = 0
    
    if val_y <= 600:
        etat_y = 1
        
    if val_y >= 60000:
        etat_y = 2
    if val_x <= 600:
        etat_x = 1
    if val_x >= 60000:
        etat_x = 2
    if val_sw == 0:
        etat_z = 1
    
    if etat_x == 0 and etat_y == 0 and etat_z == 0:
        return None
    elif etat_x == 1 and etat_y == 1:
        return "haut gauche"
    elif etat_x == 1 and etat_y == 2:
        return "bas gauche"
    elif etat_x == 2 and etat_y == 1:
        return "haut droite"
    elif etat_x == 2 and etat_y == 2:
        return "bas droite"
    elif etat_x == 1:
        return "gauche"
    elif etat_x == 2:
        return "droite"
    elif etat_y == 1:
        return "haut"
    elif etat_y == 2:
        return "bas"
    elif etat_z == 1:
        return "appuye"
    else:
        return None
    
keep_running = True
while True:
    rep = sys.stdin.readline().strip()
    
    if rep == "ON":
        led_rouge.off()
        led_vert.on()
        lcd.backlight_on()
        lcd.putstr("Systeme de captation demarre")
        sleep(1)
        lcd.clear()
        data_mesure = []
        try:
            statut = ""
            compteur = 0  # compteur de mouvements capturés
            while compteur < 6:  # sort de la boucle après 5 mouvements capturés
                etat = directions()
                if etat is not None and etat != statut:
                    data_mesure.append(etat)
                    lcd.backlight_on()
                    lcd.putstr(etat)
                    statut = etat
                    sleep(1)
                    lcd.clear()
                    compteur += 1
                    
                   
               
        except:
            pass
            
        lcd.backlight_on()
        lcd.putstr("Captation arrete")
        for i in range(2):
            sleep(0.7)
            lcd.backlight_off()
            sleep(0.7)
            lcd.backlight_on()
        sleep(0.7)
        lcd.backlight_off()
        sleep(1)
        lcd.backlight_on()
        lcd.clear()
    
    elif rep == "Description vide":
        
        led_vert.off()
        
        lcd.backlight_on()
        lcd.putstr("Il manque une description")
        sleep(2)
        lcd.clear()
        sleep(1)
        led_rouge.on()
        sleep(0.7)
        led_rouge.off()
        sleep(0.7)
        led_rouge.on()
        sleep(0.7)
        led_rouge.off()
        sleep(0.7)
        led_rouge.on()
        sleep(0.7)
        led_rouge.off()
        sleep(0.7)
        led_rouge.on()
        lcd.backlight_on()
        lcd.putstr("Systeme de captation desactive")
        sleep(2)
        lcd.clear()

    
       
        
        keep_running = False
    
    elif rep == "Description valide":
        
        lcd.backlight_on()
        lcd.putstr("Description correcte")
        sleep(2)
        lcd.clear()
        sleep(1)
        led_vert.on()
        sleep(0.7)
        led_vert.off()
        sleep(0.7)
        led_vert.on()
        sleep(0.7)
        led_vert.off()
        sleep(0.7)
        led_vert.on()
        sleep(0.7)
        led_vert.off()
        sleep(0.7)
        led_vert.on()
        sleep(0.7)
        led_vert.off()
        lcd.backlight_on()
        lcd.putstr("Systeme de captation desactive")
        sleep(2)
        lcd.clear()
        led_rouge.on()
    
        keep_running = False
        
    

      
    
  

        
        
            
            
        
    