import datetime as date
def validaOpc(tipo,texto,ranMin=None,ranMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if ranMin!=None and ranMax!=None: 
                if ranMin<=nro<=ranMax:
                  break
                else:
                 print("Opcion Invalida")
            elif ranMin!=None:
               if ranMin<=nro:
                  break
               else:
                  print("Opcion Invalida")
            elif ranMax!=None:
               if ranMax>=nro:
                  break
               else:
                  print("Opcion Invalida")
            else:
               break
        except:
           print("Opcion debe ser un Numero")
    return nro                              
def validaNomb(tipo,texto,ranMin=None,ranMax=None):
    while True:
        try:
            nom=tipo(input(texto))
            if ranMin!=None and ranMax!=None: 
                if ranMin<=len(nom)<=ranMax:
                  break
                else:
                 print("Opcion Invalida")
            elif ranMin!=None:
               if ranMin<=len(nom):
                  break
               else:
                  print("Nombre tiene que tener mas de 1 caracter")
            elif ranMax!=None:
               if ranMax>=len(nom):
                  break
               else:
                  print("Nombre excede el limite de caracteres")
            else:
               break
        except:
           print("Nombre debe ser con letras")
    return nom                       
def validaRut(tipo,texto,ranMin=None,ranMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if ranMin!=None and ranMax!=None: 
                if ranMin<=nro<=ranMax:
                  break
                else:
                 print("Rut Invalido")
            elif ranMin!=None:
               if ranMin<=nro:
                  break
               else:
                  print(f"Rut debe ser mayor a {ranMin}")
            elif ranMax!=None:
               if ranMax>=nro:
                  break
               else:
                  print(f"Rut debe ser menor a {ranMax}")
            else:
               break
        except:
           print("Rut debe ser un Numero")
    return nro   
def validaCorreo():
   while True:
    correo=input("Ingresa Correo:")
    if len(correo)>=6:
       if '@' and '.' in correo:
          break 
       else:
        print("Correo debe tener @ y '.'")
    else:
       print("Correo debe tener mas de 6 caracteres")  
   return correo     
def validaFono(tipo,texto,ranMin=None,ranMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if ranMin!=None and ranMax!=None: 
                if ranMin<=nro<=ranMax:
                  break
                else:
                 print("Numero Invalido")
            elif ranMin!=None:
               if ranMin<=nro:
                  break
               else:
                  print("Numero con caracteres insuficientes")
            elif ranMax!=None:
               if ranMax>=nro:
                  break
               else:
                  print("Numero con demasiados caracteres")
            else:
               break
        except:
           print("Celular debe ser un Numero")
    return nro   
def Despedida():
   print("Adios,Espero que nos veamos pronto")
   print("Matias Gonzalez Pizarro") 
def validaEdad(añoNac,añoAct=None):
   añoNac=0
   while añoNac!=1:
     añoNac=int(input("Ingrese Año de nacimiento"))
     if añoNac>=1943:
        break
     elif añoAct!=None:
        break
     else:
        print("Edad no Apta para jugar")
   return añoNac
