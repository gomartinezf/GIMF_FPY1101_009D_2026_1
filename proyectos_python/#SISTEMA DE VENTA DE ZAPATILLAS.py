#SISTEMA DE VENTA DE ZAPATILLAS

#-----------------------------------------------------------------------------------------------
#===============================================================================================
#DICCIONARIO CON STOCK DE ZAPATILLAS
#===============================================================================================
#-----------------------------------------------------------------------------------------------
inventario = {
    '001' : {'modelo' : 'Air Max', 'precio' : 89990, 'stock' : 15},
    '002' : {'modelo' : 'Classic', 'precio' : 49990, 'stock' : 50},
    '003' : {'modelo' : 'Runner', 'precio' : 69990, 'stock' : 15},
    '004' : {'modelo' : 'Basquet', 'precio' : 79990, 'stock' : 15}
}
#-----------------------------------------------------------------------------------------------
#===============================================================================================
#METODOS DEF
#===============================================================================================
#-----------------------------------------------------------------------------------------------

#===============================================================================================
#***** METODO DE MOSTRAR INVENTARIO
#===============================================================================================
def mostrar_inventario():
    print('=' * 60)
    print(' ***** INVENTARIO TIENDA ZACATE ALTIRO LAH ZAPATILLAH *****')
    print('=' * 60)
    
    for codigo, dato in inventario.items():
        print(f'|{codigo} |{dato['modelo']:8} | ${dato['precio']:8} | {dato['stock']:8}|')
        print('-'*60)

#===============================================================================================
#***** METODO DE PROCESAR VENTA
#===============================================================================================

def procesar_venta():
    mostrar_inventario()

    codigo_zapatilla = input('Ingresa el codigo de la  zapatilla a vender: ')
    #===============================================================================================
    #validar el ingreso el codigo de la zapatilla a vender
    #===============================================================================================
    if codigo_zapatilla not in inventario:
        print('La zapatilla no esta registrada en el inventario.')
        return
    #===============================================================================================
    #solictar la cantidad de zapatillas a vender
    #===============================================================================================
    try:
        cantidad = int(input('Ingrese la cantidad de zapatillas a vender: '))
    except ValueError as e:
        print('Error, debe ingresar un codigo de zapatilla valido.')
        print('Error: ',e)
        return
    #===============================================================================================
    #validar que exista suficiente stock
    #===============================================================================================
    if cantidad <=0:
        print('Error: la cantidad no puede ser menor a cero.')
        return
    
    elif cantidad > inventario[codigo_zapatilla]['stock']:
        print('Error: no existe suficiente stock.')
        return
    #===============================================================================================
    #calcular venta
    #===============================================================================================
    precio_unitario = inventario[codigo_zapatilla]['precio']
    total_venta = precio_unitario * cantidad
    #===============================================================================================
    #Descontar de stock
    #===============================================================================================
    #inventario[codigo_zapatilla]['stock'] = inventario[codigo_zapatilla]['stock'] - cantidad
    inventario[codigo_zapatilla]['stock'] -= cantidad

    #===============================================================================================
    #Generar Boleta de venta
    #===============================================================================================

    print('\n=' * 60)
    print('******BOLETA ELECTRONICA*****')
    print('=' * 60)
    print(f'PRODUCTO        : {inventario[codigo_zapatilla]['modelo']}')
    print(f'PRECIO UNITARIO : {inventario[codigo_zapatilla]['precio']}')
    print(f'CANTIDAD        :{cantidad}')
    print(f'TOTAL A PAGAR   : ${total_venta}')
    print('-' * 60)
    print('GRACIAS POR COMPRAR EN LA TIENDA ZACATE ALTIRO LA ZAPATILLAH!!')

#===============================================================================================
#METODO PRINCIPAL
#===============================================================================================
def main():
    print('=' * 60)
    print('BIENVENIDO AL SISTEMA DE VENTA DE ZACATE ALTIRO LA ZAPATILLAH')
    print('=' * 60)
    
    while True:
        print('OPCIONES DEL SISTEMA:')
        print('1.- Ver inventario')
        print('2.- Realizar venta.')
        print('3.- Salir.\n')

        opcion = int(input('Ingrese la opcion deseada: '))

        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            procesar_venta()
        elif opcion == 3:
            print('MUCHAS GRACIAS POR COMPRAR EN NUESTRA TIENDA, DEJE SU BILLETERA ACA.')
            exit(0)
        else:
            print('Opcion ingresada no es valida.')




main()