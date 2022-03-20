orientation = ["N", "S", "E", "O"]
x_axis = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
dimensiones = (10, 10)
list_eslora_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
message_instructions =("1. Al empezar el juego, deberá ingresar un nombre o ID que lo identifique. \n"
                                "2. Ingrese el nivel de la máquina (mayor a cero,0). La máquina tendrá por turno tantos disparos como se habría indicado; nivel 1 es normal, es decir, un disparo por turno, y solamente tendrá un disparo adicional si la máquina acierta . \n"
                                "3. El sistema escoge aleatoriamente quien empieza el juego, la máquina o el jugador\n"
                                "4. Cuando el turno sea del jugador, tendrá que ingresar la coordenada en el eje X o columna, de acuerdo al orden alfabético, de la A, B, C.. hasta la I\n"
                                "5. Después  deberá ingresar la coordenada en el eje Y o fila, del 1 al 10\n"
                                "6. Tendra notificacón si acierta en la coordenada donde se encuentra un barco del adversario. Y por lo tanto, tendrá un disparo adicional.\n"
                                "7. El primero que hunda todos los barcos será el vencedor.\n"
                                "* La asignación de los barcos en el tablero y los disparos de la máquina se ejecutan de manera aleatoriamente. Por otro lado, en la pantalla habrán dos tableros para el jugador, el de la izquierda se trata de la ubicación de los barcos (donde estarán los disparos de la máquina), y el de la derecha es de los disparos contra la máquina.\n" 
                                "** Si el jugador ingresa un nivel mayor a 1, la máquna si acierta dentro de ese número de disparos por turno, esta no tendrá uno adicional.\n"
                                "*** Durante el juego aparecerán varias ventanas emergentes con información acerca si realizaste un impacto o no, o si la máquina te impacto. Para dar continuidad al juego, solamente de clic sobre el botón aceptar, OK o con la tecla Enter.\n"
                                "**** En el tablero se encontrará con los siguientes símbolos:\n"
                                "\t- Posición Agua --> ≈\n" 
                                "\t- Posición Barco --> █\n" 
                                "\t- Posición Disparo acertado --> X\n"
                                "\t- Posición Disparo no acertado --> •\n"
                                "\nPor último, son 10 barcos los que tiene usted como jugador y otros 10 para la máquina, estos son:\n"
                                "\t- 4 barcos de 1 posición de eslora\n"
                                "\t- 3 barcos de 2 posición de eslora\n"
                                "\t- 2 barcos de 3 posición de eslora\n"
                                "\t- 1 barcos de 4 posición de eslora\n")
   

