#Importes
import os
import time
import json

ruta_archivo = "biblioteca.json"

#FUNCIONES
def abrir_archivo(ruta_json):
    with open(ruta_json, "r") as f:
        leer_json = json.load(f)
    return leer_json

v_abrir_archivo = abrir_archivo(ruta_archivo)

def guardar_archivo(guardar_datos, ruta_json):
    with open(ruta_json, "w") as f:
        json.dump(guardar_datos, ruta_json, indent= 4)

def encontrar_ultimo_id(ruta_json):
    lista_datos = ruta_json["Autor"]
    lista_ids = []
    for dato in lista_datos:
        lista_ids.append(dato["AutorID"])
    return max(lista_ids)


def validar_agregar_autor(nombre):
    lista_autores = v_abrir_archivo["Autor"]
    autor_existente = True

    for i in lista_autores:
        if i["Nombre"] == nombre:
            autor_existente = False
            return autor_existente
    
    return autor_existente

#Agregar Autor
def agregar_autor(archivo):
 while True:  
    #solicitar Datos
    nombre_autor = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")

    if not validar_agregar_autor(nombre_autor):
        print("Nombre ya existente, intente nuevamente")
    else:
        break

    autor_dict = {
        "AutorID": encontrar_ultimo_id(archivo) +1,
        "Nombre": nombre_autor,
        "Nacionalidad": nacionalidad
    }

    archivo["Autor"].append(autor_dict) 
    guardar_archivo(v_abrir_archivo, ruta_archivo)

 
def buscar_autor(archivo):
    lista_autores = archivo["Autor"]

    for i in lista_autores:
        print(i)
        

def aux_editar_autor(archivo):
   while True: 
    lista_autores = archivo["Autor"]
    autor_encontrado = False

    buscar = int(input("Ingrese el ID del Autor a modificar: "))

    for dato in lista_autores:
        if dato["AutorID"] == buscar:
            print("Autor Encontrado")
            autor_encontrado = True
            return dato
    
    if autor_encontrado:
        break
    else:
        print("Error al encontrar al autor, intente nuevamente")


def editar_autor(archivo):
    lista_autores = aux_editar_autor(archivo)

    nombre_autor_new = input("Ingrese el nuevo nombre del autor: ")
    nacionalidad_new = input("Ingrese la nueva nacionalidad el autor: ")

    lista_autores["Nombre"] = nombre_autor_new
    lista_autores["Nacionalidad"] = nacionalidad_new
    guardar_archivo(v_abrir_archivo, ruta_archivo)


def eliminar_autor():
    while True:
        lista_autores = v_abrir_archivo["Autor"]
        autor_del = int(input("Ingrese el id del autor a eliminar"))

        for i in lista_autores:
            if i["AutorID"] == autor_del:
                lista_autores.remove(i)
                print("El autor ha sido encontrado y eliminado correctamente")
                break
            else:
                print("Autor no encontrado, intente nuevamente")
        
        guardar_archivo(v_abrir_archivo, ruta_archivo)


print("***********************")
print("*     MUNDO LIBRO     *")
print("***********************")

print("[1] Mantenedor de autores")
print("[2] Reportes")
print("[3] Salir")

while True:
    try:
        opc = int(input("Seleccione una opcion: "))
        os.system("cls")
        break
    except:
        print("Error, intente nuevamente")

match opc:
    case 1:
            while True:
                print("***********************")
                print("*     MUNDO LIBRO     *")
                print("***********************")

                print("[1] Agregar Autor")
                print("[2] Editar autor")
                print("[3] Eliminar autor")
                print("[4] Buscar autor")
                print("[5] Volver")

                while True:
                    try:
                        sub_opc = int(input("Seleccione una opcion: "))
                        os.system("cls")
                        break
                    except:
                        print("Error, intente nuevamente")

                match sub_opc:
                    case 1:
                        agregar_autor(v_abrir_archivo)
                        input("presiona una telca para continuar..")
                        os.system("cls")
                    case 2:
                        editar_autor(v_abrir_archivo)
                        input("presiona una telca para continuar..")
                        os.system("cls")
                    case 3:
                        eliminar_autor()
                        input("presiona una telca para continuar..")
                        os.system("cls")
                    case 4:
                        buscar_autor(v_abrir_archivo)
                        input("presiona una telca para continuar..")
                        os.system("cls")
                    case 5:
                        break
    case 2:
            pass
    case 3:
        pass



