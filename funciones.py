import random as rd
from tkinter import messagebox
import time
import easygui
import sys

from clases import Tablero, Barco
from variables import x_axis, dimensiones, list_eslora_ships, message_instructions

def disparos_player(tableros_player, tableros_maquina):
    """
    Ubica los disparos del jugador
    INPUT : tableros_player (Objeto Clase Tablero)
            tableros_maquina (Objeto Clase Tablero)
    OUTPUT: messagebox.showinfo (str) informando al jugador si acierta o no, y por último si hunde todos los barcos de la máquina
    """
    while True:
        time.sleep(1) 
        counts_o_player = tableros_player.matriz_shooting == "X"
        if counts_o_player.sum() == 20: #Condición para la suma de los disparos acertados "X" del jugador
            print(f"Player: {tableros_player.idplayer}. YOU WIN!")  
            messagebox.showinfo(message=f"Player: {tableros_player.idplayer}. YOU WIN!" , title="YOU WIN!")
            mostrar_tableros_player(tableros_player.idplayer, tableros_player.matriz_ships, tableros_player.matriz_shooting)
            mostrar_tableros_machine(tableros_maquina.idplayer, tableros_maquina.matriz_ships, tableros_maquina.matriz_shooting)
            return True   
                
        input_arrow = easygui.enterbox("Ingrese la coordenada en Y (vertical) o la fila; un número entre el 1 al 10")
        input_column_a = easygui.enterbox("Ingrese la coordenada en X (horizontal) o la columna; una letra de orden alfabético de la A a J")
        
        if input_arrow in ["", " ", None] or input_column_a in ["", " ", None]: #Verifica que no hayan especios varios y valores tipo None
            print("Input inválido. Ingrese de nuevo.")
            continue

        input_column = input_column_a.upper()

        if input_arrow not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] or input_column not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
            print("Input inválido. Por favor ingrese otra coordenada (x & y).") #Verifica que no hayan valores fuera de los rangos del tablero
            continue
        elif tableros_player.matriz_shooting[int(input_arrow) - 1, x_axis[input_column]] == "•" or tableros_player.matriz_shooting[int(input_arrow) - 1, x_axis[input_column]] == "X":
            print("Ya escogiste esta coordenada anteriormente. Por favor ingrese otra coordenada (en X y Y).") #Verifica que las coordenadas no se hayan escogido anteriormente
            continue                
        else:#Ubica los disparos del jugador en el metodo 'disparos_player' de la Clase Tablero
            hit_miss_player = tableros_player.disparos_player(int(input_arrow) - 1, x_axis[input_column], tableros_maquina)               
        
        if hit_miss_player == True: #Diparo (Acierto)
            print(f"Player: {tableros_player.idplayer}. YOU HIT!. Ubicación: ({(input_arrow)}, {input_column})") 
            messagebox.showinfo(message=f"Player: {tableros_player.idplayer}. YOU HIT!. Ubicación: ({(input_arrow)}, {input_column}). Tienes otro disparo."  , title="HIT!")
            mostrar_tableros_player(tableros_player.idplayer, tableros_player.matriz_ships, tableros_player.matriz_shooting)
            continue
        else: #No disparo (Agua)
            print(f"Player: {tableros_player.idplayer}. YOU MISS!. Ubicación: ({(input_arrow)}, {input_column})")  
            messagebox.showinfo(message =f"Player: {tableros_player.idplayer}. YOU MISS!. Ubicación: ({(input_arrow)}, {input_column}). Ahora, es turno de la máquina.", title="MISS!")  
            break
    

