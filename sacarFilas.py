# sacarFilas.py
# coding=utf8
# -----------------------
# Esta clase se encarga de devolver la fila de la tabla Q dados unos
# parametros de entrada


def sacarFila(north, south, east, west, bestMove):
    fila = None
    if north == 0:
        if south == 0:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        fila = 0
                    elif bestMove == 'South':
                        fila = 1
                    elif bestMove == 'East':
                        fila = 2
                    else:
                        fila = 3
                else:
                    if bestMove == 'North':
                        fila = 4
                    elif bestMove == 'South':
                        fila = 5
                    elif bestMove == 'East':
                        fila = 6
                    else:
                        fila = 7
            else:
                if west == 0:
                    if bestMove == 'North':
                        fila = 8
                    elif bestMove == 'South':
                        fila = 9
                    elif bestMove == 'East':
                        fila = 10
                    else:
                        fila = 11
                else:
                    if bestMove == 'North':
                        fila = 12
                    elif bestMove == 'South':
                        fila = 13
                    elif bestMove == 'East':
                        fila = 14
                    else:
                        fila = 15
        else:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        fila = 16
                    elif bestMove == 'South':
                        fila = 17
                    elif bestMove == 'East':
                        fila = 18
                    else:
                        fila = 19
                else:
                    if bestMove == 'North':
                        fila = 20
                    elif bestMove == 'South':
                        fila = 21
                    elif bestMove == 'East':
                        fila = 22
                    else:
                        fila = 23
            else:
                if west == 0:
                    if bestMove == 'North':
                        fila = 24
                    elif bestMove == 'South':
                        fila = 25
                    elif bestMove == 'East':
                        fila = 26
                    else:
                        fila = 27
                else:
                    if bestMove == 'North':
                        fila = 28
                    elif bestMove == 'South':
                        fila = 29
                    elif bestMove == 'East':
                        fila = 30
                    else:
                        fila = 31
    else:
        if south == 0:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        fila = 32
                    elif bestMove == 'South':
                        fila = 33
                    elif bestMove == 'East':
                        fila = 34
                    else:
                        fila = 35
                else:
                    if bestMove == 'North':
                        fila = 36
                    elif bestMove == 'South':
                        fila = 37
                    elif bestMove == 'East':
                        fila = 38
                    else:
                        fila = 39
            else:
                if west == 0:
                    if bestMove == 'North':
                        fila = 40
                    elif bestMove == 'South':
                        fila = 41
                    elif bestMove == 'East':
                        fila = 42
                    else:
                        fila = 43
                else:
                    if bestMove == 'North':
                        fila = 44
                    elif bestMove == 'South':
                        fila = 45
                    elif bestMove == 'East':
                        fila = 46
                    else:
                        fila = 47
        else:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        fila = 48
                    elif bestMove == 'South':
                        fila = 49
                    elif bestMove == 'East':
                        fila = 50
                    else:
                        fila = 51
                else:
                    if bestMove == 'North':
                        fila = 52
                    elif bestMove == 'South':
                        fila = 53
                    elif bestMove == 'East':
                        fila = 54
                    else:
                        fila = 55
            else:
                if west == 0:
                    if bestMove == 'North':
                        fila = 56
                    elif bestMove == 'South':
                        fila = 57
                    elif bestMove == 'East':
                        fila = 58
                    else:
                        fila = 59
                else:
                    if bestMove == 'North':
                        fila = 60
                    elif bestMove == 'South':
                        fila = 61
                    elif bestMove == 'East':
                        fila = 62
                    else:
                        fila = 63

    return fila
