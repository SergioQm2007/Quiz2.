import tkinter as tk
from tkinter import messagebox

conversion = 513.70  #Tasa de conversión de USD a CRC

def convertir():
    try:
        usd = float(entrada_dolares.get())  #Obtiene el valor en USD
        crc = usd * conversion  #Calcula la conversión a CRC
        resultado.config(text=f"{usd:.2f} USD = {crc:.2f} CRC")  #Muestra el resultado
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")  #Muestra un error si no es un número

def limpiar():
    entrada_dolares.delete(0, tk.END)  #Limpia el campo de entrada
    resultado.config(text="")  #Limpia el resultado

def cerrar_ventana():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):  #Pide confirmación antes de cerrar
        ventana.destroy()  #Cierra la ventana

#Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de USD a CRC")  #Título de la ventana
ventana.geometry("300x200")  #Tamaño de la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)  #Maneja el cierre de la ventana

#Etiqueta y entrada para el monto en USD
tk.Label(ventana, text="Ingrese monto en USD:").grid(row=0, column=0, padx=10, pady=10)
entrada_dolares = tk.Entry(ventana)  #Campo de texto para ingresar el valor en USD
entrada_dolares.grid(row=0, column=1)

#Botón para convertir el valor
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=0, columnspan=2, pady=10)

#Etiqueta para mostrar el resultado de la conversión
resultado = tk.Label(ventana, text="")
resultado.grid(row=2, column=0, columnspan=2)

#Botón para limpiar la entrada y el resultado
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=3, column=0, columnspan=2, pady=10)

#Inicia el bucle principal de la interfaz
ventana.mainloop()
