print ("bienvenido a la tienda virtual de Deivis") 
producto = input("Que producto desea el dia de hoy: ")
while not producto.isalpha(): 
  print ("Solo caracteres validos intenta nuevamente")
  producto = input("Ingresa nuevamente el producto: ")

while True:
  precio = (input("Cual es el precio del producto: "))
  
  
  if not precio.isalpha():
      if float (precio) >0:
        
        break
      else:
        print ("Error numero mayores a 0 ")
        
        continue
  else:
     print("Error solo numeros")   

while True: 
  cantidad = (input("Ingrese cantidad de producto: "))
  
  if not cantidad.isalpha():
      if float (cantidad) >0:
          
        break
      else:
        print("Error numeros mayores a 0 ")
    
        continue 
  else:
       print ("Error solo numeros")
    
while True:
  descuento = (input("Ingrese el valor del descuento proporcionado: "))
  
  if not descuento.isalpha():
    if float (descuento)>0:
      
      break
    else: 
        print("Solo valores mayores a 0 ")
    
    continue
  else: print("Ingrese solo valores numericos ")
  

#Calculador
 
P = float(precio)
C = float(cantidad)
D = float(descuento)

Stotal = P * C
print (type(Stotal))  
print(f"resultado: {Stotal}")

descuento_total = Stotal * (D / 100)
total = Stotal-descuento_total
  
#resultados
print("Esta es tu compra")
print(f"Producto: {producto}")
print(f"Precio unitario: {precio}")
print(f"Stotal: {Stotal}") 
print(f"Total:{total}")

precio_descuento = P * D / 100

print (f"El precio final de su producto con descuento: {total:.2f} ")

