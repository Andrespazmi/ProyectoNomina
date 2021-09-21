from componentes import Menu, Valida
from helpers import borrarPantalla, gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date
import time



# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()
    validar = Valida()
    gotoxy(15, 2);print("EMPLEADOS ADMINISTRATIVOS")
    # Textos para datos a ingresar para Empleado Administrativo
    gotoxy(17, 4);print("Codigo:   ")
    gotoxy(17, 5);print("Nombre: ")
    gotoxy(17, 6);print("Dep.  ID[   ]: ")
    gotoxy(17, 7);print("Cargo ID[   ]: ")
    gotoxy(17, 8);print("Direccion: ")
    gotoxy(17, 9);print("Cédula: ")
    gotoxy(17, 10);print("Teléfono: ")
    gotoxy(17, 11);print("Fecha Ingreso: ")
    gotoxy(17, 12);print("Sueldo       : ")
    gotoxy(17, 13);print("Comisión     : ")

    gotoxy(33, 5);nomEmpl = validar.solo_letras(" Solo Se Admite Letras", 33, 5)
    # Al ingresar el Id del departamento busca la descripción 
    departamento = ""
    while not departamento:
        gotoxy(27, 6);id = input().upper()
        archiDepartamento = Archivo("./archivos/departamento.txt", "|")
        departamento = archiDepartamento.buscar(id)
        if departamento:
            entDepartamento = Departamento(departamento[1], departamento[0])
            gotoxy(33, 6);print(entDepartamento.descripcion)
        else:
            gotoxy(27, 6);print("No existe dicho Departamento [{}]:".format(id))
            time.sleep(2);
            gotoxy(27, 6);print("  " * 22)
            gotoxy(27, 6);print("  ]:")
    # Al ingresar el Id del Cargo busca la descripción
    cargo = ""
    while not cargo:
        gotoxy(27, 7);id = input().upper()
        archiCargo = Archivo("./archivos/cargo.txt", "|")
        cargo = archiCargo.buscar(id)
        if cargo:
            entCargo = Cargo(cargo[1], cargo[0])
            gotoxy(33, 7);print(entCargo.descripcion)
        
        else:
            gotoxy(27, 7);print("No existe dicho Cargo [{}]:".format(id))
            time.sleep(2)
            gotoxy(27, 7);print(" "*43)
            gotoxy(27, 7);print("  ]:")
    gotoxy(33, 8);direccion = validar.solo_letras("Solo se admite Letras", 33, 8)
    gotoxy(33, 9);cedula = validar.validar_cedula("Cédula Incorrecta vuelva a intentar", 33, 9)
    gotoxy(33, 10);telefono = validar.validar_tel("Teléfono Incorrecto vuelva a intentar", 33, 10)
    gotoxy(33, 11);fechaIngreso = input()
    gotoxy(33, 12);sueldo = validar.solo_decimales("Solo se admite números", 33, 12)
    gotoxy(33, 13);comision = input()
    gotoxy(15, 15);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 15);grabar = input().lower()
    if grabar == "s":
        archiEmplAdm = Archivo("./archivos/administrativo.txt","|")
        lista_administrativos = archiEmplAdm.leer()
        if lista_administrativos:
            idSig="A"+str(len(lista_administrativos)+1)
        else:
            idSig = 1
            idSig = ("A"+ str(idSig))
        Admin = Administrativo(nomEmpl, entDepartamento, entCargo, direccion, cedula, telefono, fechaIngreso, sueldo, idSig, comision)
        dato = Admin.getEmpleado()
        datos = '|'.join(dato)
        archiEmplAdm.escribir([datos],"a")   
        gotoxy(15, 16);input("Registro Grabado Satisfactoriamente\n             presione enter para continuar...")
    else:
        gotoxy(15, 16);input("Registro No fue Grabado\n presione enter para continuar...")

