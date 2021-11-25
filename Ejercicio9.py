from datetime import datetime, timedelta

formato = "%d/%m/%Y"
contador = 0            
fechadesde = input('Fecha desde (dd/mm/aaaa): ')
fechahasta = input('Fecha hasta (dd/mm/aaaa): ')
if fechadesde == '' or fechahasta == '':
    exit()

try:                    
    fechadesde = datetime.strptime(fechadesde, formato)
    fechahasta = datetime.strptime(fechahasta, formato)    
    if fechadesde > fechahasta:
        print('Fecha desde debe ser menor o igual que hasta')
    
    while fechadesde <= fechahasta:
        if datetime.weekday(fechadesde) == 1: 
            contador +=5
            fechaactual = fechadesde.strftime(formato)
            print(contador, fechaactual, 'DOMINGO')
        fechadesde = fechadesde + timedelta(days=1)
                
except:
    print('Fecha incorrecta')