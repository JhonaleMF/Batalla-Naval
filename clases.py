import numpy as np
import random as rd

from variables import orientation, dimensiones
class Barco: 
    def __init__(self, eslora):
        """
        Clase Barco, constructor
        INPUT: eslora (int) longitud de cada uno de los barcos
        OUTPUT: Instancias de la clase Barco
        """  
        self.eslora_barco = eslora

class Tablero:
   
    def __init__(self, dimensiones, id = "Machine"):
        """
        Clase Tablero, constructor
        INPUT: dimensiones (int) dimensiones de los tableros
               id (str) nombre o id del jugador o máquina, por default
        OUTPUT: Instancias de la clase Tablero
        """  
        self.idplayer = id
        self.matriz_ships = np.full((dimensiones), "≈")
        self.matriz_shooting = np.full((dimensiones), "≈") 

    def disparos_player(self, row, column, tableros_maquina): 
        """
        Ubica los disparos del jugador en los tableros
        INPUT: row(int) indice fila de la matriz (0-9)
               column (int) indica columna de la matriz (0-9)
               tableros_maquina (matriz)  tablero de barcos de la máquina
        OUTPUT: Boolean, True, si el jugador acierta el disparo, y False, lo contratrio.
        """         
        if tableros_maquina.matriz_ships[row, column] == "█":
            self.matriz_shooting[row, column] = "X"
            tableros_maquina.matriz_ships[row, column] = "X"    
            return True 
        else:
            self.matriz_shooting[row, column] = "•"
            tableros_maquina.matriz_ships[row, column] = "•"
            return False

    def disparos_machine(self, row, column, tableros_player):
        """
        Ubica los disparos de la maquina en los tableros
        INPUT: row(int) indice fila de la matriz (0-9)
               column (int) indica columna de la matriz (0-9)
               tableros_player (matriz) tablero de barcos de la máquina
        OUTPUT: Boolean, True, si el jugador acierta el disparo, y False, lo contratrio.
        """  
        if tableros_player.matriz_ships[row, column] == "█":
            self.matriz_shooting[row, column] = "X"
            tableros_player.matriz_ships[row, column] = "X"    
            return True 
        else:
            self.matriz_shooting[row, column] = "•"
            tableros_player.matriz_ships[row, column] = "•"    
            return False        

    def colocar_barcos(self, barcos_eslora):
        """
        Ubica los barcos de manera automática en el tablero matriz_ships
        INPUT: barcos_eslota (list) lista con 10 esloras o longitudes de barcos
        OUTPUT: matriz_ships (matriz) barcos ubicados
        """ 
        list_ocupados_total = []
        list_ship_position_total = []
        count_ships_onboard = 0
        
        while True:            
            choice_o = rd.choice(orientation) #Random orientación         

            if choice_o == "N":  # Norte          
                while True:
                    list_ocupados = []
                    list_ship_position = []
                    initial_fila = rd.randint(0, 9)
                    initial_columna = rd.randint(0, 9)
                    for position in range(initial_fila - barcos_eslora[count_ships_onboard].eslora_barco + 1, initial_fila + 1):
                        list_ship_position.append((position, initial_columna))
                    
                    if (initial_fila - barcos_eslora[count_ships_onboard].eslora_barco + 1) > -1:                
                        for i in range(initial_fila - barcos_eslora[count_ships_onboard].eslora_barco, initial_fila + 2):
                            for j in range(initial_columna - 1, initial_columna + 2):
                                if ((i >= 0) and (i <10)) and ((j >= 0) and (j <10)):
                                    list_ocupados.append((i, j))

                        count = 0
                        for o in list_ship_position:
                            for h in list_ocupados_total:
                                if o == h:
                                    count += 1

                        if count > 0:        
                            continue
                        else:
                            list_ship_position_total += list_ship_position
                            list_ocupados_total += list_ocupados                     

                        self.matriz_ships[initial_fila-10:(initial_fila- 10  - barcos_eslora[count_ships_onboard].eslora_barco):-1, initial_columna] = "█"
                        count_ships_onboard += 1
                        break
                    else:
                        continue               

            elif choice_o == "S": # Sur
                while True:
                    list_ocupados = []
                    list_ship_position = []
                    initial_fila = rd.randint(0, 9)
                    initial_columna = rd.randint(0, 9)
                    for position in range(initial_fila, initial_fila + barcos_eslora[count_ships_onboard].eslora_barco):
                        list_ship_position.append((position, initial_columna))

                    if (initial_fila + barcos_eslora[count_ships_onboard].eslora_barco - 1) < len(self.matriz_ships):
                        for i in range(initial_fila - 1, initial_fila + barcos_eslora[count_ships_onboard].eslora_barco + 1):
                            for j in range(initial_columna - 1, initial_columna + 2):
                                if ((i >= 0) and (i <10)) and ((j >= 0) and (j <10)):
                                    list_ocupados.append((i, j))

                        count = 0
                        for o in list_ship_position:
                            for h in list_ocupados_total:
                                if o == h:
                                    count += 1

                        if count > 0:        
                            continue
                        else:
                            list_ship_position_total += list_ship_position
                            list_ocupados_total += list_ocupados                  

                        self.matriz_ships[initial_fila:(initial_fila + barcos_eslora[count_ships_onboard].eslora_barco), initial_columna] = "█"
                        count_ships_onboard += 1
                        break
                    else:
                        continue

            elif choice_o == "E": # Este
                while True:
                    list_ocupados = []
                    list_ship_position = []
                    initial_fila = rd.randint(0, 9)
                    initial_columna = rd.randint(0, 9)
                    for position in range(initial_columna, initial_columna + barcos_eslora[count_ships_onboard].eslora_barco):
                        list_ship_position.append((initial_fila, position))
                    if initial_columna + barcos_eslora[count_ships_onboard].eslora_barco - 1 < len(self.matriz_ships):
                        for i in range(initial_fila - 1, initial_fila  + 2):
                            for j in range(initial_columna - 1, initial_columna + barcos_eslora[count_ships_onboard].eslora_barco +  1):
                                if ((i >= 0) and (i <10)) and ((j >= 0) and (j <10)):
                                    list_ocupados.append((i, j))

                        count = 0
                        for o in list_ship_position:
                            for h in list_ocupados_total:
                                if o == h:
                                    count += 1

                        if count > 0:        
                            continue
                        else:
                            list_ship_position_total += list_ship_position
                            list_ocupados_total += list_ocupados 
                
                        self.matriz_ships[initial_fila, initial_columna:(initial_columna + barcos_eslora[count_ships_onboard].eslora_barco)] = "█"
                        count_ships_onboard += 1
                        break
                    else:
                        continue

            else: # Oeste
                while True:
                    list_ocupados = []
                    list_ship_position = []
                    initial_fila = rd.randint(0, 9)
                    initial_columna = rd.randint(0, 9)
                    for position in range(initial_columna - barcos_eslora[count_ships_onboard].eslora_barco + 1, initial_columna + 1):
                        list_ship_position.append((initial_fila, position))
                    if (initial_columna - barcos_eslora[count_ships_onboard].eslora_barco + 1) > -1:
                        for i in range(initial_fila - 1, initial_fila + 2):
                            for j in range(initial_columna - barcos_eslora[count_ships_onboard].eslora_barco, initial_columna + 2):
                                if ((i >= 0) and (i <10)) and ((j >= 0) and (j <10)):
                                    list_ocupados.append((i, j))

                        count = 0
                        for o in list_ship_position:
                            for h in list_ocupados_total:
                                if o == h:
                                    count += 1

                        if count > 0:        
                            continue
                        else:
                            list_ship_position_total += list_ship_position
                            list_ocupados_total += list_ocupados       

                        self.matriz_ships[initial_fila, initial_columna - 10:(initial_columna -10 - barcos_eslora[count_ships_onboard].eslora_barco):-1] = "█"
                        count_ships_onboard += 1
                        break
                    else:
                        continue       

            if count_ships_onboard  == 10:    
                                 
                return list_ship_position_total 

    def __repr__(self):
        """
        Clase Tablero, representar la instancia de la clase como un string.
        OUTPUT: tableros (str) Tableros de barcos y disparos
        """ 
        rows, columns = dimensiones
        n = 0   
        tableros = (f"                                   Player: {self.idplayer}\n"
        "                  Tablero Barcos                                Tablero Disparos\n"
        "      A | B | C | D | E | F | G | H | I | J         A | B | C | D | E | F | G | H | I | J\n" )
        while n < rows:
            espacios = " "*(2-len(str(n+1)))
            tablero_ship = self.matriz_ships[n, :columns]
            tablero_shooting = self.matriz_shooting[n, :columns]
            tableros += f" {espacios} {(n + 1)} {tablero_ship} {espacios} {(n + 1)} {tablero_shooting}\n"
            n += 1

        return tableros