def disparos_machine(tableros_maquina, tableros_player):
    """
    Ubica los disparos de la maquina con nivel 1 (normal)
    INPUT : tableros_player (Objeto Clase Tablero)
            tableros_maquina (Objeto Clase Tablero)
    OUTPUT: messagebox.showinfo (str) informando al jugador si acierta o no la máquina, y por último si esta hunde todos los barcos del jugador
    """
    x_axis_inv = dict([(v,k) for k, v in x_axis.items()])       
    while True:
        counts_o_machine = tableros_maquina.matriz_shooting == "X"
        if counts_o_machine.sum() == 20: #Condición para la suma de los disparos acertados "X" de máquina
            print(f"Player: {tableros_player.idplayer}. YOU LOSE!\nPlayer: {tableros_maquina.idplayer} WINS")  
            messagebox.showinfo(message=f"Player: {tableros_player.idplayer}. YOU LOSE!\nPlayer: {tableros_maquina.idplayer} WINS"  , title="GAME OVER")
            mostrar_tableros_player(tableros_player.idplayer, tableros_player.matriz_ships, tableros_player.matriz_shooting)
            mostrar_tableros_machine(tableros_maquina.idplayer, tableros_maquina.matriz_ships, tableros_maquina.matriz_shooting)
            return True

        machine_row = rd.randint(0, 9)
        machine_column = rd.randint(0, 9)          
        #Verifica que la máquina no vuelva a repetir el disparo
        if tableros_maquina.matriz_shooting[machine_row, machine_column] == "•" or tableros_maquina.matriz_shooting[machine_row, machine_column] == "X":
            continue                
        else: #Ubica los disparos de la máquina en el metodo 'disparos_maquina' de la Clase Tablero
            hit_miss_machine = tableros_maquina.disparos_machine(machine_row, machine_column, tableros_player) 

        if hit_miss_machine == True: #Diparo (Acierto)
            print(f"Player: {tableros_maquina.idplayer}. HIT!. Ubicación: ({(machine_row + 1)}, {x_axis_inv[machine_column]})")    
            messagebox.showinfo(message = f"Player: {tableros_maquina.idplayer}. HIT!. Ubicación: ({(machine_row + 1)}, {x_axis_inv[machine_column]})", title="MACHINE HITS!")
            continue
        else: #No Disparo (Agua)
            print(f"Player: {tableros_maquina.idplayer}. MISS!. Ubicación: ({(machine_row + 1)}, {x_axis_inv[machine_column]})") 
            break    

def disparos_machine_level(tableros_maquina, tableros_player, number):
    """
    Ubica los disparos de la maquina con nivel mayor a 1
    INPUT : tableros_player (Objeto Clase Tablero)
            tableros_maquina (Objeto Clase Tablero)
            number (int) nivel de la máquina
    OUTPUT: messagebox.showinfo (str) informando al jugador si acierta o no la máquina, y por último si esta hunde todos los barcos del jugador
    """
    x_axis_inv = dict([(v,k) for k, v in x_axis.items()])   
    numberlevel = number    
    while numberlevel > 0:  
        machine_row = rd.randint(0, 9)
        machine_column = rd.randint(0, 9)          
        #Verifica que la máquina no vuelva a repetir el disparo
        if tableros_maquina.matriz_shooting[machine_row, machine_column] == "•" or tableros_maquina.matriz_shooting[machine_row, machine_column] == "X":
            continue                
        else:#Ubica los disparos de la máquina en el metodo 'disparos_maquina' de la Clase Tablero
            hit_miss_machine = tableros_maquina.disparos_machine(machine_row, machine_column, tableros_player) 

        if hit_miss_machine == True: #Diparo (Acierto)
            print(f"Player: {tableros_maquina.idplayer}. HIT!. Ubicación: ({(machine_row + 1)},{x_axis_inv[machine_column]})")    
            messagebox.showinfo(message = f"Player: {tableros_maquina.idplayer}. HIT!. Ubicación: ({(machine_row + 1)}, {x_axis_inv[machine_column]})", title="MACHINE HITS!")
        else: #No Diparo (Agua)
            print(f"Player: {tableros_maquina.idplayer}. MISS!. Ubicación: ({(machine_row + 1)},{x_axis_inv[machine_column]})") 
        
        counts_o_machine = tableros_maquina.matriz_shooting == "X"
        if counts_o_machine.sum() == 20: #Condición para la suma de los disparos acertados "X" de máquina con nivel
            print(f"Player: {tableros_player.idplayer}. YOU LOSE!\nPlayer: {tableros_maquina.idplayer} WINS")  
            messagebox.showinfo(message=f"Player: {tableros_player.idplayer}. YOU LOSE!\nPlayer: {tableros_maquina.idplayer} WINS"  , title="GAME OVER")
            mostrar_tableros_player(tableros_player.idplayer, tableros_player.matriz_ships, tableros_player.matriz_shooting)
            mostrar_tableros_machine(tableros_maquina.idplayer, tableros_maquina.matriz_ships, tableros_maquina.matriz_shooting)
            return True

        numberlevel -= 1  


def mostrar_tableros_player(name, tablero_ships, tablero_shooting):
    """
    Imprime los tableros del jugador
    INPUT : name (str) nombre o id del jugador
            tablero_ships (matriz) tableros de barcos
            tablero_shooting (matriz) tableros de disparos
    OUTPUT: print (str) tableros
    """
    rows, columns = dimensiones
    n = 0   
    print(f"                                   Player: {name}\n"
        "                  Tablero Barcos                                Tablero Disparos\n"
        "      A | B | C | D | E | F | G | H | I | J         A | B | C | D | E | F | G | H | I | J" )
    while n < rows:
        print(" "*(2-len(str(n+1))), n + 1, tablero_ships[n, :columns], " "*(2-len(str(n+1))), n + 1, tablero_shooting[n, :columns])
        n += 1


