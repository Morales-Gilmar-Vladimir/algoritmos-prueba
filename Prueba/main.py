from os import system
import random
detalleCompra =[[],[],[],[],[],[],[],[]]


def menuOpciones():
  print("¿Que acción desea realizar?")
  print(f'*  1) Registrar pedidos')
  print(f'*  2) Mostrar pedidos')
  print(f'*  3) Mostrar detalle de un pedido')
  print(f'*  4) Salir del sistema')
  tipoAccion=int(input("Ingrese la opción: "))
  return tipoAccion


def ingresarPedido():
  print("\n\t\t Ingresar los datos del cliente \n")
  nombre_cliente=input("Nombre: ")
  apellido_cliente=input("Apellido: ")
  telefono_cliente=input("Teléfono: ")
  print("\n\t\t Ingresar los datos de la policrush\n")
  nombre_policrush=input("Nombre: ")
  lugar_policrush=input("Dependencia: ")
  celular_policrush=input("Teléfono: ")
  detalleCompra[0].append(nombre_cliente)
  detalleCompra[1].append(apellido_cliente)
  detalleCompra[2].append(telefono_cliente)
  detalleCompra[3].append(nombre_policrush)
  detalleCompra[4].append(lugar_policrush)
  detalleCompra[5].append(celular_policrush)
  detalleCompra[6].append(random.randrange(1000, 9999))

  print("\n\t\t Selección del regalo \n")
  print("1) Opción 1: Poliflor + Polipeluche = $2.50")
  print("2) Opción 2: Poliflor + Policarta = $1.50")
  print("3) Opción 3: Poliflor + Polillavero = $2.00")
  print("4) Opción 4: Poliflor + Polivaso = $2.75")
  opcion= int(input("Ingrese la opción: "))
  if opcion==1:
    detalleCompra[7].append(2.50+(0.1*2.50))
  elif opcion==2:
    detalleCompra[7].append(1.50+(0.1*1.50))
  elif opcion==3:
    detalleCompra[7].append(2.00+(0.1*2.00))
  elif opcion==4:
    detalleCompra[7].append(2.75+(0.1*2.75))
    
  print("\n-------- Pedido registrado con éxito --------\n") 



def mostrarPedido(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompra[0][i])
    print("\t\t\t * Apellido:", detalleCompra[1][i])
    print("\t\t\t * Teléfono:", detalleCompra[2][i])
    print("\t\t\n Datos de la entrega")
    print("\t\t\t * Nombre:", detalleCompra[3][i])
    print("\t\t\t * Dependencia:", detalleCompra[4][i])
    print("\t\t\t * Teléfono:", detalleCompra[5][i])
    print("\t\t\n Datos del pago")
    print("\t\t\t * Código del pedido:", detalleCompra[6][i])      
    print("\t\t\t * Pago final: $", detalleCompra[7][i])






print("------------ MI POLICRUSH -------------")
print("\n\t\t *** Bienvenido(a) ***\n")
opcion= menuOpciones()
while opcion !=4:
  
  if opcion==1:
    system("clear")
    print("\n----- Nuevo pedido -----")
    ingresarPedido()
    opcion= menuOpciones()
  
  elif opcion==2:
    system("clear")
    print("\n------- Detalle de todos los pedidos ----------\n")
    for i in range(len(detalleCompra[0])):
      print("-------------------------------------")
      print("Detalle del pedido", i + 1)
      mostrarPedido(i)
      print("-------------------------------------")
    opcion= menuOpciones()  

  elif opcion==3:
    system("clear")
    codigo=int(input("\n Ingrese el código del pedido: "))
    try:
      dato= detalleCompra[6].index(codigo)
      for i in range(len(detalleCompra[0])):
        if i==dato:
          print("\t\t\t\n Pedido encontrado")
          print("-------------------------------------")
          print("Detalle")
          mostrarPedido(i)
          print("-------------------------------------")
    except:
      print("\n\n ******* ERROR *****\n")
      print("No existe ese código de pedido registrado\n")

    opcion= menuOpciones()

print("Muchas gracias")