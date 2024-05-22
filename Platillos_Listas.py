#ejercicio de lista
list_platos=[]
def agregar_platos():
    Nombre_plato = input ("ingrese el plato: ")
    precio_plato = float(input ("ingrese el precio: "))
    categoria_plato = input ("ingrese la categoria: ")
    Listado_ingredientes = []
    for ing in range(5):    
        ingrediente = input ("ingrese el ingrediente: ")    
        Listado_ingredientes.append(ingrediente)
        break
    list_platos.append([Nombre_plato,precio_plato,categoria_plato,Listado_ingredientes])
    print (list_platos)

agregar_platos()
print (list_platos)

def mostar_menu():
    print (" 1 - agregar platos")
    print (" 2 - mostrar platos")
    print (" 3 - buscar platos")
    print (" 4 - modificar platos")
    print (" 5 - eliminar platos")
    print (" 6 - salir")

def buscar_platos():
    plato=input("ingrese el plato que desea buscar: ")
    for i in list_platos:
        if plato==i[0]:
            print(i)
            break
        else:
            print("el plato no existe")

def modificar_platos():
    plato=input("ingrese el plato que desea modificar: ")
    for i in list_platos:
        if plato==i[0]:
            print(i)
            break
        else:
            print("el plato no existe")

def eliminar_platos():
    plato=input("ingrese el plato que desea eliminar: ")
    for i in list_platos:
        if plato==i[0]:
            print(i)
            break
        else:
            print("el plato no existe")




lista_platos=[]

while True:
    mostar_menu()
    op=int(input("ingrese la opcion: "))
    if op==1:
        agregar_platos()
    elif op==2:
        print (list_platos)
    elif op==3:
        buscar_platos()
    elif op==4:
        modificar_platos()
    elif op==5:
        eliminar_platos()
    elif op==6:
        break
    else:
        print ("ingrese una opcion correcta")