def empObreros():
    borrarPantalla()
    validar = Valida()
    gotoxy(15, 2);print("EMPLEADOS OBREROS")
    #  datos a ingresar para Empleado Administrativo
    gotoxy(17, 4);print("Codigo:          ")
    gotoxy(17, 5);print("Nombre       : ")
    gotoxy(17, 6);print("Dep.  ID[   ]: ")
    gotoxy(17, 7);print("Cargo ID[   ]: ")
    gotoxy(17, 8);print("Direccion    : ")
    gotoxy(17, 9);print("Cédula       : ")
    gotoxy(17, 10);print("Teléfono     : ")
    gotoxy(17, 11);print("Fecha Ingreso: ")
    gotoxy(17, 12);print("Sueldo       : ")
    gotoxy(17, 13);print("C. Colectivo : ")
    gotoxy(33, 5);nomEmpl = validar.solo_letras("Solo se admite Letras", 33, 5)
    departamento = ""
    while not departamento:
        gotoxy(27, 6);id_dep = input().upper()
        archiDepartamento = Archivo("./archivos/departamento.txt", "|")
        departamento = archiDepartamento.buscar(id_dep)
        if departamento:
            entDepartamento = Departamento(departamento[1], departamento[0])
            gotoxy(33, 6);print(entDepartamento.descripcion)
        else:
            gotoxy(25, 6);print("No existe dicho Departamento [{}]:".format(id_dep))
            time.sleep(2);
            gotoxy(25, 6);print(" " * 22)
            gotoxy(27, 6);print("  ]:")
    cargo = ""
    while not cargo:
        gotoxy(27, 7);
        archiCargo = Archivo("./archivos/cargo.txt", "|")
        id_carg = input().upper()
        cargo = archiCargo.buscar(id_carg)
        if cargo:
            entCargo = Cargo(cargo[1], cargo[0])
            gotoxy(33, 7);print(entCargo.descripcion)
        else:
            gotoxy(25, 7);
            print("No existe dicho Cargo [{}]:".format(id_carg))
            time.sleep(2)
            gotoxy(26, 7);print(" "*43)
            gotoxy(27, 7);print("  ]:")
    gotoxy(33, 8);direccion = validar.solo_letras("Solo se admite Letras", 33, 8)
    gotoxy(33, 9);cedula = validar.validar_cedula("Cédula Incorrecta vuelva a intentar", 33, 9)
    gotoxy(33, 10);telefono = validar.validar_tel("Teléfono Incorrecto vuelva a intentar", 33, 10)
    gotoxy(33, 11);fechaIngreso = input()
    gotoxy(33, 12);sueldo = validar.solo_decimales("Error: Agregar un (.) luego del número entero", 33, 12)
    gotoxy(33, 13);cc = input()
    gotoxy(15, 15);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 15);grabar = input().lower()
    if grabar == "s":
        archiObrero = Archivo("./archivos/obrero.txt", "|")
        lista_obreros = archiObrero.leer()
        if lista_obreros:
            idSig="O"+str(len(lista_obreros)+1)
        else:
            idSig = 1
            idSig = ("O"+ str(idSig))
        administrativo = Obrero(nomEmpl, entDepartamento, entCargo, direccion, cedula, telefono, fechaIngreso, sueldo, idSig, cc)
        datos = administrativo.getEmpleado()
        datos = '|'.join(datos)
        archiObrero.escribir([datos], "a")
        gotoxy(15, 15);input("Registro Grabado Satisfactoriamente\n              presione enter para continuar...")
    else:
        gotoxy(15, 16);input("Registro No fue Grabado\n             presione enter para continuar...")


