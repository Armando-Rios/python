import time

hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print("¡Es hora de ir a casa!")
else:
    horas_restantes = 19 - hora_actual
    minutos_restantes = (horas_restantes * 60) - time.localtime().tm_min
    print(
        f"Aún quedan {horas_restantes} horas y {minutos_restantes} minutos para ir a casa.")
