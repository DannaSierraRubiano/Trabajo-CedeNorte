import time

def cronometro(tiempo_segundos):
    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + tiempo_segundos
    
    while time.time() < tiempo_final:
        tiempo_restante = int(tiempo_final - time.time())
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60
        print(f"Tiempo restante: {minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    
    print("¡Tiempo completado!")

tiempo_minutos = 1
tiempo_segundos = tiempo_minutos * 60
cronometro(tiempo_segundos)
