# ESTE ES EL BUENO

import pandas as pd
from tkinter import Tk, Label, Button, filedialog, Frame, Scrollbar, ttk, END

# Función para cargar archivo
def cargar_archivo():
    global df
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel y CSV", "*.xlsx *.csv")])
    try:
        if archivo.endswith('.xlsx'):
            df = pd.read_excel(archivo)
        elif archivo.endswith('.csv'):
            df = pd.read_csv(archivo)
        else:
            limpiar_treeview()
            mensaje_error("Error: Formato de archivo no soportado.")
            return

        # Normalizar nombres de columnas
        df.columns = [col.strip().lower() for col in df.columns]

        # Validar columnas necesarias
        columnas_esperadas = ['universidad', 'grado', 'corte grupo 1', 'corte grupo 2']
        columnas_faltantes = [col for col in columnas_esperadas if col not in df.columns]

        if columnas_faltantes:
            limpiar_treeview()
            mensaje_error(f"Error: Faltan las columnas necesarias: {', '.join(columnas_faltantes)}")
            return

        # Eliminar filas con valores nulos en las columnas clave
        df.dropna(subset=['grado'], inplace=True)

        limpiar_treeview()
        mensaje_exito(f"Archivo cargado con éxito: {archivo}")
    except Exception as e:
        limpiar_treeview()
        mensaje_error(f"Error al cargar el archivo: {e}")

# Función para actualizar las opciones del Combobox
def actualizar_opciones(event=None):
    global df
    if df is None:
        mensaje_error("Error: No se ha cargado ningún archivo.")
        return

    termino = entrada_carrera.get()
    if termino.strip():
        opciones = sorted(
            df[df['grado'].str.contains(termino, case=False, na=False)]['grado'].unique()
        )
        entrada_carrera['values'] = opciones
    else:
        entrada_carrera['values'] = []

# Función para buscar carrera seleccionada
def buscar_carrera():
    global df
    if df is None:
        limpiar_treeview()
        mensaje_error("Error: No se ha cargado ningún archivo.")
        return

    carrera = entrada_carrera.get()
    if not carrera.strip():
        mensaje_error("Por favor, selecciona una carrera del desplegable.")
        return

    # Asegurarnos de manejar valores nulos y filtrar correctamente
    carreras_encontradas = df[df['grado'].fillna("").str.fullmatch(carrera, case=False)]

    limpiar_treeview()

    if carreras_encontradas.empty:
        mensaje_error("No se encontraron resultados para la carrera seleccionada.")
    else:
        # Mostrar resultados en el Treeview
        for _, fila in carreras_encontradas.iterrows():
            treeview.insert("", "end", values=(fila['universidad'], fila['grado'], fila['corte grupo 1'], fila['corte grupo 2']))

# Función para limpiar el Treeview
def limpiar_treeview():
    for row in treeview.get_children():
        treeview.delete(row)

# Función para mostrar mensajes de error
def mensaje_error(msg):
    etiqueta_mensaje.config(text=msg, foreground="red")

# Función para mostrar mensajes de éxito
def mensaje_exito(msg):
    etiqueta_mensaje.config(text=msg, foreground="green")

# Configuración de la interfaz
root = Tk()
root.title("Consulta de Notas de Corte")

# Frame superior: Botón para cargar archivo
frame_superior = Frame(root)
frame_superior.pack(pady=10)
boton_cargar = Button(frame_superior, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack()

# Entrada de texto para la carrera con Combobox
label_carrera = Label(root, text="Introduce el nombre de la carrera:")
label_carrera.pack()
entrada_carrera = ttk.Combobox(root, width=50)
entrada_carrera.pack()
entrada_carrera.bind("<KeyRelease>", actualizar_opciones)  # Actualizar opciones dinámicamente

# Botón para buscar carrera
boton_buscar = Button(root, text="Buscar Carrera", command=buscar_carrera)
boton_buscar.pack(pady=10)

# Área de resultados con Treeview
frame_resultados = Frame(root)
frame_resultados.pack(pady=10)

columns = ("Universidad", "Grado", "Corte Grupo 1", "Corte Grupo 2")
treeview = ttk.Treeview(frame_resultados, columns=columns, show="headings", height=15)
treeview.heading("Universidad", text="Universidad")
treeview.heading("Grado", text="Grado")
treeview.heading("Corte Grupo 1", text="Corte Grupo 1")
treeview.heading("Corte Grupo 2", text="Corte Grupo 2")
treeview.pack(side="left")

# Scrollbar para el Treeview
scrollbar = Scrollbar(frame_resultados, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Área para mensajes (errores o éxitos)
etiqueta_mensaje = Label(root, text="", wraplength=400, justify="center")
etiqueta_mensaje.pack(pady=5)

# Variable global para almacenar el DataFrame
df = None

root.mainloop()
