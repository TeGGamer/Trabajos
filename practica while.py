while True:
    descuento = (input("ingrese descuento: "))
    
    if not descuento.isalpha():
       if float (descuento) >0:
        break
       else:
         print("Solo numeros mayores a 0")     
    else:
        print("Error solo numeros")
    
    continue