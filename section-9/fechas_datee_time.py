from datetime import datetime, time, date


hora = time(11, 2)
print(hora)

dia = date(2026, 6, 10)
print(dia)

ahora = datetime.now()
print(f"ahora es {ahora.date()} y son las {ahora.time()}")