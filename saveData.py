# saveDate.py
# coding=utf8
# -------
# Esta clase es la encargada de guardar en un archivo txt los datos del turno
# de la partida


def saveData(datos, accion, refuerzo):

    """ Aqui guardamos en el archivo """
    fich = 'datosP3.txt'

    if len(datos) == 2:
            data = ""
            data = data + str(datos[0]) + ',' + accion + ',' +\
                str(datos[1]) + ',' + str(refuerzo)
            outfile = open(fich, 'a')
            outfile.write(data + '\n')
            outfile.close()