def cargos():
    borrarPantalla()
    validar = Valida()
    # Textos para datos a ingresar para Cargos
    gotoxy(15, 2);print("MANTENIMIENTO DE CARGOS:")
    gotoxy(17, 4);print("Codigo:         ")
    gotoxy(17, 5);print("Descripcion Cargo: ")
    gotoxy(37, 5);desCargo = validar.solo_letras("Solo se admite Letras", 37, 5)
    gotoxy(15, 7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 7);grabar = input().lower()
    if grabar == "s":
        archiCargo = Archivo("./archivos/cargo.txt", "|")
        cargos = archiCargo.leer()
        if cargos:
            idSig = int(cargos[-1][0]) + 1
        else:
            idSig = 1
        cargo = Cargo(desCargo, idSig)
        datos = cargo.getCargo()
        datos = '|'.join(datos)
        archiCargo.escribir([datos], "a")
        gotoxy(15, 8);input("Registro Grabado Satisfactoriamente\n             presione enter para continuar...")
    else:
        gotoxy(15, 8);input("Registro No fue Grabado\n              presione enter para continuar...")


def departamentos():
    borrarPantalla()
    validar = Valida()
    gotoxy(15, 2);print("MANTENIMIENTO DE DEPARTAMENTOS:")
    # Textos para datos a ingresar para Departamentos
    gotoxy(17, 4);print("Codigo:        ")
    gotoxy(17, 5);print("Descripcion Departamento: ")
    gotoxy(44, 5);desDepart = validar.solo_letras("Solo se admite Letras", 44, 5)
    gotoxy(15, 7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 7);grabar = input().lower()
    if grabar == "s":
        archiDepart = Archivo("./archivos/departamento.txt", "|")
        departamentos = archiDepart.leer()
        if departamentos:
            idSig = int(departamentos[-1][0]) + 1
        else:
            idSig = 1
        departamento = Departamento(desDepart, idSig)
        datos = departamento.getDepartamento()
        datos = '|'.join(datos)
        archiDepart.escribir([datos], "a")
        gotoxy(15, 8);input("Registro Grabado Satisfactoriamente\n              presione enter para continuar...")
    else:
        gotoxy(15, 8);input("Registro No fue Grabado\n             presione enter para continuar...")


def empresa():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);print("MANTENIMIENTO EMPRESA")
    gotoxy(17, 4);print("Razón Social: ")
    gotoxy(17, 5);print("Dirección: ")
    gotoxy(17, 6);print("Teléfono: ")
    gotoxy(17, 7);print("Ruc: ")
    gotoxy(33, 4);n_empresa = validar.solo_letras("Solo se admite Letras", 37, 4)
    gotoxy(33, 5);direccion = validar.solo_letras("Solo se admite Letras", 37, 5)
    gotoxy(33, 6);telefono = validar.validar_tel("Teléfono Incorrecto vuelva a intentar", 33, 6)
    gotoxy(33, 7);ruc = validar.validar_ruc("Ruc Incorrecto vuelva a intentar", 33, 7)
    gotoxy(15, 9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 9);grabar = input().lower()
    if grabar == "s":
        archiEmpresa = Archivo("./archivos/empresa.txt", "|")
        empresa = Empresa(n_empresa, direccion, telefono, ruc)
        datos = empresa.getEmpresa()
        datos = '|'.join(datos)
        archiEmpresa.escribir([datos], "a")
        gotoxy(15, 8);input("Registro de Empresa Grabado Satisfactoriamente\n             presione enter para continuar...")
    else:
        gotoxy(15, 8);input("Registro No fue Grabado\n              presione enter para continuar...")

def parametros():
    borrarPantalla()  
    validar = Valida()
    gotoxy(15, 2);print("MANTENIMIENTO DE DEDUCCIONES:")
    gotoxy(17,4);print("Iess        : ")
    gotoxy(17,5);print("Comisión    : ")
    gotoxy(17,6);print("Antiguedad  : ")
    iess=validar.solo_decimales("Error: Solo numeros",33,4)
    comision=validar.solo_decimales("Error: Solo numeros",33,5)
    antiguedad=validar.solo_decimales("Error: Solo numeros",33,6)
    gotoxy(15,8);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,8);grabar = input().lower()
    if grabar == "s":
       archiDeducciones = Archivo("./archivos/deducciones.txt","|")
       archiDeducciones.leer()
       dedu = Deduccion(iess,comision,antiguedad)
       datos= dedu.getDeduccion()
       datos = '|'.join(datos)
       archiDeducciones.escribir([datos],"w")
       gotoxy(15,9);input("Registro Grabado Satisfactoriamente\n              presione enter para continuar...")
    else:
       gotoxy(15,9);input("Registro No fue Grabado\n              presione enter para continuar...")

# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
    borrarPantalla()
    validar = Valida()
    # Textos para datos a ingresar en horas extras
    gotoxy(15, 3);print("INGRESO DE HORAS EXTRAS: ")
    gotoxy(17, 6);print("Periodo        [aaaamm]: ")
    gotoxy(17, 7);print("Horas50: ")
    gotoxy(17, 8);print("Horas100: ")
    empleado, entEmpleado = [], None
    aamm, h50, h100 = 0, 0, 0
    while not empleado:
        gotoxy(17, 5);print("Empleado ID [    ]: ")
        gotoxy(32, 5);id = input().upper()
        archiEmpleado = Archivo("./archivos/obrero.txt", "|")
        empleado = archiEmpleado.buscar(id)
        if empleado:
            entEmpleado = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                 empleado[7], empleado[8], empleado[0])
            gotoxy(40, 5);print(entEmpleado.nombre)
        else:
            gotoxy(30, 5);print("No existe dicho Empleado [{}]:".format(id))
            time.sleep(2);
            gotoxy(30, 5);print(" " * 40)
    gotoxy(22, 6);aamm = validar.solo_numeros("Solo se admite Números", 33, 6)
    gotoxy(40, 7);h50 = validar.solo_numeros("Solo se admite Números", 33, 7)
    gotoxy(40, 8);h100 = validar.solo_numeros("Solo se admite Números", 33, 8)
    gotoxy(15, 10);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 10);grabar = input().lower()
    if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt", "|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos:
            idSig = int(sobretiempos[-1][0]) + 1
        else:
            idSig = 1
        sobretiempo = Sobretiempo(entEmpleado, aamm, h50, h100, True, idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos], "a")
        gotoxy(15, 11);input("Registro Grabado Satisfactoriamente\n              presione enter para continuar...")
    else:
        gotoxy(15, 11);input("Registro No fue Grabado\n              presione enter para continuar...")


def prestamos():
    borrarPantalla()
    validar = Valida()
    # Textos para datos a ingresar en prestamos
    gotoxy(15, 3);print("INGRESO DE PRÉSTAMOS:")
    gotoxy(17,5);print("Obrero-Administrativo(O/A): ")
    gotoxy(17, 6);print("Empleado ID [    ]: ")
    gotoxy(17, 7);print("Periodo [aaaamm]")
    gotoxy(17, 8);print("Valor             :    $")
    gotoxy(17, 9);print("Nº de Pagos       : ")
    gotoxy(17, 10);print("Cuota             : ")
    gotoxy(17, 11);print("Saldo             :    $")
    empleado, entEmpleado = [], None
    aamm, valor, n_pagos,  = 0, 0, 0
    rol = validar.solo_letras("Solo se admite letras", 45, 5)
    gotoxy(31, 6);id = input().upper()
    
    while not empleado:
        if rol == "A":
            archiEmpleado = Archivo("./archivos/administrativo.txt", "|")
            empleado = archiEmpleado.buscar(id)
            if empleado:
                entEmpleado = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                    empleado[7], empleado[8], empleado[0])
                gotoxy(40, 6);print(entEmpleado.nombre)
            else:
                gotoxy(27, 6);print("No existe dicho Empleado [{}]:".format(id))
                

        else:
            archiEmpleado = Archivo("./archivos/obrero.txt", "|")
            empleado = archiEmpleado.buscar(id)
            if empleado:
                entEmpleado = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                    empleado[7], empleado[8], empleado[0])
                gotoxy(40, 6);print(entEmpleado.nombre)
            else:
                gotoxy(27, 6);print("No existe dicho Empleado [{}]:".format(id))
                time.sleep(2);
                gotoxy(27, 6);
                print(" " * 40)

    gotoxy(26, 7);aamm = validar.solo_numeros("Solo se admite numeros", 26, 7)
    gotoxy(40, 8);valor = validar.solo_decimales("Agregar un (.) luego del número entero", 41, 8)
    gotoxy(40, 9);n_pagos = validar.solo_numeros("Solo se admite numeros", 40, 9)
    cuota = float(valor)/int(n_pagos)
    gotoxy(40, 10);print("$", cuota)
    gotoxy(41, 11);saldo = validar.solo_decimales("Agregar un (.) luego del número entero", 41, 11)

    gotoxy(15, 13);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(57, 13);grabar = input().lower()
    if grabar == "s":
        archiPrestamo = Archivo("./archivos/prestamo.txt", "|")
        prestamos = archiPrestamo.leer()
        if prestamos:
            idSig = int(prestamos[-1][0]) + 1
        else:
            idSig = 1
        prestamo = Prestamo(entEmpleado, aamm, valor, n_pagos, saldo, True, idSig)
        datos = prestamo.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos], "a")
        gotoxy(25, 14);input("Registro Grabado Satisfactoriamente\n presione enter para continuar...")
    else:
        gotoxy(15, 14);input("Registro No fue Grabado\n              presione enter para continuar...")
            

