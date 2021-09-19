from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date
import time
# Procesos de las Opciones del Menu Mantenimiento

def empAdministrativos():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS ADMINISTRATIVOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Nombre: ")
   gotoxy(15,6);print("Código Departamento: ")
   gotoxy(15,7);print("Código Cargo: ")
   gotoxy(15,8);print("Dirección: ")
   gotoxy(15,9);print("Cédula: ")
   gotoxy(15,10);print("Teléfono: ")
   gotoxy(15,11);print("Fecha de Ingreso: ")
   gotoxy(15,12);print("Sueldo: ")
   gotoxy(23,5);nombre = input() 
   gotoxy(36,6);codigo= input()    
   gotoxy(23,5);nombre = input()
   gotoxy(36,6);departamento= input()
   gotoxy(29,7);cargo= input()
   gotoxy(26,8);dirreccion= input()
   gotoxy(23,9);cedula= input()
   gotoxy(25,10);telef= input()
   gotoxy(33,11);fechaIngreso= input()
   gotoxy(23,12);sueldo= int(input())
   gotoxy(15 ,15);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
   
def empObreros():
    borrarPantalla()     
    gotoxy(20,2);print("MANTENIMIENTO DE EMPLEADOS OBREROS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Nombre: ")
    gotoxy(15,6);print("Código Departamento: ")
    gotoxy(15,7);print("Código Cargo: ")
    gotoxy(15,8);print("Dirección: ")
    gotoxy(15,9);print("Cédula: ")
    gotoxy(15,10);print("Teléfono: ")
    gotoxy(15,11);print("Fecha de Ingreso: ")
    gotoxy(15,12);print("Sueldo: ")
    gotoxy(23,5);nombre = input() 
    gotoxy(36,6);codigo= input()    
    gotoxy(23,5);nombre = input()
    gotoxy(36,6);departamento= input()
    gotoxy(29,7);cargo= input()
    gotoxy(26,8);dirreccion= input()
    gotoxy(23,9);cedula= input()
    gotoxy(25,10);telef= input()
    gotoxy(33,11);fechaIngreso= input()
    gotoxy(23,12);sueldo= int(input())
    gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")

def cargos():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARGOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Cargo: ")
   gotoxy(33,5)
   desCargo = input()
   archiCargo = Archivo("./archivos/cargo.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   archiCargo.escribir([datos],"a")
   gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
   
def departamentos():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE DEPARTAMENTOS")
   gotoxy(15,5);print("Departamento: ")
   gotoxy(33,5)
   desCargo = input()
   archiCargo = Archivo("./archivos/departamento.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   archiCargo.escribir([datos],"a")
   gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")

def empresa():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE EMPRESA")
   gotoxy(15,4);print("Razón Social:")
   gotoxy(15,5);print("Dirección: ")
   gotoxy(15,6);print("Teléfono: ")
   gotoxy(15,7);print("Ruc: ")

   gotoxy(29,4);razon = input()
   gotoxy(26,5);dir = input()
   gotoxy(25,6);tel = input()
   gotoxy(20,7);ruc = input() 
   gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")

def deducciones():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE DEDUCCIONES")
   gotoxy(15,4);print("Valor iess:")
   gotoxy(15,5);print("Valor Comisión: ")
   gotoxy(15,6);print("Valor Antiguedad: ")
   gotoxy(27,4);iess = float(input())
   gotoxy(31,5);comi = float(input())
   gotoxy(33,6);anti = float(input())
   gotoxy(10,10);input("El Mantenimiento se ha guardado Satisfactoriamente\n Presione una tecla para continuar...")
   

   

# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40)
    
    
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   #gotoxy(23,6);aamm = input()
   gotoxy(23,7);h50 = input()
   gotoxy(24,8);h100 = input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
   
def prestamos():
   borrarPantalla()     
   gotoxy(20,2);print("INGRESO DEL VALOR: ")
   empleado,entEmpleado = [],None
   aamm,numPagos,cuotas=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre)
      archiEmpleado = Archivo("./archivos/administrativo.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
          gotoxy(35,5);print(entEmpleado.nombre) 

      else: 
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40)
    
    
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Valor:")
   gotoxy(15,8);print("numPagos:")
   gotoxy(15,9);print("cuotas: ")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   #gotoxy(23,6);aamm = input()
   gotoxy(23,7);h50 = input()
   gotoxy(24,8);h100 = input()
   gotoxy(25,9);coutas=input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/prestamo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")


# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O S")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

  

def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])       
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  


def rolObrero():
   borrarPantalla()
   gotoxy(20,2);print("ROL OBRERO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   if grabar == "s":
        # lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt","|")
            datosDet = nomina.getDetalle()
            #  graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
          
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")
# Menu  Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administratvos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            elif opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamentos()
            elif opc1 == "5":
                empresa()
            elif opc1 == "6":
                deducciones()
            
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            #elif opc3 == "3":
            #    consultaRol()
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