def mostrar_tableros_machine(name, tablero_ships, tablero_shooting):
    """
    Imprime los tableros de la máquina
    INPUT : name (str) máquina
            tablero_ships (matriz) tableros de barcos
            tablero_shooting (matriz) tableros de disparos
    OUTPUT: print (str) tableros
    """
    rows, columns = dimensiones
    n = 0   
    print(f"                                   Player: {name}\n"
        "                  Tablero Barcos                                Tablero Disparos\n"
        "      A | B | C | D | E | F | G | H | I | J         A | B | C | D | E | F | G | H | I | J" )
    while n < rows:
        print(" "*(2-len(str(n+1))), n + 1, tablero_ships[n, :columns], " "*(2-len(str(n+1))), n + 1, tablero_shooting[n, :columns])
        n += 1

def start_battleship(player_id):  
    """
    Función que empieza con el juego
    INPUT : player_id (str) Id o Nombre del jugador
    OUTPUT: messagebox.showinfo (str) 
    """
    global tableros_player  
    tableros_maquina = Tablero(dimensiones) #Crear tableros (barcos y disparos) de la máquina
    tableros_player = Tablero(dimensiones, player_id) #Crear tableros (barcos y disparos) del jugador
    
    barcos = crear_barcos()   
    tableros_player.colocar_barcos(barcos) #Ubicar barcos automáticamente del jugador
    tableros_maquina.colocar_barcos(barcos) #Ubicar barcos automáticamente de la máquina

    while True:
        level_choice = easygui.enterbox("Escoga el nivel de la máquina (mayor a 0). NOTA: Nivel 1 es un nivel normal. donde la máquina no tendra más de un disparo por turno, a menos que acierte:")
        try:
            if int(level_choice) > 0:
                break
        except:
            print("Escoga un número mayor a 0")
            continue

    choice_turn = rd.choice([1, 2])  
    if choice_turn == 1:
        print("Tú empiezas el juego")  
    else:
        print("La máquina empieza el juego")      

    while True:    
        mostrar_tableros_player(tableros_player.idplayer, tableros_player.matriz_ships, tableros_player.matriz_shooting)
        if choice_turn == 1 or choice_turn == 0:
            condicion_player_win = disparos_player(tableros_player, tableros_maquina) 
            if condicion_player_win == True:
                messagebox.showinfo(message= "Fin del Juego"  , title="Batalla Naval")
                return ("Fin del Juego") 
        
        choice_turn = 0      
                
        if choice_turn == 2 or choice_turn == 0:
            if int(level_choice) == 1:
                condicion_machine_win = disparos_machine(tableros_maquina, tableros_player)  
            else:
                condicion_machine_win = disparos_machine_level(tableros_maquina, tableros_player, int(level_choice)) 
            
            if condicion_machine_win == True:
                messagebox.showinfo(message= "Fin del Juego"  , title="Batalla Naval")
                return ("Fin del Juego")
      
        choice_turn = 0

def crear_barcos():
    """
    Instanciar los objetos de la Clase Barco que tiene como parametro el eslora o longitud del barco
    OUTPUT: barcos (list) objetos de la Clase Barco 
    """   
    barcos = []
    for i in range(len(list_eslora_ships)):
        barcos.append(Barco(list_eslora_ships[i]))
   
    return barcos

def exit_game():  
    """
    Al llamar dicha función, deja de ejecutar el menú del juego
    OUTPUT: sys(exit)  
    """   
    sys.exit("Exit")

def instructions():
    """
    Ejecuta la variable message_instructions  del script 'variables.py'
    OUTPUT: messagebox(str)
    """
    messagebox.showinfo(message= message_instructions  , title="Instrucciones")

def start_game(): 
    """
    Da a empezar la función 'start_battleship'
    OUTPUT: player_id (str) Id o Nombre del jugador
    """
    while True:
        player_id = easygui.enterbox("Ingrese su nombre o un id que lo identifique:")
    
        if player_id in ["", " ", None]:
            print("Ingrese un nombre o un id")
        else: 
            break
    start_battleship(player_id)

def table_jugador():
    """
    Imprime los tableros del jugador.
    OUTPUT: messagebox(str) 
    """ 
    try:
        print(tableros_player)
    except:
        print("No has iniciado el juego")
        messagebox.showinfo(message= "No has iniciado el juego"  , title="ERROR")
    
  