# opciones de Rol de Pago
def rolAdministrativo():
    borrarPantalla()
    validar = Valida()
    # Se ingresa los datos del rol a procesar
    gotoxy(15, 3);print("ROL ADMINISTRATIVO:")
    gotoxy(17, 6);print("Periodo [aaaamm]")
    gotoxy(26, 7);aamm = validar.solo_numeros("Solo se admite numeros", 26, 6)
    gotoxy(15, 7);
    print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54, 7);
    grabar = input().lower()
    entEmpAdm = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt", "|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm:
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt", "|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]), float(deducciones[1]), float(deducciones[2]))
            # print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(), aamm)
            for empleado in ListaEmpAdm:
                # print(empleado)
                entEmpAdm = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                           empleado[7], float(empleado[8]), empleado[0])
                # print(entEmpAdm.nombre,entEmpAdm.sueldo)
                nomina.calcularNominaDetalle(entEmpAdm, entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt", "|")
            archiRol.escribir([datosCab], "a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt", "|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm + '|' + '|'.join(dt)
                archiDet.escribir([dt], "a")
            # imprimir rol

            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                         entEmpresa.ruc, "A D M I N I S T R A T I V O S")
            nomina.mostrarDetalleNomina()

    else:
        gotoxy(10, 10);
        input("Rol No fue Procesado\n              presione enter para continuar...")

    input("             presione enter para continuar...")

def rolObrero():
    borrarPantalla()
    # Se ingresa los datos del rol a procesar
    gotoxy(20, 2);
    print("ROL OBRERO")
    aamm = 0
    gotoxy(15, 6);
    print("Periodo  [aaaamm]")
    validar = Valida()
    aamm = validar.solo_numeros("Solo se admite numeros", 25, 6)
    gotoxy(15, 7);
    print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54, 7);
    grabar = input().lower()
    entEmpObr = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt", "|")
        ListaEmpObr = archiEmp.leer()
        if ListaEmpObr:
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt", "|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]), float(deducciones[1]), float(deducciones[2]))
            print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(), aamm)
            for empleado in ListaEmpObr:
                entEmpObr = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], empleado[7], 
                float(empleado[8]), empleado[0])
                nomina.calcularNominaDetalle(entEmpObr, entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt", "|")
            archiRol.escribir([datosCab], "a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt", "|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm + '|' + '|'.join(dt)
                archiDet.escribir([dt], "a")
            # imprimir rol

            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                         entEmpresa.ruc, "O B R E R O S")
            nomina.mostrarDetalleNomina()
        else:
            pass

    else:
        gotoxy(10, 10);
        input("Rol No fue Procesado\n              presione enter para continuar...")

    input("              presione enter para continuar...")

def consultaRol():
    borrarPantalla()
    validar = Valida()
    # Se ingresa los datos del rol a Consultar     
    gotoxy(20,2);print("CONSULTA DE ROL ADMINISTRATIVO//OBRERO")
    rol=0
    aamm=""
    gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(44,4)
    rol=input().upper()
    aamm=validar.solo_numeros("Solo se admite numeros",23,6)
    gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
    gotoxy(54,7);procesar = input().lower()
    if procesar == "s":
        if rol == "A":
            tit = "A D M I N I S T R A T I V O S"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt", "|")
        else:
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt", "|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1], cabrol[0])
            entCabRol.totIngresos = float(cabrol[2])
            entCabRol.totDescuentos = float(cabrol[3])
            entCabRol.totPagoNeto = float(cabrol[4])
            detalle = archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])
                # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                            entEmpresa.ruc, tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(15, 10);
            input("No existe rol con ese periodo!!!\n              presione enter para continuar...")

    else:
        gotoxy(10, 10);
        input("Consulta Cancelada\n presione enter para continuar...")
    input("               presione enter para continuar...")


