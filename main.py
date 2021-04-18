from nodo import Nodo
from lista_doblemente_enlazada import Lista_Doblemente_Enlazada
lista_contactos=Lista_Doblemente_Enlazada()

def menu_principal():
    while True:
        print('\t1). Ingresar nuevo contacto')
        print('\t2). Buscar Contacto')
        print('\t3). Visualizar agenda')
        op=int(input('Ingrese opción: '))
        print('\n')
        if op==1:
            print('\n----------------------Ingresar nuevo contacto-----------------')
            nombre=input('\tIngrese nombre: ')
            apellido=input('\tIngrese apellido: ')
            tel=input('\tIngrese número de teléfono: ')
            lista_contactos.insertar(str(nombre),str(apellido),str(tel))
            print('\n')
        if op==2:
            print('\n--------------Buscar contacto--------------')
            buscar=input('\tIngrese número de teléfono: ')
            lista_contactos.buscar(buscar)
            print('\n')
        if op==3:
            lista_contactos.generar_grafoContactos()
            print('\n')
if __name__=='__main__':
    menu_principal()
