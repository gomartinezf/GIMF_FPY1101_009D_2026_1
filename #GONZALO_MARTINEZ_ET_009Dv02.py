#GONZALO_MARTINEZ_ET_009D

diccionario_planes ={'F01': ['Plan Básico', 'MENSUAL', 1, False,  False,  'libre'],
                    'F02': ['Plan Full', 'MENSUAL', 1, True, True, 'libre'],
                    'F03': ['Plan Estudiante', 'TRIMESTRAL', 3, False, True,'tarde'],
                    'F04': ['Plan Senior', 'TRIMESTRAL', 3, True, False, 'mañana'],
                    'F05': ['Plan Anual Pro', 'ANUAL', 12, True, True, 'libre'],
                    'F06': ['Plan Nocturno', 'MENSUAL', 1, False, True, 'noche']}
diccionario_inscripciones = {'F01': [14990, 30],
                            'F02': [22990, 10],
                            'F03': [39990, 0],
                            'F04': [35990, 6],
                            'F05': [159990, 2],
                            'F06': [18990, 15]}

def menu_principal():
    print('========== MENÚ PRINCIPAL ==========')    
    print('1. Cupos por tipo de plan')
    print('2. Búsqueda de planes por rango de precio')
    print('3. Actualizar precio de plan')
    print('4. Agregar plan')
    print('5. Eliminar plan')
    print('6. Salir')
    print('====================================\n')

def leer_opcion():
    while True:
        if opcion == "":
            print('Error, la opcion no puede quedar vacia.\n')
        elif opcion.strip == "":
            print('Error, la opcion no puede contener solo espacios.\n')
        else:
            try:
                opcion = int(opcion)
                if opcion not in (1,2,3,4,5,6):
                    print('Error, opcion ingresada no valida\n')
                else:
                    return opcion
            except ValueError as e:
                print(f'Error, respuesta no valida, error:{e}\n')

def detalle_plan(codigo_plan):
    for codigo_plan,tipo,cupos in diccionario_planes:
        
        
    
        cupos_disp = int(0)

    print(f'La cantidad de cupos disponibles es: {cupos_disp}.\n')

def cupos_tipo(tipo):
    print('*****CUPOS POR TIPO DE PLAN****\n')

    tipo = input('Ingrese el tipo de plan a solicitar cupos.(Mensual, Trimestral, Anual)')
    tipo == str(tipo.upper)
    
    if tipo == "":
            print('Error, la respuesta no puede quedar vacia.\n')
    elif tipo.strip == "":
            print('Error, la respuesta no puede contener solo espacios.\n')
  
    elif tipo not in diccionario_planes['F01'][1] or diccionario_planes['F02'][1] or diccionario_planes['F03'][1] or diccionario_planes['F04'][1] or diccionario_planes['F05'][1] or diccionario_planes['F06'][1]:
        print('Error, no se encuentran planes con esas caracteristicas.\n')

    else:
        detalle_plan()

def filtro_plan_rango_precio():
    while True:
        Precio_min = input('Ingrese el precio minimo:')
        Precio_max = input('Ingrese el precio maximo:')

        if Precio_min or Precio_max == "":
            print('Error, las respuestas no puede quedar vacias.\n')
        elif Precio_max.strip or Precio_min.strip == "":
            print('Error, las respuestas no puede contener solo espacios.\n')

        else:
            try:
             Precio_max = float(Precio_max)
             Precio_min = float(Precio_min)
             if Precio_min < 0 or Precio_max < 0:
                print('Error, no pueden ser numeros negativos.')
             if Precio_min>Precio_max:
                 print('Error, el precio minimo no puede ser mayor al precio maximo.') 
             return Precio_max, Precio_min     
            except ValueError as e:
                print(f'Error, respuesta no valida, ingrese una respuesta valida. error: {e}')

def busqueda_precio(Precio_min,Precio_max):
    print('*****BUSQUEDA DE PLAN POR RANGO DE PRECIO****\n')

    Precio_min, Precio_max = filtro_plan_rango_precio()

    plan_en_rango = []

    for codigo(precio,cupos) in diccionario_inscripciones():
            if (Precio_min <= precio <=Precio_max) and (cupos>0):
                plan_en_rango.append(codigo, diccionario_inscripciones[codigo][0], precio, cupos)
            if plan_en_rango:
                print(f'Planesdisponibles entre {Precio_min} - {Precio_max}.\n')
            for codigo, tipo , precio, cupos in plan_en_rango:
                print(f'Codigo:{codigo}, Plan: {tipo}, Cupos: {cupos}, Precio: {precio}')
            else:
                print(f'No se encontraron planes disponibles en ese rango de precio.')

