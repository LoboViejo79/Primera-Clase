import datetime

def verificar_mayoria_edad():
    try:
        anio_nac = int(input("Imgresa tu año de nacimiento: "))
        anio_actual = datetime.datetime.now().year
        edad = anio_actual - anio_nac

        if edad >= 18:
            print("Usted es mayor de edad.")
        else:
            print("Usted es menor de edad.")
    except ValueError:
            print("Ingrese un año valido.")

verificar_mayoria_edad()