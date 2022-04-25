
agua=600
azucar=1200
aceite=1500
arroz=1250
fideos=790
bebida = 1780
chocolate = 2500
pan_molde = 1340

contador=0
productos=[]
total_compra=0
p1=input('Quiere llevar agua?: ')
if p1 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(agua*c)
    productos.append(f'Agua: {agua}*{c}')
p2=input('Quiere llevar azucar?: ')
if p2 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(azucar*c)
    productos.append(f'Azucar:{azucar}*{c} ')
p3=input('Quiere llevar aceite?: ')
if p3 == 'si':
    c=int(input('Cuanto?'))
    contador=contador+(aceite*c)
    productos.append(f'Aceite: {aceite}*{c}')
p4=input('Quiere llevar arroz?: ')
if p4 == 'si':
   c=int(input('Cuanto?'))
   contador=contador+(arroz*c)
   productos.append(f'arroz: {arroz}*{c}')
p5=input('Quiere llevar fideos?: ')
if p5 == 'si':
   c=int(input('Cuanto?'))
   contador=contador+(fideos*c)
   productos.append(f'fideos: {fideos}*{c}') 
p6=input('Quiere llevar bebida?: ')
if p6 == 'si':
   c=int(input('Cuanto?'))
   contador=contador+(bebida*c)
   productos.append(f'bebida: {bebida}*{c}') 
p7=input('Quiere llevar chocolate?: ')
if p7 == 'si':
   c=int(input('Cuanto?'))
   contador=contador+(chocolate*c)
   productos.append(f'chocolate: {chocolate}*{c}') 
p8=input('Quiere llevar pan_molde?: ')
if p8 == 'si':
   c=int(input('Cuanto?'))
   contador=contador+(pan_molde*c)
   productos.append(f'pan_molde: {pan_molde}*{c}')

cliente_preferencial = str(input('Es cliente preferencial?: '))
if cliente_preferencial == 'si':
  print('Usted es Cliente preferencial y tiene disponible un 25 porciento de descuento')
  print(f'El total de su compra es: {contador}')
  total_compra=total_compra+(contador-(contador*0.25))
  print(f'El total de su compra con el descuento es: {total_compra}')
  efectivo = int(input('Con cuanto paga?'))
  vuelto = efectivo-total_compra
  vuelto2 = efectivo-contador
  if efectivo>=total_compra:
    print(f'su vuelto es: {vuelto}' )
  elif efectivo<total_compra:
    print(f'el total es{vuelto}')  
    print('Dinero insuficiente, Guardias!')
elif cliente_preferencial == 'no': 
   print('Usted no es Cliente Preferencial')
   print(f'El total de su compra es: {contador}')
   efectivo = int(input('Con cuanto paga?'))
   vuelto2 = efectivo-contador
   if efectivo>=contador:
        print(f'el vuelto es: {vuelto2}')
   elif efectivo<contador:
    print(f'el total es{vuelto2}')   
    print('Dinero insuficiente, Guardias!')   
  