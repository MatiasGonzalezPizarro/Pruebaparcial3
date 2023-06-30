import funcionesPrueba3MatiasGonzalez as fn
import datetime as date
opc=0
opcCat=0
nombres=[]
categoria=[]
nombreDuos=[]
fechaNacs=[]
ruts=[]
correos=[]
fonos=[]
while opc!=4:
    print("Padel Yari VillaGrande")
    print("*"*25)
    print("1)Ingresar Participantes \n2)Buscar participante \n3)Mostrar Parejas \n4)Salir")
    opc=fn.validaOpc(int,"Opcion deseada: ",1,4)
    if opc==1:
        nom=fn.validaNomb(str,"Ingresa Nombre: ",2,80)
        nombres.append(nom)
        rut=fn.validaRut(int,"Ingresa Rut(sin Dv):",5000000,50000000)
        ruts.append(rut)
        nomDuo=fn.validaNomb(str,"Ingresa Nombre del Duo:",1,80)
        nombreDuos.append(nomDuo)
        correo=fn.validaCorreo()
        correos.append(correo)
        fono=fn.validaFono(int,"Ingresa Celular:",100000000,999999999)
        fonos.append(fono)
        while opcCat!=3:
            opcCat=fn.validaOpc(int,"Seleccione Categoria: \n1)Oro \n2)Plata \n3)Bronce \n-->",1,3)
            if opcCat==1:
                cat='Oro'
                categoria.append(cat)
                break
            elif opcCat==2:
                cat='Plata'
                categoria.append(cat)
                break
            else:
                cat='Bronce'
                categoria.append(cat)  
                break
    elif opc==2:
     rutBusqueda=fn.validaRut(int,"Ingresa Rut (sin Dv):",5000000,50000000)
     for r in range(len(ruts)):
      if rutBusqueda==ruts[r]:
        print(f"{nombres[r]} | {categoria[r]} | {fonos[r]} |  {correos[r]}")
      else:
        print("Rut Inexistente")    
    elif opc==3:
     nomDuoBuscar=input("Ingrese el Nombre del duo que desea buscar:")
     for n in range(len(nombreDuos)):
      if nomDuoBuscar==nombreDuos[n]:
        print(f"{nombres[n]} | {categoria[n]}")
      else:
        print("Duo Inexistente")
    else:
       fn.Despedida()                      
        




