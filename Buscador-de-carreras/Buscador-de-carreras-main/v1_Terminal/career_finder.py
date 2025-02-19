import pandas as pd
from tabulate import tabulate

# Función para buscar carrera en el DataFrame
def buscar_carrera(df, carrera):
    # Filtrar DataFrame para encontrar carrera
    carreras_encontradas = df[df['GRADO'].str.lower() == carrera.lower()]
    
    if carreras_encontradas.empty:
        print("\nNo se encontró la carrera. Por favor, verifica el nombre completo.")
    else:
        # Extraer columnas necesarias y convertir a lista para tabular
        tabla = carreras_encontradas[['UNIVERSIDAD', 'GRADO', 'Corte Grupo 1', 'Corte Grupo 2']].values.tolist()
        # Imprimir en formato tabla
        print("\nResultados:")
        print(tabulate(tabla, headers=['Universidad', 'Grado', 'Corte Grupo 1', 'Corte Grupo 2'], tablefmt='grid'))

# Cargar el archivo Excel en un DataFrame de pandas
try:
    df = pd.read_excel('notas_de_corte_2024-25_-_ordinaria.xlsx')
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Solicitar el nombre de la carrera al usuario
carrera = input("Introduce el nombre completo de la carrera: ")

# Buscar la carrera
buscar_carrera(df, carrera)
