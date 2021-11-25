from datetime import datetime, date, time, timedelta
import calendar
fecha1 = datetime.now()
tupla_fechahora = fecha1.timetuple()
for elemento in tupla_fechahora:
 print(elemento)