def buscar_codigo():
    codigo_plan = ""
    while True:
        codigo_plan = input('Ingrese el codigo del plan: ')
        if codigo_plan == "":
            print('Error, el codigo no puede quedar vacio.')
        elif codigo_plan.strip == "":
            print('Error, el codigo no puede contener solo espacios.')
        elif codigo_plan not in diccionario_inscripciones:
            print('Error, el codigo ingresado no existe.')
        else:
            print(f'EL codigo se encuentra en el diccionario.\n')
            return True, codigo_plan
        
def actualizar_precio(codigo_plan,precio_nuevo):
    estado_actualizacion = False
    estado_actualizacion,codigo_plan = validar_precio_plan()
    if estado_actualizacion:
        print(f'El precio del plan{codigo_plan} ha sido actualizado: {diccionario_inscripciones[codigo_plan][0]}\n')
    else:
        print('Se ha cancelado la operacion.\n')

def validar_precio_plan():
    estado_busqueda = False
    estado_busqueda, codigo_plan = buscar_codigo()
    if estado_busqueda == False:
        return False, codigo_plan
    else:
        while True:
            print(f'Desea actualizar el plan: {codigo_plan}?s/n.')
            if input().lower() == 's':
                precio_nuevo = input(f'Ingrese el nuevo precio para el plan: {codigo_plan}')
            if precio_nuevo == "":
                    print('Error, el precio no puede quedar vacio.')
            elif precio_nuevo.strip == "":
                print('Error, el precio no puede contener solo espacios.')
            else:
                try:
                    precio_nuevo = int(precio_nuevo)
                    if precio_nuevo<0:
                        print('Error, el precio debe ser mayor a 0')
                    diccionario_inscripciones[codigo_plan][0]=int(precio_nuevo)
                    print(f'El precio de {codigo_plan} ha sido actualizado a: {diccionario_inscripciones[codigo_plan][0]}')
                    return True, codigo_plan
                except ValueError as e:
                    print(f'Error, ingrese una respuesta valida. error: {e}.')

def validar_codigo(nuevo_codigo):
    if nuevo_codigo == "":
        print('Error, no puede quedar vacio.')
    elif nuevo_codigo.strip == "":
        print('Error, no puede contener solo espacios')
    else:
        return True
    
def validar_nombre(nuevo_nombre):
    if nuevo_nombre == "":
        print('Error, no puede quedar vacio.')
    elif nuevo_nombre.strip == "":
        print('Error, no puede contener solo espacios')
    else:
        return True
    
def validar_nombre(nuevo_tipo):
    if nuevo_tipo == "":
        print('Error, no puede quedar vacio.')
    elif nuevo_tipo.strip == "":
        print('Error, no puede contener solo espacios')
    else:
        return True
    
def validar_nombre(nuevo_duracion):
    if nuevo_duracion == "":
        print('Error, no puede quedar vacio.')
    elif nuevo_duracion.strip == "":
        print('Error, no puede contener solo espacios')
    else:
        try:
            nuevo_duracion = int(nuevo_duracion)
            if nuevo_duracion<0:
                return False
            return True
        except ValueError:

            
        
def agregar_plan():
    nuevo_codigo   = input ('Ingrese el codigo del nuevo plan:')
    nuevo_nombre   = input ('Ingrese el nombre del nuevo plan:')
    nuevo_tipo     = input ('Ingrese el tipo del nuevo plan:')
    nuevo_duracion = input ('Ingrese la nueva duracion del nuevo plan:')
    nuevo_acceso_p = input ('Ingrese si tiene acceso a piscina el nuevo plan: (s/n)')
    nuevo_incluyec = input ('Ingrese si incluye clases el nuevo plan: (s/n)')
    nuevo_horario  = input ('Ingrese el horario del nuevo plan:')
    nuevo_precio   = input ('Ingrese el precio del nuevo plan:')
    nuevo_cupos    = input ('Ingrese los cupos del nuevo plan:')

    bool_codigo= validar_codigo(nuevo_codigo)



































            
                




