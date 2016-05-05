# sacarFilas.py
# coding=utf8
# -----------------------
# Esta clase se encarga de devolver la fila de la tabla Q dados unos
# parametros de entrada


def sacarFila(north, south, east, west, bestMove, distanciaFantasma):
    fila = None
    if north == 0:
        if south == 0:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 0
                        elif distanciaFantasma == 2:
                            fila = 1
                        elif distanciaFantasma == 3:
                            fila = 2
                        else:
                            fila = 3
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 4
                        elif distanciaFantasma == 2:
                            fila = 5
                        elif distanciaFantasma == 3:
                            fila = 6
                        else:
                            fila = 7
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 8
                        elif distanciaFantasma == 2:
                            fila = 9
                        elif distanciaFantasma == 3:
                            fila = 10
                        else:
                            fila = 11
                    else:
                        if distanciaFantasma == 1:
                            fila = 12
                        elif distanciaFantasma == 2:
                            fila = 13
                        elif distanciaFantasma == 3:
                            fila = 14
                        else:
                            fila = 15
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 16
                        elif distanciaFantasma == 2:
                            fila = 17
                        elif distanciaFantasma == 3:
                            fila = 18
                        else:
                            fila = 19
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 20
                        elif distanciaFantasma == 2:
                            fila = 21
                        elif distanciaFantasma == 3:
                            fila = 22
                        else:
                            fila = 23
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 24
                        elif distanciaFantasma == 2:
                            fila = 25
                        elif distanciaFantasma == 3:
                            fila = 26
                        else:
                            fila = 27
                    else:
                        if distanciaFantasma == 1:
                            fila = 28
                        elif distanciaFantasma == 2:
                            fila = 29
                        elif distanciaFantasma == 3:
                            fila = 30
                        else:
                            fila = 31
            else:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 32
                        elif distanciaFantasma == 2:
                            fila = 33
                        elif distanciaFantasma == 3:
                            fila = 34
                        else:
                            fila = 35
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 36
                        elif distanciaFantasma == 2:
                            fila = 37
                        elif distanciaFantasma == 3:
                            fila = 38
                        else:
                            fila = 39
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 40
                        elif distanciaFantasma == 2:
                            fila = 41
                        elif distanciaFantasma == 3:
                            fila = 42
                        else:
                            fila = 43
                    else:
                        if distanciaFantasma == 1:
                            fila = 44
                        elif distanciaFantasma == 2:
                            fila = 45
                        elif distanciaFantasma == 3:
                            fila = 46
                        else:
                            fila = 47
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 48
                        elif distanciaFantasma == 2:
                            fila = 49
                        elif distanciaFantasma == 3:
                            fila = 50
                        else:
                            fila = 51
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 52
                        elif distanciaFantasma == 2:
                            fila = 53
                        elif distanciaFantasma == 3:
                            fila = 54
                        else:
                            fila = 55
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 56
                        elif distanciaFantasma == 2:
                            fila = 57
                        elif distanciaFantasma == 3:
                            fila = 58
                        else:
                            fila = 59
                    else:
                        if distanciaFantasma == 1:
                            fila = 60
                        elif distanciaFantasma == 2:
                            fila = 61
                        elif distanciaFantasma == 3:
                            fila = 62
                        else:
                            fila = 63
        else:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 64
                        elif distanciaFantasma == 2:
                            fila = 65
                        elif distanciaFantasma == 3:
                            fila = 66
                        else:
                            fila = 67
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 68
                        elif distanciaFantasma == 2:
                            fila = 69
                        elif distanciaFantasma == 3:
                            fila = 70
                        else:
                            fila = 71
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 72
                        elif distanciaFantasma == 2:
                            fila = 73
                        elif distanciaFantasma == 3:
                            fila = 74
                        else:
                            fila = 75
                    else:
                        if distanciaFantasma == 1:
                            fila = 76
                        elif distanciaFantasma == 2:
                            fila = 77
                        elif distanciaFantasma == 3:
                            fila = 78
                        else:
                            fila = 79
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 80
                        elif distanciaFantasma == 2:
                            fila = 81
                        elif distanciaFantasma == 3:
                            fila = 82
                        else:
                            fila = 83
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 84
                        elif distanciaFantasma == 2:
                            fila = 85
                        elif distanciaFantasma == 3:
                            fila = 86
                        else:
                            fila = 87
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 88
                        elif distanciaFantasma == 2:
                            fila = 89
                        elif distanciaFantasma == 3:
                            fila = 90
                        else:
                            fila = 91
                    else:
                        if distanciaFantasma == 1:
                            fila = 92
                        elif distanciaFantasma == 2:
                            fila = 93
                        elif distanciaFantasma == 3:
                            fila = 94
                        else:
                            fila = 95
            else:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 96
                        elif distanciaFantasma == 2:
                            fila = 97
                        elif distanciaFantasma == 3:
                            fila = 98
                        else:
                            fila = 99
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 100
                        elif distanciaFantasma == 2:
                            fila = 101
                        elif distanciaFantasma == 3:
                            fila = 102
                        else:
                            fila = 103
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 104
                        elif distanciaFantasma == 2:
                            fila = 105
                        elif distanciaFantasma == 3:
                            fila = 106
                        else:
                            fila = 107
                    else:
                        if distanciaFantasma == 1:
                            fila = 108
                        elif distanciaFantasma == 2:
                            fila = 109
                        elif distanciaFantasma == 3:
                            fila = 110
                        else:
                            fila = 111
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 112
                        elif distanciaFantasma == 2:
                            fila = 113
                        elif distanciaFantasma == 3:
                            fila = 114
                        else:
                            fila = 115
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 116
                        elif distanciaFantasma == 2:
                            fila = 117
                        elif distanciaFantasma == 3:
                            fila = 118
                        else:
                            fila = 119
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 120
                        elif distanciaFantasma == 2:
                            fila = 121
                        elif distanciaFantasma == 3:
                            fila = 122
                        else:
                            fila = 123
                    else:
                        if distanciaFantasma == 1:
                            fila = 124
                        elif distanciaFantasma == 2:
                            fila = 125
                        elif distanciaFantasma == 3:
                            fila = 126
                        else:
                            fila = 127
    else:
        if south == 0:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 128
                        elif distanciaFantasma == 2:
                            fila = 129
                        elif distanciaFantasma == 3:
                            fila = 130
                        else:
                            fila = 131
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 132
                        elif distanciaFantasma == 2:
                            fila = 133
                        elif distanciaFantasma == 3:
                            fila = 134
                        else:
                            fila = 135
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 136
                        elif distanciaFantasma == 2:
                            fila = 137
                        elif distanciaFantasma == 3:
                            fila = 138
                        else:
                            fila = 139
                    else:
                        if distanciaFantasma == 1:
                            fila = 140
                        elif distanciaFantasma == 2:
                            fila = 141
                        elif distanciaFantasma == 3:
                            fila = 142
                        else:
                            fila = 143
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 144
                        elif distanciaFantasma == 2:
                            fila = 145
                        elif distanciaFantasma == 3:
                            fila = 146
                        else:
                            fila = 147
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 148
                        elif distanciaFantasma == 2:
                            fila = 149
                        elif distanciaFantasma == 3:
                            fila = 150
                        else:
                            fila = 151
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 152
                        elif distanciaFantasma == 2:
                            fila = 153
                        elif distanciaFantasma == 3:
                            fila = 154
                        else:
                            fila = 155
                    else:
                        if distanciaFantasma == 1:
                            fila = 156
                        elif distanciaFantasma == 2:
                            fila = 157
                        elif distanciaFantasma == 3:
                            fila = 158
                        else:
                            fila = 159
            else:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 160
                        elif distanciaFantasma == 2:
                            fila = 161
                        elif distanciaFantasma == 3:
                            fila = 162
                        else:
                            fila = 163
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 164
                        elif distanciaFantasma == 2:
                            fila = 165
                        elif distanciaFantasma == 3:
                            fila = 166
                        else:
                            fila = 167
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 168
                        elif distanciaFantasma == 2:
                            fila = 169
                        elif distanciaFantasma == 3:
                            fila = 170
                        else:
                            fila = 171
                    else:
                        if distanciaFantasma == 1:
                            fila = 172
                        elif distanciaFantasma == 2:
                            fila = 173
                        elif distanciaFantasma == 3:
                            fila = 174
                        else:
                            fila = 175
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 176
                        elif distanciaFantasma == 2:
                            fila = 177
                        elif distanciaFantasma == 3:
                            fila = 178
                        else:
                            fila = 179
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 180
                        elif distanciaFantasma == 2:
                            fila = 181
                        elif distanciaFantasma == 3:
                            fila = 182
                        else:
                            fila = 183
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 184
                        elif distanciaFantasma == 2:
                            fila = 185
                        elif distanciaFantasma == 3:
                            fila = 186
                        else:
                            fila = 187
                    else:
                        if distanciaFantasma == 1:
                            fila = 188
                        elif distanciaFantasma == 2:
                            fila = 189
                        elif distanciaFantasma == 3:
                            fila = 190
                        else:
                            fila = 191
        else:
            if east == 0:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 192
                        elif distanciaFantasma == 2:
                            fila = 193
                        elif distanciaFantasma == 3:
                            fila = 194
                        else:
                            fila = 195
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 196
                        elif distanciaFantasma == 2:
                            fila = 197
                        elif distanciaFantasma == 3:
                            fila = 198
                        else:
                            fila = 199
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 200
                        elif distanciaFantasma == 2:
                            fila = 201
                        elif distanciaFantasma == 3:
                            fila = 202
                        else:
                            fila = 203
                    else:
                        if distanciaFantasma == 1:
                            fila = 204
                        elif distanciaFantasma == 2:
                            fila = 205
                        elif distanciaFantasma == 3:
                            fila = 206
                        else:
                            fila = 207
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 208
                        elif distanciaFantasma == 2:
                            fila = 209
                        elif distanciaFantasma == 3:
                            fila = 210
                        else:
                            fila = 211
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 212
                        elif distanciaFantasma == 2:
                            fila = 213
                        elif distanciaFantasma == 3:
                            fila = 214
                        else:
                            fila = 215
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 216
                        elif distanciaFantasma == 2:
                            fila = 217
                        elif distanciaFantasma == 3:
                            fila = 218
                        else:
                            fila = 219
                    else:
                        if distanciaFantasma == 1:
                            fila = 220
                        elif distanciaFantasma == 2:
                            fila = 221
                        elif distanciaFantasma == 3:
                            fila = 222
                        else:
                            fila = 223
            else:
                if west == 0:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 224
                        elif distanciaFantasma == 2:
                            fila = 225
                        elif distanciaFantasma == 3:
                            fila = 226
                        else:
                            fila = 227
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 228
                        elif distanciaFantasma == 2:
                            fila = 229
                        elif distanciaFantasma == 3:
                            fila = 230
                        else:
                            fila = 231
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 232
                        elif distanciaFantasma == 2:
                            fila = 233
                        elif distanciaFantasma == 3:
                            fila = 234
                        else:
                            fila = 235
                    else:
                        if distanciaFantasma == 1:
                            fila = 236
                        elif distanciaFantasma == 2:
                            fila = 237
                        elif distanciaFantasma == 3:
                            fila = 238
                        else:
                            fila = 239
                else:
                    if bestMove == 'North':
                        if distanciaFantasma == 1:
                            fila = 240
                        elif distanciaFantasma == 2:
                            fila = 241
                        elif distanciaFantasma == 3:
                            fila = 242
                        else:
                            fila = 243
                    elif bestMove == 'South':
                        if distanciaFantasma == 1:
                            fila = 244
                        elif distanciaFantasma == 2:
                            fila = 245
                        elif distanciaFantasma == 3:
                            fila = 246
                        else:
                            fila = 247
                    elif bestMove == 'East':
                        if distanciaFantasma == 1:
                            fila = 248
                        elif distanciaFantasma == 2:
                            fila = 249
                        elif distanciaFantasma == 3:
                            fila = 250
                        else:
                            fila = 251
                    else:
                        if distanciaFantasma == 1:
                            fila = 252
                        elif distanciaFantasma == 2:
                            fila = 253
                        elif distanciaFantasma == 3:
                            fila = 254
                        else:
                            fila = 255
    return fila
