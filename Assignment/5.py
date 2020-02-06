lluvia_mensual = [5, 4, 8, 10, 9, 0, 1, 5, 6, 8, 8, 7]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
         'Diciembre']
max_lluvia = max(lluvia_mensual)
print(max_lluvia)
mes_max = meses[lluvia_mensual.index(max_lluvia)]
print(mes_max)
print('El mes mas lluvioso es', str(mes_max), 'con', str(max_lluvia), 'litros')