# Menu Proceso Principal
opc = ''
while opc != '4':
    borrarPantalla()

    menu = Menu("", 
                ["MENÚ PRINCIPAL:", 
                "       1) Mantenimiento                                       ",
                "       2) Novedades                                           ", 
                "       3) Rol de Pago                                         ", 
                "       4) Salir                                               "], 15, 2)

    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 != '7':
            borrarPantalla()
            menu1 = Menu("",
                         ["Menu Mantenimiento:",
                         "       1) Empleados Administrativos                           ", 
                         "       2) Empleados Obreros                                   ", 
                         "       3) Cargos                                              ", 
                         "       4) Departamentos                                       ",
                         "       5) Empresa                                             ", 
                         "       6) Parametros                                          ",
                         "       7) Salir                                               "], 15, 2)
            opc1 = menu1.menu()
            if opc1 == "1":
                borrarPantalla()
                empAdministrativos()

            elif opc1 == "2":
                borrarPantalla()
                empObreros()

            elif opc1 == "3":
                borrarPantalla()
                cargos()
            
            elif opc1 == "4":
                borrarPantalla()
                departamentos()

            elif opc1 == "5":
                borrarPantalla()
                empresa()

            elif opc1 == "6":
                borrarPantalla()
                parametros()

            elif opc1 == "7":
                borrarPantalla()
                print("Gracias por su visita....")

            else:
                print("Opcion no valida")


    elif opc == "2":
        opc2 = ''
        while opc2 != '3':
            borrarPantalla()
            menu2 = Menu("", 
                        ["Menu Novedades:", 
                        "       1) Sobretiempo                                          ", 
                        "       2) Prestamos                                            ", 
                        "       3) Salir                                                "], 15, 2)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()

            elif opc2 == "2":
                prestamos()
            
            elif opc2 == "3":
                borrarPantalla()
                print("Gracias por su visita....")
            else:
                print("Opcion no valida")


    elif opc == "3":
        opc3 = ''
        while opc3 != '4':
            borrarPantalla()
            menu3 = Menu("",
                        ["Menu Rol:",
                        "       1) Rol Administrativos                                 ", 
                        "       2) Rol Obreros                                         ", 
                        "       3) Consulta Rol                                        ", 
                        "       4) Salir                                               "],
                        15, 2)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()

            elif opc3 == "2":
                rolObrero()

            elif opc3 == "3":
                consultaRol()
        

            elif opc3 == "4":
                borrarPantalla()
                print("Gracias por su visita....")

            else:
                print("Opcion no valida")

    elif opc == "4":
        borrarPantalla()
        print("Gracias por su visita....")
    else:
        print("Opcion no valida")

input("Presione una tecla para salir")
borrarPantalla()
