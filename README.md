Un agente automático que se apoya en el Q learning para que PacMan se coma a los fantasmas.

    python busters.py --help

Los principales argumentos que se pueden cambiar son:

* `\-n GAMES` Número de juegos. Por defecto es 1.
* `\-l LAYOUT FILE` El tablero del juego. Por defecto es oneHunt.
* `\-p TYPE` El tipo de agente Pac-Man. Por defecto es BustersKeyboardAgent (control por teclado).
* `\-g TYPE` El tipo de agente de fantasma. Por defecto es RandomGhost (se mueve aleatoriamente).
* `\-k NUMGHOSTS` El número máximo de fantasmas. El valor por defecto es 4. Todos los mapas predefinidos permiten de 1 hasta 4 fantasmas.
* `\-s` Dibuja los fantasmas en el mapa (solo para debug)
