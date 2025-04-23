def calcular_costo_compra():
    print("=== Sistema de Cálculo de Costo Total de Compra ===")
    
    # Solicitar datos del producto
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    # Validar y obtener precio unitario
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("Error: El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido para el precio.")
    
    # Validar y obtener cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número entero positivo.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un valor entero válido para la cantidad.")
    
    # Validar y obtener descuento
    while True:
        try:
            descuento = float(input("Ingrese el porcentaje de descuento (0-100%): "))
            if descuento < 0 or descuento > 50:
                print("Error: El descuento debe estar entre 0% y 50%.")
                continue
            break
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido para el descuento.")
    
    # Cálculos
    subtotal = precio_unitario * cantidad
    monto_descuento = subtotal * (descuento / 50)
    total = subtotal - monto_descuento
    
    # Mostrar resultados
    print("\n--- Resumen de la Compra ---")
    print(f"Producto: {nombre_producto}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento ({descuento}%): -${monto_descuento:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------------")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_costo_compra()