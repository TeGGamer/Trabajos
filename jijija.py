print ("bienvenido a la tienda virtual de Deivis") 
producto = input("Que producto desea el dia de hoy: ")
while not producto.isalpha(): 
  print ("Solo caracteres validos intenta nuevamente")
  producto = input("Ingresa nuevamente el producto: ")
precio = float (input("cual es el precio del producto: " ))
while precio <=0 and precio if not isinstance(precio, float)
  print ("error") 
  precio = float (input("Digite un precio valido: " ))

cantidad = int(input ("Cuantas unidades desea adquirir?: "))
while cantidad <=0:
  print ("error") 
  cantidad = float (input("Digite una cantidad valdia: " ))
descuento = float(input("Ingrese el porcentaje de su descuento: "))
precio_descuento = precio * descuento / 100

print (f"El precio final de su producto con descuento: {precio_descuento:.2f} ")

