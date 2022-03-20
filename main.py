from funciones import exit_game, instructions, start_game, table_jugador
import tkinter as tk
from tkinter import ttk

#Menu principal del juego
"""
Opciones del juego que ejecuta las diferentes funcionalidades del juego como, instrucciones, comenzar juego,
Ver tableros y salir del juego.
Estas opciones ejecutan funciones del script funciones.py
"""
ventana = tk.Tk(className='Python Examples - Window Size')
ventana.geometry("350x100")
ventana.title(f"Menú: Battleship")
boton = ttk.Button(text= "Ver instrucciones", command=instructions).pack()
boton = ttk.Button(text= "Comenzar Juego", command=start_game).pack()   
boton = ttk.Button(text= "Ver tableros", command=table_jugador).pack()   
boton = ttk.Button(text= "Salir del juego", command=exit_game).pack()      
ventana.mainloop()

