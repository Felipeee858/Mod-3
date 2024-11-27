from datetime import datetime
import time
while True:
    hora_atual=print(datetime.now()).strftime("%H:%M:%S")
    print(hora_atual)
    #Esperar 1 segundo
    time.sleep(1)
    if datetime.now().hour>=16 and datetime.now().minute>=35 and datetime.now().second>=0 and despertou==False:
        print("ACORDA!!!!!!!")
        despertou=True
