import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
import questionary

Historial = InMemoryHistory()

def Menu_principal():
    print('|================================================|')
    print(' ***********Bienvenido a ModernClothes***********')
    print('|================================================|')
    print('       ¿Quieres acceder al catalogo Online?       ')
    print('|================================================|')
    time.sleep(0.3)
    
    Confirmacion = questionary.select(
        "",
        choices=["Si", "No"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    os.system('clear')
    return Confirmacion
    

def Menu_catalogo():
    print('|================================================|')
    print('***********Bienvenido al catalogo Online***********')
    print('|================================================|')
    time.sleep(0.3)
    Prendas = questionary.select(
        'Eliga que tipo de prenda desea:',
        choices=["1 - Camisas/Camisetas", "2 - Shorts/Pantalones", "3 - ***(Salir del Sistema)***"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    os.system('clear')
    return Prendas
    

def Menu_camisas(Camisa, Factura):
    print('|================================================|')
    print(' Eliga que tipo de Camisa/Camiseta desea: ')
    print('|================================================|')
    time.sleep(0.3)
    Camisa = questionary.select(
        "",
        choices=["1.- Tank Top........3.00$", "2.- T_Shirt.........5.00$", "3.- Polo Shirt......7.00$", "4.- Dress Shirt....10.00$", "5.- Jacket.........15.00$", "6.**(Volver al Menu Principal)**"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    os.system('clear')
    if Camisa == "1.- Tank Top........3.00$":
        Camisa = "Tank Top"
        Factura += 3
    elif Camisa == "2.- T_Shirt.........5.00$":
        Camisa = "T_Shirt"
        Factura += 5
    elif Camisa == "3.- Polo Shirt......7.00$":
        Camisa = "Polo Shirt"
        Factura += 7
    elif Camisa == "4.- Dress Shirt....10.00$":
        Camisa = "Dress Shirt"
        Factura += 10
    elif Camisa == "5.- Jacket.........15.00$":
        Camisa = "Jacket"
        Factura += 15
    elif Camisa == "6.**(Volver al Menu Principal)**":
        Camisa = None
    return Camisa, Factura


def Menu_pantalones(Shorts, Factura):
    print('|================================================|')
    print(' Eliga que tipo de Shorts/Pantalones desea: ')
    print('|================================================|')
    time.sleep(0.3)
    Shorts = questionary.select(
        "",
        choices=["1.- Bermuda Short...3.00$", "2.- Running Short...5.00$", "3.- Cargo Short....10.00$", "4.- Denim Short....15.00$", "5.- Baggy Short....20.00$", "6.**(Volver al Menu Principal)**"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    os.system('clear')
    if Shorts == "1.- Bermuda Short...3.00$":
        Shorts = "Bermuda Short"
        Factura += 3
    elif Shorts == "2.- Running Short...5.00$":
        Shorts = "Running Short"
        Factura += 5
    elif Shorts == "3.- Cargo Short....10.00$":
        Shorts = "Cargo Short"
        Factura += 10
    elif Shorts == "4.- Denim Short....15.00$":
        Shorts = "Denim Short"
        Factura += 15
    elif Shorts == "5.- Baggy Short....20.00$":
        Shorts = "Baggy Short"
        Factura += 20
    elif Shorts == "6.**(Volver al Menu Principal)**":
        Shorts = None
    return Shorts, Factura
    

def Menu_salir():
    print('|================================================|')
    print('**********Sus operaciones han finalizado********* ')
    print('**************Gracias por Visitarnos*************')
    print('|================================================|')
    time.sleep(3)


def Menu_Camisa_Seleccionada(Camisa, Factura):
    
    print('|**********************************************************************|')
    print(f' - Has Agregado {Camisa} al Carrito, Su Factura es: {Factura}$')
    print(' - Deseas añadir mas productos a tu carrito: ')
    time.sleep(0.3)
    Añadir = questionary.select(
        "",
        choices=["Si", "No"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)",
    ).ask()
    print('|**********************************************************************|')
    return Añadir


def Menu_Pantalon_Seleccionado(Shorts, Factura):
    
    print('|**********************************************************************|')
    print(f' - Has Agregado {Shorts} al Carrito, Su Factura es: {Factura}$')
    print(' - Deseas añadir mas productos a tu carrito: ')
    time.sleep(0.3)
    Añadir = questionary.select(
        "",
        choices=["Si", "No"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    print('|**********************************************************************|')
    return Añadir


def Menu_Factura(Factura):
    os.system('clear')
    print('|================================================|')
    print(' *************Su factura es de:****************** ')
    time.sleep(0.3)
    print(f'****************** {Factura}.00$ ****************')
    print('|================================================|')
    time.sleep(0.5)
    Continuar = questionary.select(
        "¿Desea completar la compra?:",
        choices=["Si", "No"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    print('|**********************************************************************|')
    return Continuar


def Completar_compra():
    while True:
        os.system('clear')
        print( '|==================================================|')
        print('Perfecto Ingrese los siguientes datos para confirmar:')
        print('|===================================================|')
        time.sleep(0.3)
        print('|***************************************************|')
        print('1.Nombre Completo:')
        Nombre = prompt(history=Historial)
        print('|***************************************************|')  
        print('2.Numero de Celular:')
        NummCell = prompt(history=Historial)
        print('|***************************************************|')
        print('3.Direccion de Envio:')
        DirecEnvio = prompt(history=Historial)
        time.sleep(0.7)
        os.system('clear')
        print('|===================================================|')
        print('Verifique si los siguientes datos son Correctos:')
        print(f'Nombre: {Nombre}')
        time.sleep(0.3)
        print(f'Numero de Celular: {NummCell}')
        time.sleep(0.3)
        print(f'Direccion: {DirecEnvio}')
        print('|===================================================|')
        print('Si cometio algun tipo de error al ingresar los datos puede cambiarlo ahora.')
        print('¿Desea modificar la informacion ingresada?:')
        print('|===================================================|')
        ConfDatos = questionary.select(
            "",
            choices=["Si", "No"],
            instruction="(Use ↑↓ para seleccionar y presione Enter)"
        ).ask()
        if ConfDatos == "Si":
            continue
        elif ConfDatos == "No":
            os.system('clear')
            time.sleep(0.3)
            print('|===========================================================================|')
            print(f'Perfecto, {Nombre} su pedido llegara en un plazo de:')
            print(' - 3 a 5 dias habiles, a su direccion:', DirecEnvio)
            print('Cualquier notificacion o inconveniente se le comunicara a su numero:', NummCell)
            print('|===========================================================================|')
            time.sleep(0.3)
            print('Presione Enter para finalizar su compra y salir del sistema...')
            input()
            break

def Reinicio_del_Carrito(Factura):
    os.system('clear')
    time.sleep(0.3)
    print('|===================================================|')
    print('Desea vaciar su carrito y volver al menu principal:')
    print('|===================================================|')
    Respuesta = questionary.select(
        "",
        choices=["Si", "No"],
        instruction="(Use ↑↓ para seleccionar y presione Enter)"
    ).ask()
    if Respuesta == "Si":
        Factura = 0
    return Respuesta, Factura
    

    
	
